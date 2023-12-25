from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def print_title():
    title = "欢迎使用PVZRandomScript--！"
    title_panel = Panel.fit(title, border_style="cyan", padding=(0, 2))
    align_title = Align.center(title_panel)
    console.print(align_title, style="bold cyan")

def print_options():
    options = ["默认开始","选择关卡", "选择植物卡组", "全自定义游戏", "退出脚本"]
    for i, option in enumerate(options):
        console.print(f"{i+1}. {option}")

def main():
    print_title()
    print_options()

    while True:
        user_input = Prompt.ask("请选择功能：", choices=["1", "2", "3", "4", "0"], default="1")

        if user_input == '1':
            # 执行现有默认开始
            pass
        elif user_input == '2':
            # 执行选择关卡
            pass
        elif user_input == '3':
            # 执行选择植物卡组
            pass
        elif user_input == '4':
            # 执行选择植物卡组
            pass 
        elif user_input == '0':
            # 退出脚本
            break
