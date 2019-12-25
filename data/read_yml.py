import yaml
# 打开yaml文件
# with open("./value2.yml","r",encoding="utf8")as f:
#     data =yaml.safe_load(f)
#
#     print(data)
    # print(type(data.get("value0")))
    # print(type(data.get("value18")))

# 写入yaml文件
data ={"name":
           {"tj":"TJ"}}



with open("./value3.yml","w",encoding="utf8") as f:
    yaml.safe_dump(data,f,encoding="utf8",allow_unicode=True)
