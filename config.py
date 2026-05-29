from dataclasses import dataclass


@dataclass
class AppConfig:
    window_title_keyword: str = "洛克王国：世界"
    click_interval_min_sec: float = 0.5
    click_interval_max_sec: float = 1.5


CONFIG = AppConfig()
