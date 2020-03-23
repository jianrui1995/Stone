# @Time: 2020/3/22 14:31
# @Author: R.Jian
# @Note: 

from SuiChongS import *
from copy import deepcopy

if __name__ == "__main__":
    a = HaiDao(True)
    s_list = {1:a,2:a}
    a_list = deepcopy(s_list)
    a_list[1].ishand= False
    print(s_list[1])
    print(s_list[2])