
# pyproject.toml
- [tool.ruff]
    This section configures the Ruff linter, a fast Python linter and code formatter.
    target-version="py313":

    Specifies the Python version that Ruff should target. In this case, it is Python 3.13.
    This ensures that Ruff understands the syntax and features available in Python 3.13.
    line-length=100:

    Sets the maximum allowed line length for the code. Ruff will enforce this limit and flag lines that exceed 100 characters.

- [tool.ruff.lint]

This section specifies the linting rules that Ruff should apply.

    select=['E','F','I','W','UP']:
    Defines the categories of linting rules to enable:
    E: Errors (e.g., PEP 8 violations like indentation issues).
    F: Pyflakes checks (e.g., unused imports, undefined variables).
    I: Import-related checks (e.g., sorting imports).
    W: Warnings (e.g., deprecated syntax).
    UP: Upgrade Python checks (e.g., identifying outdated syntax that can be modernized).

- [tool.pytest.ini_opinions]

    asyncio_mode="auto":

    Automatically detects whether tests use asyncio and adjusts the test execution mode accordingly.
    Useful for projects that include asynchronous code.
    testpaths=['tests']:

    Specifies the directory where pytest should look for test files. In this case, it is the tests folder.

- [tool.hatch.build.targets.wheel]

    This section configures Hatch, a modern Python packaging tool, for building a wheel distribution.

    packages=['app']:
    Specifies the package(s) to include in the wheel build. Here, the app package will be included.