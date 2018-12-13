# encoding=utf8

name = 'open.txt'
with open(name, 'wb') as f:
    f.writelines("this is test open"+'\n')
    f.writelines("this is test open2"+'\n')
    f.writelines("this is test open3"+'\n')
    f.writelines("this is test open4"+'\n')
    f.writelines("this is test open5"+'\n')
    f.writelines("this is test open6"+'\n')


with open(name, 'rb') as f:
    con = f.readlines()
print con

