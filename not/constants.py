"""Unchanging values that would be inappropriate for config"""
from enum import Enum
from pathlib import Path
import re
from typing import List, Set

from .localization import polyglot as glot

VALID_TASK_SPEC_EXTENSION_NAMES: List = ["yml", "yaml"]
STEP_SEPARATOR: str = "\n\n"
TASK_SPEC_EXT_PATTERN = re.compile(r"(\.yml|\.yaml)$")

CWD: Path = Path.cwd()
HOME: Path = Path.home()

DOT_NOTHING_DIRECTORY_NAME: str = ".nothing"
CWD_DOT_NOTHING_DIR: Path = CWD / DOT_NOTHING_DIRECTORY_NAME
HOME_DOT_NOTHING_DIR: Path = HOME / DOT_NOTHING_DIRECTORY_NAME

FIELD_NAMES_EXCLUDED_FROM_CLEANED_TASK_SPEC: Set = {"filename"}


class DirectoryChoicesForListCommand(str, Enum):
    cwd = glot["cwd"]
    home = glot["home"]
    both = glot["both"]
