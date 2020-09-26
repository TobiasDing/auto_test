import yaml

file = open('a.yml', encoding='utf-8')
res = yaml.load(file, Loader=yaml.FullLoader)
print(res)