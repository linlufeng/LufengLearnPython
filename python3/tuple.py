import json

data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据:", repr(json_str))
print("JSON 对象 :", json_str)

data2 = json.loads(json_str)
print("data2 =",data2)

with open('data.json', 'w') as file:
    json.dump(data, file)

with open('data.json', 'r') as file:
    obj = json.load(file)
    print("obj=",obj)

if file.closed:
    print('aaa')

array = ['lin', 'lu', 'feng']
with open('linlufeng.json', 'w') as file1:
    json.dump(array, file1)

lam  = {
    'linlufeng' : ['lin', 'lu', 'feng'],
    'linyeliang' : ['lin', 'ye', 'liang'],
    'pengying' : ['peng', 'ying']
}
with open('lam.json', 'w') as file2:
    json.dump(lam, file2)