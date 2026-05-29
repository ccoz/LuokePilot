"""Build standalone executable using PyInstaller.

Usage:
    python build.py
"""

import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
DIST_DIR = PROJECT_DIR / "dist"
BUILD_DIR = PROJECT_DIR / "build"
NAME = "RocoPilot"


def _rmtree(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path, ignore_errors=True)


def build() -> None:
    _rmtree(BUILD_DIR)
    _rmtree(DIST_DIR / NAME)

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--onedir",
        "--console",
        f"--paths={PROJECT_DIR}",
        "--clean",
        f"--name={NAME}",
        "main.py",
    ]

    subprocess.check_call(cmd, cwd=PROJECT_DIR)

    out_dir = DIST_DIR / NAME
    for doc in ("README.md", "LICENSE"):
        src = PROJECT_DIR / doc
        if src.exists():
            shutil.copy2(src, out_dir / doc)

    print(f"\n[OK] {NAME} built -> {out_dir}")


if __name__ == "__main__":
    build()
