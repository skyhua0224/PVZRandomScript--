from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress
import time
from pynput import keyboard

console = Console()

def print_title():
    title = "欢迎使用PVZRandomScript--！"
    title_panel = Panel.fit(title, border_style="cyan", padding=(0, 2))
    align_title = Align.center(title_panel)
    console.print(align_title, style="bold cyan")

def print_options():
    options = ["默认开始","选择关卡", "选择植物卡组", "全自定义游戏", "全随机游戏"]
    for i, option in enumerate(options, start=1):
        console.print(f"{i}. {option}")
    console.print("0. 退出脚本")

def print_mode_menu_options():
    options = ["冒险模式", "小游戏模式", "解谜模式", "生存模式", "随机模式"]
    for i, option in enumerate(options, start=1):
        console.print(f"{i}. {option}")
    console.print("0. 返回上级菜单")

def print_mode_menu_title():
    title = "请选择模式："
    title_panel = Panel.fit(title, border_style="cyan", padding=(0, 2))
    align_title = Align.center(title_panel)
    console.print(align_title, style="bold cyan")
    
def print_plant_menu_options():
    options = ["4个模仿者卡组", "3个模仿者卡组", "全模仿者卡组", "卡组", "随机卡组", "自定义卡组"]
    for i, option in enumerate(options, start=1):
        console.print(f"{i}. {option}")
    console.print("0. 返回上级菜单")

def print_plant_menu_title():
    title = "请选择植物卡组："
    title_panel = Panel.fit(title, border_style="cyan", padding=(0, 2))
    align_title = Align.center(title_panel)
    console.print(align_title, style="bold cyan")
    
def print_game_running_screen():
    console.clear()
    console.print("游戏运行中...", style="bold cyan")
    console.print("请通过快捷键Ctrl+1，Ctrl+2，Ctrl+3进行快捷操作，或通过快捷键Ctrl+0回到主菜单", style="bold cyan")

