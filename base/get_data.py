import os,yaml
class GetData():
    def get_yaml(self,filename):
        with open("./data" + os.sep + filename, "r", encoding="utf8")as f:
           return yaml.safe_load(f)
