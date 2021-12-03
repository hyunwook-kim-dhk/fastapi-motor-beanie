from functools import lru_cache

import toml

from app.common.util.path import get_root_path


@lru_cache
def get_project_version() -> str:
    root_path = get_root_path()
    parsed_result = toml.load(root_path / "pyproject.toml")
    return str(parsed_result["tool"]["poetry"]["version"])
