import os


def ensure_directory(path: str):
    """Create directory if not exists."""
    os.makedirs(path, exist_ok=True)

