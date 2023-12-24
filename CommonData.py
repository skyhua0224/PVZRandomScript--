class Tool:
    name = '植物大战僵尸全版本辅助工具'
    path = r"C:\Users\XuanMeng\Desktop\plants\PvZ_Toolkit_v1.20.3\PvZ_Toolkit_v1.20.3.exe"
    hwnd = None
    left, top, right, bottom = None,None,None,None
    def ClearData():
        hwnd = None
        left, top, right, bottom = None,None,None,None

class Game:
    name = '植物大战僵尸中文版'
    path = r"C:\Users\XuanMeng\Desktop\plants\随机版各种版本\只有模仿者能随机的随机模仿者\模仿者随机版\PlantsVsZombies.exe"
    hwnd = None
    def ClearData():
        hwnd = None
    gameMode = ["冒险模式","小游戏模式","解密模式","生存模式"]

