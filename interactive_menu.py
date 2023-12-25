from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress
import time
#import keyboard

console = Console()

mode_dict = {
    "1": "冒险模式",
    "2": "小游戏模式",
    "3": "解谜模式",
    "4": "生存模式",
    "5": "随机模式",
    "0": "默认关卡"
}

plant_dict = {
    "1": "4个模仿者卡组",
    "2": "3个模仿者卡组",
    "3": "全模仿者卡组",
    "4": "卡组",
    "5": "随机卡组",
    "6": "自定义卡组",
    "0": "默认卡组"
}

def print_title(title):
    title_panel = Panel.fit(title, border_style="cyan", padding=(0, 2))
    align_title = Align.center(title_panel)
    console.print(align_title, style="bold cyan")

def print_options(options):
    for i, option in enumerate(options, start=1):
        console.print(f"{i}. {option}")
    console.print("0. 退出脚本")

def print_game_running_screen():
    console.clear()
    console.print("游戏运行中...", style="bold cyan")
    console.print("请通过快捷键Ctrl+1，Ctrl+2，Ctrl+3进行快捷操作，或通过快捷键Ctrl+0回到主菜单", style="bold cyan")

def start_game(mode_name, plant_name):
    console.clear()
    console.print(f"你选择的模式是：[bold cyan]{mode_dict[mode_name]}[/bold cyan]")
    console.print(f"你选择的卡组是：[bold cyan]{plant_dict[plant_name]}[/bold cyan]")
    console.print("正在启动游戏与修改器，请稍后...", style="bold cyan")
    with Progress() as progress:
        task = progress.add_task("[cyan]启动中...", total=5)
        for i in range(5, 0, -1):
            time.sleep(1)
            progress.update(task, advance=1)
    print_game_running_screen()

def main():
    while True:
        console.clear()
        print_title("欢迎使用PVZRandomScript--！")
        print_options(["默认开始","选择关卡", "选择植物卡组", "全自定义游戏", "全随机游戏"])

        user_input = Prompt.ask("请选择功能：", choices=["1", "2", "3", "4", "0"], default="1")

        if user_input == '1':
            start_game("0", "0")
        elif user_input in ['2', '3', '4']:
            while True:
                console.clear()
                mode_input = "0"  # 默认关卡
                plant_input = "0"  # 默认卡组
                if user_input == '2':
                    console.print(f"你选择的卡组是：[bold cyan]默认卡组[/bold cyan]")
                    print_title("请选择模式：")
                    print_options(list(mode_dict.values())[:-1])  # 不包括"默认关卡"
                    mode_input = Prompt.ask("请选择模式：", choices=list(mode_dict.keys())[:-1], default="1")  # 不包括"默认关卡"
                elif user_input == '3':
                    console.print(f"你选择的关卡是：[bold cyan]默认关卡[/bold cyan]")
                    print_title("请选择植物卡组：")
                    print_options(list(plant_dict.values())[:-1])  # 不包括"默认卡组"
                    plant_input = Prompt.ask("请选择卡组：", choices=list(plant_dict.keys())[:-1], default="1")  # 不包括"默认卡组"
                elif user_input == '4':
                    print_title("请选择模式：")
                    print_options(list(mode_dict.values())[:-1])  # 不包括"默认关卡"
                    mode_input = Prompt.ask("请选择模式：", choices=list(mode_dict.keys())[:-1], default="1")  # 不包括"默认关卡"
                    print_title("请选择植物卡组：")
                    print_options(list(plant_dict.values())[:-1])  # 不包括"默认卡组"
                    plant_input = Prompt.ask("请选择卡组：", choices=list(plant_dict.keys())[:-1], default="1")  # 不包括"默认卡组"
                start_game(mode_input, plant_input)
                print_game_running_screen()
                #keyboard.wait('ctrl+0')
                break
        elif user_input == '0':
            break