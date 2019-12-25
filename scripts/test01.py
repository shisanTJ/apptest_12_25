import pytest,os,sys
sys.path.append(os.getcwd())
from base.get_data import GetData

def get_data():
    sum_list =[]
    # with open("./data"+os.sep+"value3.yml","r",encoding="utf8")as f:
    #     yaml.safe_load(f)
    data =GetData().get_yaml("sum.yml")
    for i in data.values():
        sum_list.append(tuple(i.values()))

    return sum_list

class Testsum:   #在控制台运行
    @pytest.mark.parametrize("a,b,c",get_data())
    def test(self,a,b,c):
        print("加法运算:{}+{}={}".format(a,b,c))
        assert a+b==c