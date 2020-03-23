# @Time: 2020/3/22 17:02
# @Author: R.Jian
# @Note: 法术牌


class MengJi():
    def __init__(self):
        pass

    def __call__(self, obj):
        return obj.be_attached(2)

class XuanFengZhan():
    def __init__(self):
        pass

    def __call__(self,M,Y,fun):
        resultM0 = [] #死掉的
        resultM1 = [] #新增加的
        resultY0 = []
        resultY1 = []
        for obj in M:
            result = obj.be_attached(1)
            fun(M)
            if len(result)<2:
                if result[0] == 0:
                    resultM0.append(obj)
            else:
                resultM1.append(result[1])
        for obj in Y:
            result = obj.be_attached(1)
            fun(M)
            if len(result) < 2:
                if result[0] == 0:
                    resultY0.append(obj)
            else:
                resultY1.append(result[1])
        return resultM0,resultM1,resultY0,resultY1