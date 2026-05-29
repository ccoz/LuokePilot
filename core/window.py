import ctypes
from typing import List, Tuple

import win32gui

try:
    ctypes.windll.user32.SetProcessDPIAware()
except Exception:
    pass


def list_windows_by_keyword(keyword: str) -> List[Tuple[int, str, Tuple[int, int, int, int]]]:
    results: List[Tuple[int, str, Tuple[int, int, int, int]]] = []
    for hwnd, title in _enum_matching_windows(keyword):
        results.append((hwnd, title, get_client_rect_on_screen(hwnd)))
    return results


def _enum_matching_windows(keyword: str) -> list[tuple[int, str]]:
    matches: list[tuple[int, str]] = []

    def _enum_handler(hwnd: int, _ctx: object) -> None:
        if not win32gui.IsWindowVisible(hwnd):
            return
        if win32gui.IsIconic(hwnd):
            return
        title = win32gui.GetWindowText(hwnd)
        if title and keyword in title:
            matches.append((hwnd, title))

    win32gui.EnumWindows(_enum_handler, None)
    return matches


def get_client_rect_on_screen(hwnd: int) -> Tuple[int, int, int, int]:
    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    width = right - left
    height = bottom - top
    screen_left, screen_top = win32gui.ClientToScreen(hwnd, (0, 0))
    return screen_left, screen_top, width, height
