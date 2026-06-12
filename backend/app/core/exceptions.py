import structlog
from  fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

logger = structlog.get_logger(__name__)

class RAGException(Exception):
    def __init__(self, message: str)-> None:
        self.message=message
        super().__init__(message)

class NotFoundError(RAGException):
    pass

class AuthenticationError(RAGException):
    pass

class AuthorizationError(RAGException):
    pass

def register_exception_handlers(app: FastAPI)-> None:

    @app.exception_handler(RAGException)
    async def rag_handler(request: Request, exc: RAGException) -> ORJSONResponse:
        status_map={
            NotFoundError: status.HTTP_404_NOT_FOUND,
            AuthenticationError: status.HTTP_401_UNAUTHORIZED,
            AuthenticationError: status.HTTP_403_FORBIDDEN,
        }

        code = status_map.get(type(exc), status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.warning("domain error", type=type(exc).__name__, message=exc.message)
        return ORJSONResponse(
            status_code=code,
            content={"error":type(exc).__name__, "message": exc.message},
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_handler(request: Request, exc: RequestValidationError) -> ORJSONResponse:
        return ORJSONResponse(
            status_code=status.HTTP_402_UNPROCESSABLE_ENTITY,
            content={"error":"ValidationError", "message": exc.errors()},
        )

    @app.exception_handler(Exception)
    async def unhandled_handler(request: Request, exc: Exception) -> ORJSONResponse:
        logger.exception("unhandled error", exc_info=exc)
        return ORJSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error":"InternalServerError", "message": "Something went wrong"},
        ) 

    