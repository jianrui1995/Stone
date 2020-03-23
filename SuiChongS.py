# @Time: 2020/3/21 23:29
# @Author: R.Jian
# @Note: 随从类

class SuiChongBase():
    def __init__(self,attach,blood,ishand):
        self.attach = attach
        self.blood = blood
        self.isattached = False
        self.ishand = ishand

    def be_attached(self,attach):
        self.blood = self.blood-attach
        if self.blood<1 :
            return [0]
        else:
            "没有死"
            return [1]

class HaiDao(SuiChongBase):
    "海盗"
    def __init__(self,ishand):
        super(HaiDao,self).__init__(3,3,ishand)
    def __str__(self):
        return "HaiDao"

class KuangBaoZhe(SuiChongBase):
    "狂暴者"
    def __init__(self,ishand):
        super(KuangBaoZhe,self).__init__(2,4,ishand)

    def inject(self):
        self.attach = self.attach + 1

    def __str__(self):
        return "KuangBaoZhe"

class CaoJiShiBin(SuiChongBase):
    "超级士兵"
    def __init__(self,ishand):
        super(CaoJiShiBin,self).__init__(2,3,ishand)
        self.isattached = True

    def __str__(self):
        return "CaoJiShiBin"

class LuLiZhu(SuiChongBase):
    "奴隶主"
    def __init__(self,isreste,ishand):
        super(LuLiZhu,self).__init__(3,3,ishand)
        if isreste:
            self.blood = 2

    def be_attached(self,attach):
        self.blood = self.blood-attach
        if self.blood<1 :
            return [0]
        else:
            "没有死"
            return [1,LuLiZhu(False,False)]

    def __str__(self):
        return "LuLiZhu"

class XiaoRuan(SuiChongBase):
    def __init__(self,ishand):
        super(XiaoRuan, self).__init__(1, 2,ishand)

    def __str__(self):
        return "XiaoRuan"

class DaRuan(SuiChongBase):
    def __init__(self,ishand):
        super(DaRuan,self).__init__(3,5,ishand)

    def be_attached(self,attach):
        self.blood = self.blood-attach
        if self.blood<1 :
            return [0,XiaoRuan(False)]
        else:
            "没有死"
            return [1]

    def __str__(self):
        return "DaRuan"