# Z-Verifier

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
```

## Manage package using poetry

```bash
# Add new package
poetry add <package-name>

# Add new package to group
poetry add <package-name> --group <group-name>

# Remove package
poetry remove <package-name>

# Remove package from group
poetry remove <package-name> --group <group-name>
```

## Pre-commit

```bash
# Install pre-commit (Just once)
pre-commit install

# Run pre-commit
git add .
pre-commit run -a
```
