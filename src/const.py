#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/1 11:59
@Author  : adamzh0u
@File    : const.py
"""
from pathlib import Path
from loguru import logger

def get_project_root():
    """Search upwards to find the project root directory."""
    current_path = Path.cwd()
    while True:
        if (
            (current_path / ".git").exists()
            or (current_path / ".project_root").exists()
            or (current_path / ".gitignore").exists()
        ):
            logger.info(f"PROJECT_ROOT set to {str(current_path)}")
            return current_path
        current_path = current_path.parent


PROJECT_ROOT = get_project_root()
DATA_PATH = PROJECT_ROOT / "data"
NOOTBOOKS_ROOT = PROJECT_ROOT / "notebooks"
LOG_PATH = PROJECT_ROOT / "logs"

