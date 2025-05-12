#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/1 11:59
@Author  : adamzh0u
@File    : const.py
"""

import glob
import os
import tomllib
from pathlib import Path

from loguru import logger


# ===============================================================
# path settings
# ===============================================================
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
        parent_path = current_path.parent
        if parent_path == current_path:
            # loop until top level and land cwd
            cwd = Path.cwd()
            logger.info(f"PROJECT_ROOT set to current working directory: {str(cwd)}")
            return cwd
        current_path = parent_path


ROOT = get_project_root()
PATH_DATA = ROOT / "data"
PATH_NOTEBOOKS = ROOT / "notebooks"
PATH_LOGS = ROOT / "logs"
PATH_CONFIG = ROOT / "config"

# ===============================================================
# logger
# ===============================================================
ENV = os.environ.get("ENV", "dev")

logger.add(
    os.path.join(
        PATH_LOGS,
        f"log_{ENV}.log",  # Use environment in log filename
    ),
    rotation="500 MB",  # Rotate logs when they exceed 500MB
    retention="10 days",  # Keep logs for 10 days
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)


def get_logger():
    return logger


# ===============================================================
# config params
# ===============================================================


def load_config(CONFIG_FILES):
    """
    Load config files, prioritize environment-specific configs, inherit missing configs from base config
    :return: dict
    """
    final_config = {}
    for file in CONFIG_FILES:
        with open(file, "rb") as f:
            config = tomllib.load(f)
        final_config.update(config)
    return final_config


try:
    config_files = glob.glob(f"{PATH_CONFIG}/*.toml")
    CONFIG = load_config(config_files)
except Exception as e:
    logger.error(f"Error loading config: {e}")
    raise e


if __name__ == "__main__":
    print(PATH_DATA)
    print(PATH_NOTEBOOKS)
    print(PATH_LOGS)

    print(CONFIG)
    print(os.environ["PYTHONPATH"])

    print(get_logger())
