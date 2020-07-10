import json
# data = '{"var1":"deepak","var2":"20"}'
# print(data)
#
# parsed = json.loads(data)
# print(parsed['var1'])


data2 = {
    "cars": ['audi','bmw'],
    "compnay":['tata','jio']
}

jscomp  = json.dumps(data2)
print(jscomp)