def main():
    while True:
        console.clear()
        print_title()
        print_options()

        user_input = Prompt.ask("请选择功能：", choices=["1", "2", "3", "4", "0"], default="1")

        if user_input == '1':
            # 执行现有默认开始
            mode_name = "默认关卡"
            plant_name = "默认卡组"
            console.clear()
            console.print(f"你选择的关卡是：[bold cyan]{mode_name}[/bold cyan]")
            console.print(f"你选择的卡组是：[bold cyan]{plant_name}[/bold cyan]")
            console.print("正在启动游戏与修改器，请稍后...", style="bold cyan")
            with Progress() as progress:
                task = progress.add_task("[cyan]启动中...", total=5)
                for i in range(5, 0, -1):
                    time.sleep(1)
                    progress.update(task, advance=1)
            pass
        elif user_input == '2':
            # 执行选择模式
            plant_name = "默认卡组"
            while True:
                console.clear()
                console.print(f"你选择的植物卡组是：[bold cyan]{plant_name}[/bold cyan]")
                print_mode_menu_title()
                print_mode_menu_options()
                    
                mode_input = Prompt.ask("请选择模式：", choices=["1", "2", "3", "4", "5", "0"], default="1")

                if mode_input == '1':
                    # 执行冒险模式
                    mode_name = "冒险模式"
                elif mode_input == '2':
                    # 执行小游戏模式
                    mode_name = "小游戏模式"
                elif mode_input == '3':
                    # 执行解谜模式
                    mode_name = "解谜模式"
                elif mode_input == '4':
                    # 执行生存模式
                    mode_name = "生存模式"
                elif mode_input == '5':
                    # 执行随机模式
                    mode_name = "随机模式"
                elif mode_input == '0':
                    # 返回上级菜单
                    break
                console.clear()
                console.print(f"你选择的模式是：[bold cyan]{mode_name}[/bold cyan]")
                console.print(f"你选择的卡组是：[bold cyan]{plant_name}[/bold cyan]")
                console.print("正在启动游戏与修改器，请稍后...", style="bold cyan")
                with Progress() as progress:
                    task = progress.add_task("[cyan]启动中...", total=5)
                    for i in range(5, 0, -1):
                        console.print(f"[bold red]{i}", end="\r")
                        time.sleep(1)
                        progress.update(task, advance=1)
                print_game_running_screen()
                keyboard.wait('ctrl+0')
                break
        elif user_input == '3':
            # 执行选择植物卡组
            mode_name = "默认关卡"
            while True:
                console.clear()
                console.print(f"你选择的关卡是：[bold cyan]{mode_name}[/bold cyan]")
                print_plant_menu_title()
                print_plant_menu_options()
                    
                plant_input = Prompt.ask("请选择卡组：", choices=["1", "2", "3", "4", "5", "6", "0"], default="1")

                if plant_input == '1':
                    # 执行4个模仿者卡组
                    plant_name = "4个模仿者卡组"
                elif plant_input == '2':
                    # 执行3个模仿者卡组
                    plant_name = "3个模仿者卡组"
                elif plant_input == '3':
                    # 执行全模仿者卡组
                    plant_name = "全模仿者卡组"
                elif plant_input == '4':
                    # 执行卡组
                    plant_name = "卡组"
                elif plant_input == '5':
                    # 执行随机卡组
                    plant_name = "随机卡组"
                elif plant_input == '6':
                    # 执行自定义卡组
                    plant_name = "自定义卡组"
                elif plant_input == '0':
                    # 返回上级菜单
                    break         
                console.clear()
                console.print(f"你选择的模式是：[bold cyan]{mode_name}[/bold cyan]")
                console.print(f"你选择的卡组是：[bold cyan]{plant_name}[/bold cyan]")
                console.print("正在启动游戏与修改器，请稍后...", style="bold cyan")
                with Progress() as progress:
                    task = progress.add_task("[cyan]启动中...", total=5)
                    for i in range(5, 0, -1):
                        console.print(f"[bold red]{i}", end="\r")
                        time.sleep(1)
                        progress.update(task, advance=1)
                print_game_running_screen()
                keyboard.wait('ctrl+0')
                break
        elif user_input == '4':
            # 执行全自定义游戏
            while True:
                console.clear()
                print_mode_menu_title()
                print_mode_menu_options()
                    
                mode_input = Prompt.ask("请选择模式：", choices=["1", "2", "3", "4", "5", "0"], default="1")

                if mode_input == '1':
                    # 执行冒险模式
                    mode_name = "冒险模式"
                elif mode_input == '2':
                    # 执行小游戏模式
                    mode_name = "小游戏模式"
                elif mode_input == '3':
                    # 执行解谜模式
                    mode_name = "解谜模式"
                elif mode_input == '4':
                    # 执行生存模式
                    mode_name = "生存模式"
                elif mode_input == '5':
                    # 执行随机模式
                    mode_name = "随机模式"
                elif mode_input == '0':
                    # 返回上级菜单
                    break

                console.clear()
                console.print(f"你选择的模式是：[bold cyan]{mode_name}[/bold cyan]")
                print_plant_menu_title()
                print_plant_menu_options()
                    
                plant_input = Prompt.ask("请选择卡组：", choices=["1", "2", "3", "4", "5", "6", "0"], default="1")

                if plant_input == '1':
                    # 执行4个模仿者卡组
                    plant_name = "4个模仿者卡组"
                elif plant_input == '2':
                    # 执行3个模仿者卡组
                    plant_name = "3个模仿者卡组"
                elif plant_input == '3':
                    # 执行全模仿者卡组
                    plant_name = "全模仿者卡组"
                elif plant_input == '4':
                    # 执行卡组
                    plant_name = "卡组"
                elif plant_input == '5':
                    # 执行随机卡组
                    plant_name = "随机卡组"
                elif plant_input == '6':
                    # 执行自定义卡组
                    plant_name = "自定义卡组"
                elif plant_input == '0':
                    # 返回上级菜单
                    break

                console.clear()
                console.print(f"你选择的模式是：[bold cyan]{mode_name}[/bold cyan]")
                console.print(f"你选择的卡组是：[bold cyan]{plant_name}[/bold cyan]")
                console.print("正在启动游戏与修改器，请稍后...", style="bold cyan")
                with Progress() as progress:
                    task = progress.add_task("[cyan]启动中...", total=5)
                    for i in range(5, 0, -1):
                        console.print(f"[bold red]{i}", end="\r")
                        time.sleep(1)
                        progress.update(task, advance=1)
                print_game_running_screen()
                keyboard.wait('ctrl+0')
                break
        elif user_input == '5':
            # 执行全随机游戏
            pass
        elif user_input == '0':
            # 退出脚本
            break