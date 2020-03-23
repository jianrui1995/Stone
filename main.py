# @Time: 2020/3/22 0:02
# @Author: R.Jian
# @Note: 主函数

from SuiChongS import *
from Tables import *
from Spell import *

if __name__ == "__main__":
    Hands = [HaiDao(True),HaiDao(True),MengJi(),XuanFengZhan()]
    MineTable = [KuangBaoZhe(False),CaoJiShiBin(False),LuLiZhu(True,False),LuLiZhu(True,False)]
    YoursTable = [DaRuan(False)]
    log = []
    table = Table(Hands,MineTable,YoursTable,log)
    while table:
        table = table.operate()

