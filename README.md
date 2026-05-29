# RocoPilot

RocoPilot 现在只保留一个目标：基于 Interception 驱动级输入，按 0.5 到 2 秒随机间隔点击游戏窗口客户区中心点。

## 功能

- 枚举标题包含 `洛克王国：世界` 的游戏窗口
- 计算所选窗口客户区中心点
- 使用 `interception-python` 通过 Interception 驱动点击中心点

## 环境

- Windows 10/11
- Python 3.11+
- 管理员权限
- 已安装 Interception 驱动

## 安装

```powershell
uv sync
```

或手动安装依赖：

```powershell
pip install pywin32 interception-python
```

## 运行

```powershell
uv run python main.py
```

选择游戏窗口后，程序会随机等待 `0.5` 到 `2.0` 秒点击一次界面中心。可在 [config.py](config.py) 中修改窗口标题关键字和随机间隔范围。

## 项目结构

```text
main.py       # 入口：选择窗口并循环点击中心点
config.py     # 窗口关键字和点击间隔
build.py      # PyInstaller 打包脚本
core/
  input.py    # Interception 点击
  util.py     # 时间戳
  window.py   # 窗口枚举和客户区坐标
```

## 注意

- 游戏窗口不能最小化。
- 默认只在目标窗口位于前台时点击，避免误点其他窗口。
- 使用自动化脚本可能违反游戏用户协议，相关风险由使用者自行承担。
