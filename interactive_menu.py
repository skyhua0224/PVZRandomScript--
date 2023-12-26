from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress
import time
from game_operations import *
from keyboard_event import *

console = Console()


isStart = False

mode_dict = {
    "1": "默认关卡",
    "2": "冒险模式",
    "3": "小游戏模式",
    "4": "解谜模式",
    "5": "生存模式",
    "6": "随机模式"
}

plant_dict = {
    "1": "默认卡组",
    "2": "4个模仿者卡组",
    "3": "3个模仿者卡组",
    "4": "全模仿者卡组",
    "5": "卡组",
    "6": "随机卡组",
    "7": "自定义卡组"
}

# 添加一个全局变量
global return_to_menu
return_to_menu = False

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

def start_game(mode_input, plant_input):
    global isStart
    global return_to_menu
    isStart = True
    console.clear()
    console.print(f"你选择的模式是：[bold cyan]{mode_dict[mode_input]}[/bold cyan]")
    console.print(f"你选择的卡组是：[bold cyan]{plant_dict[plant_input]}[/bold cyan]")
    console.print("请通过快捷键Ctrl+1，Ctrl+2，Ctrl+3进行快捷操作，或通过快捷键Ctrl+0回到主菜单", style="bold cyan")
    console.print("正在启动游戏与修改器，请稍后...", style = "bold cyan")
    with Progress() as progress:
        task = progress.add_task("[cyan]启动中...", total=5)
        for i in range(5, 0, -1):
            if return_to_menu:
                return_to_menu = False
                return
            time.sleep(1)
            progress.update(task, advance=1)
    print_game_running_screen()
    StartGame(mode_dict[mode_input],plant_dict[plant_input])#game_operations的函数


def main():
    global return_to_menu
    isStart = False
    while isStart == False and return_to_menu == False:
        console.clear()
        print_title("欢迎使用PVZRandomScript--！")
        print_options(["默认开始", "自定义游戏", "随机游戏", "游戏版本"])
        user_input = Prompt.ask("请选择功能：", choices=["1", "2", "3", "4", "0"], default="1")

        if user_input == '1':
            mode_input = '1'  # 默认关卡
            plant_input = '1'  # 默认卡组
        elif user_input in ['2', '3']:
            while True and return_to_menu == False:
                console.clear()
                if user_input == '2':
                    print_title("请选择模式：")
                    print_options(list(mode_dict.values()))
                    mode_input = Prompt.ask("请选择模式：", choices=list(mode_dict.keys()) + ['0'], default = "1")
                    console.clear()
                    
                    print_title("请选择植物卡组：")
                    console.print(f"你选择的卡组是：[bold cyan]{mode_dict[mode_input]}[/bold cyan]", )
                    print_options(list(plant_dict.values()))
                    plant_input = Prompt.ask("请选择卡组：", choices=list(plant_dict.keys()) + ['0'], default = "1")
                
                if mode_input == '0' or plant_input == '0':
                    break
                    
                if mode_input != None and plant_input != None:
                    start_game(mode_input, plant_input)

                break
        elif user_input == '0':
            break

        start_game(mode_input, plant_input)
        #KeyboardEvent().KeyboardWait()