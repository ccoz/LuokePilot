import random
import time

import win32gui

from config import CONFIG
from core.input import click_at
from core.util import _ts
from core.window import get_client_rect_on_screen, list_windows_by_keyword


def _select_window() -> int | None:
    keyword = CONFIG.window_title_keyword
    windows = list_windows_by_keyword(keyword)

    if not windows:
        print(f'\n[错误] 未找到包含 "{keyword}" 的窗口，请确认游戏已经启动。')
        return None

    print(f'\n找到 {len(windows)} 个匹配 "{keyword}" 的窗口：\n')
    for i, (hwnd, title, (x, y, w, h)) in enumerate(windows, 1):
        print(f"  {i}. {title}")
        print(f"     句柄: {hwnd}  位置: ({x}, {y})  尺寸: {w}x{h}\n")

    if len(windows) == 1:
        hwnd, title, _ = windows[0]
        print(f"仅找到一个窗口，自动选择: {title}\n")
        return hwnd

    while True:
        sel = input(f"请选择窗口 (1-{len(windows)}): ").strip()
        try:
            idx = int(sel) - 1
            if 0 <= idx < len(windows):
                hwnd, title, _ = windows[idx]
                print(f"\n已选择: {title}\n")
                return hwnd
        except ValueError:
            pass
        print(f"输入无效，请输入 1-{len(windows)} 的数字。")


def _throw_ball_at_center(hwnd: int) -> None:
    if win32gui.GetForegroundWindow() != hwnd:
        print(f"[{_ts()}] 跳过：目标窗口不是前台窗口")
        return

    _left, _top, width, height = get_client_rect_on_screen(hwnd)
    if width <= 0 or height <= 0:
        print(f"[{_ts()}] 跳过：窗口尺寸无效 {width}x{height}")
        return

    x = width // 2
    y = height // 2
    if click_at(hwnd, x, y):
        print(f"[{_ts()}] 已点击界面中心 ({x}, {y})")
    else:
        print(f"[{_ts()}] [警告] 点击失败")


def main() -> None:
    print("\nRocoPilot 自动丢球")
    print("[提示] 不做图像检测，选定窗口后随机间隔点击界面中心。")

    hwnd = _select_window()
    if hwnd is None:
        return

    print(f"[{_ts()}] 已启动，按 Ctrl+C 退出。")
    while True:
        _throw_ball_at_center(hwnd)
        interval = random.uniform(CONFIG.click_interval_min_sec, CONFIG.click_interval_max_sec)
        time.sleep(interval)


if __name__ == "__main__":
    main()
