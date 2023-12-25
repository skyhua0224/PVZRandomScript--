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
                if user_input == '2':
                    print_title("请选择模式：")
                    print_options(list(mode_dict.values())[:-1])  # 不包括"默认关卡"
                    mode_input = Prompt.ask("请选择模式：", choices=list(mode_dict.keys())[:-1], default="1")  # 不包括"默认关卡"
                    mode_name = mode_dict[mode_input]
                    plant_name = "0"
                elif user_input == '3':
                    print_title("请选择植物卡组：")
                    print_options(list(plant_dict.values())[:-1])  # 不包括"默认卡组"
                    plant_input = Prompt.ask("请选择卡组：", choices=list(plant_dict.keys())[:-1], default="1")  # 不包括"默认卡组"
                    plant_name = plant_dict[plant_input]
                    mode_name = "0"
                elif user_input == '4':
                    print_title("请选择模式：")
                    print_options(list(mode_dict.values())[:-1])  # 不包括"默认关卡"
                    mode_input = Prompt.ask("请选择模式：", choices=list(mode_dict.keys())[:-1], default="1")  # 不包括"默认关卡"
                    mode_name = mode_dict[mode_input]
                    print_title("请选择植物卡组：")
                    print_options(list(plant_dict.values())[:-1])  # 不包括"默认卡组"
                    plant_input = Prompt.ask("请选择卡组：", choices=list(plant_dict.keys())[:-1], default="1")  # 不包括"默认卡组"
                    plant_name = plant_dict[plant_input]
                if mode_name == '0' or plant_name == '0':
                    break
                start_game(mode_input, plant_input)
        elif user_input == '0':
            break