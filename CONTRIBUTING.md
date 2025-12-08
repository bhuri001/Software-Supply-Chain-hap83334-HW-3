# Contributing to the Python Rekor Verifier

We warmly welcome contributions to this project! Whether you’re fixing a bug, adding a new feature, or improving our documentation, your contributions are invaluable.

## How to Contribute

### Reporting Issues

If you discover a bug or have suggestions for improvement, please open an issue on GitHub. Include as much detail as possible, including:
- A clear and concise title.
- Steps to reliably reproduce the issue.
- The expected behavior compared to the actual behavior.
- Information about your environment (e.g., Python version, operating system).

### Submitting Pull Requests

1. **Fork the repository** and create a new branch from `main`.
2. **Make your changes** in your feature branch.
3. **Write tests** to validate any new functionality.
4. **Ensure your code adheres to style guidelines** and passes all existing tests.
5. **Update the documentation** (e.g., `README.md`) as necessary to reflect your changes.
6. **Submit a pull request** to the `main` branch of the original repository.

## Code Style

This project adheres to standard Python style guidelines (PEP 8). We use tools like `pylint` and `ruff` to maintain high code quality. Before submitting a pull request, ensure that your code passes these tools locally to meet the project's style standards.

## Code of Conduct

This project operates under a Contributor Code of Conduct, and your participation signifies your commitment to its principles. (Feel free to add a `CODE_OF_CONDUCT.md` file if you choose.)

Thank you for being a part of this project and sharing your talents!

## Requirements for Acceptable Contributions

To maintain code quality and consistency, all pull requests **must** meet the following requirements.  
These are the same checks that run in GitHub Actions (CI).

### 1. Code formatting

All Python code must be formatted with **Black** before opening a pull request:

```bash
poetry run black .
