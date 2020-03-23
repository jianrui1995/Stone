# @Time: 2020/3/21 23:30
# @Author: R.Jian
# @Note: 桌面类

from copy import  deepcopy
from SuiChongS import *
from Spell import *
class Table():
    def __init__(self,hands,minetable,yourstable,log):
        self.info={"H":hands,"M":minetable,"Y":yourstable,"L":log,"O":[]}
        self.forward = None
        self.operate_label = 0
        self.mengji_target = 0
        self.creat_operations()
        self.creat_T()

    def creat_T(self):
        self.info["T"] = self.info["M"]+self.info["Y"]

    def creat_operations(self):
        "生成操作列表"
        for obj in self.info["H"]:
            if isinstance(obj,SuiChongBase):
                "是随从牌"
                if len(self.info["M"])<7:
                    self.info["O"].append(obj)
            else:
                "是法术牌"
                self.info["O"].append(obj)
        for obj in self.info["M"]:
            if len(self.info["Y"])>0:
                if not obj.isattached:
                    self.info["O"].append(obj)

    def operate(self):
        new_info = deepcopy(self.info)
        # print(new_info)
        if self.operate_label < len(new_info["O"]) and (len(new_info["Y"])>0 or len(new_info["H"])>0):
            op = new_info["O"][self.operate_label]
            if isinstance(op,SuiChongBase):
                self.operate_label = self.operate_label+1
                if op.ishand:
                    "在手上"
                    new_info["H"].remove(op)
                    new_info["M"].append(op)
                    op.ishand = False
                    new_info["L"].append(op.__str__()+"出牌-->")
                    newtable = Table(new_info["H"],new_info["M"],new_info["Y"],new_info["L"])
                    newtable.forward = self
                    return newtable
                else:
                    new_info["L"].append(op.__str__() + "攻击-->")
                    "不在手上,就是要攻击"
                    resultA = op.be_attached(new_info["Y"][0].attach)
                    "如果狂暴者在"
                    self.isKuangBaoZhe(new_info["M"])

                    resultB = new_info["Y"][0].be_attached(op.attach)
                    "如果狂暴者在"
                    self.isKuangBaoZhe(new_info["M"])
                    op.isattached = True
                    "resultA,自己随从"
                    if resultA[0] ==0:
                        "死掉了"
                        if len(resultA)==2:
                            "添加"
                            new_info["M"] = self.append(new_info["M"],resultA[-1:])
                            new_info["M"].remove(op)
                        else:
                            new_info["M"].remove(op)
                    if resultA[0] == 1:
                        "没有死"
                        if len(resultA)==2:
                            "添加"
                            new_info["M"] = self.append(new_info["M"],resultA[-1:])

                    "resultB,对方随从"
                    if resultB[0] ==0:
                        "死掉了"
                        if len(resultB)==2:
                            "添加"
                            new_info["Y"] = self.append(new_info["Y"], resultB[-1:])
                            new_info["Y"].remove(new_info["Y"][0])
                        else:
                            new_info["Y"].remove(new_info["Y"][0])
                    if resultB[0] == 1:
                        "没有死"
                        if len(resultB)==2:
                            "添加"
                            new_info["Y"] = self.append(new_info["Y"],resultB[-1:])
                    newtable = Table(new_info["H"],new_info["M"],new_info["Y"],new_info["L"])
                    newtable.forward = self
                    return newtable
            if isinstance(op,MengJi):
                if self.mengji_target==len(new_info["T"])-1:
                    self.operate_label = self.operate_label+1
                new_info["H"].remove(op)
                result = op(new_info["T"][self.mengji_target])
                new_info["L"].append("猛击"+new_info["T"][self.mengji_target].__str__()+"-->")
                if new_info["T"][self.mengji_target] in new_info["M"]:
                    "目标在我的桌面"
                    self.isKuangBaoZhe(new_info["M"])
                    if result[0] ==0:
                        "死掉了"
                        if len(result)==2:
                            "添加"
                            new_info["M"] = self.append(new_info["M"],result[-1:])
                            new_info["M"].remove(new_info["T"][self.mengji_target])
                        else:
                            new_info["M"].remove(new_info["T"][self.mengji_target])
                    if result[0] == 1:
                        "没有死"
                        if len(result)==2:
                            "添加"
                            new_info["M"] = self.append(new_info["M"],result[-1:])
                if new_info["T"][self.mengji_target] in new_info["Y"]:
                    "目标在对方桌面"
                    self.isKuangBaoZhe(new_info["Y"])
                    if result[0] ==0:
                        "死掉了"
                        if len(result)==2:
                            "添加"
                            new_info["Y"] = self.append(new_info["Y"], result[-1:])
                            new_info["Y"].remove(new_info["Y"][0])
                        else:
                            new_info["Y"].remove(new_info["Y"][0])
                    if result[0] == 1:
                        "没有死"
                        if len(result)==2:
                            "添加"
                            new_info["Y"] = self.append(new_info["Y"],result[-1:])
                newtable = Table(new_info["H"], new_info["M"], new_info["Y"], new_info["L"])
                newtable.forward = self
                self.mengji_target = self.mengji_target+1
                return newtable
            if isinstance(op,XuanFengZhan):
                self.operate_label = self.operate_label + 1
                results = op(new_info["M"],new_info["Y"],self.isKuangBaoZhe)
                self.append(new_info["M"],results[1])
                self.append(new_info["Y"],results[3])
                for obj in results[0]:
                    new_info["M"].remove(obj)
                for obj in results[2]:
                    new_info["Y"].remove(obj)
                new_info["H"].remove(op)
                new_info["L"].append("旋风斩-->")
                newtable = Table(new_info["H"], new_info["M"], new_info["Y"], new_info["L"])
                newtable.forward = self
                return newtable
        else:
            if not (len(new_info["Y"])>0 or len(new_info["H"])>0):
                # print(2)
                "计算斩杀线"
                sum = 0
                for obj in new_info["M"]:
                    if not obj.isattached:
                        sum = sum + obj.attach
                new_info["L"].append("斩杀线-"+str(sum))
                f = open("data2.txt","a+",encoding="utf8")
                print("".join(new_info["L"]),file=f)
                f.close()
                return self.forward
            else:
                # print(1)
                return self.forward
            # if self.operate_label >= len(new_info["O"]):
            #     print(1)
            #     return self.forward
            # elif len(new_info["Y"])>0:
            #     "失败"
            #     new_info["L"].append("失败")
            #     print("".join(new_info["L"]))
            #     return self.forward
            # else:
            #     print(2)
            #     "计算斩杀线"
            #     sum = 0
            #     for obj in new_info["M"]:
            #         if not obj.isattached:
            #             sum = sum + obj.attach
            #     new_info["L"].append("斩杀线-"+str(sum))
            #     f = open("data2.txt","a+",encoding="utf8")
            #     print("".join(new_info["L"]),file=f)
            #     f.close()
            #     return self.forward

    def append(self,list,objs):
        for obj in objs:
            if len(list)<7:
                list.append(obj)
            else:
                break
        return list

    def isKuangBaoZhe(self,M):
        for obj in M:
            if isinstance(obj,KuangBaoZhe):
                obj.inject()



