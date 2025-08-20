from __future__ import annotations

from importlib.resources import files
from typing import Any, Dict, List

import yaml

PKG = "mcpstack_jupyter.tools.jupyter.configuration"

def _load_yaml(name: str) -> dict:
    with files(PKG).joinpath(name).open("rb") as f:
        data = yaml.safe_load(f)
    return data or {}


def load_env_defaults() -> Dict[str, Any]:
    return _load_yaml("env_defaults.yaml")

def load_cli_defaults() -> Dict[str, Any]:
    return _load_yaml("cli_defaults.yaml")


def load_known_tools() -> Dict[str, List[str]]:
    data = _load_yaml("tools.yaml")
    data.setdefault("known_tools", [])
    data.setdefault("read_only", [])
    return data