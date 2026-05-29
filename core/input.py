import random

import interception
import win32gui

_interception_ready = False


def _ensure_interception() -> None:
    global _interception_ready
    if not _interception_ready:
        interception.auto_capture_devices()
        _interception_ready = True


def click_at(hwnd: int, x: int, y: int) -> bool:
    try:
        _ensure_interception()
        sx, sy = win32gui.ClientToScreen(hwnd, (x, y))
        interception.click(
            sx + random.randint(-2, 2),
            sy + random.randint(-2, 2),
            delay=random.uniform(0.05, 0.12),
        )
        return True
    except Exception:
        return False
