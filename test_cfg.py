# encoding=utf-8

import ConfigParser


config = ConfigParser.ConfigParser()
config.read("test.cfg")
secs = config.sections()  # 返回所有的section块名
print secs

options = config.options(secs[0])   # 返回指定section块的配置项
opts = config.options('sectionB')
print options
print opts


item_a = config.items(secs[0])    # 返回指定的section的键值对
print item_a

keys_a = config.get(secs[0], options[2])   # 获取指定section、指定key的值， 获取到的值全部都为字符串
keys_b = config.getint(secs[0], options[2])  # getint/getfloat/getboolean 如果类型不对会抛出异常
print keys_a
print keys_a == 1
print keys_b == 1


# 写入配置文件：先设置再写入文件
config.set(secs[0], options[0], 'newval')
config.set(secs[0], options[1], 'newval1')
config.set(secs[0], options[3], 'newval3')
config.write(open("test.cfg", 'w'))

