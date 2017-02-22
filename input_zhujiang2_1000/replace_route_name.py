#coding:utf-8

import os 
import logging 
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'), ord('A')+6)]
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

tree = ET.parse('zhujiang.osm')  # 载入数据
root = tree.getroot()  # 获取根节点
hash_dict = dict()
hash_idx = 1
node_list = root.findall('way')
for child in node_list:
    # print child.tag, child.attrib
    id = child.attrib['id']
    hash_dict[id] = str(hash_idx)
    hash_idx += 1
    #print id
node_list = root.findall('node')
for child in node_list:
    # print child.tag, child.attrib
    id = child.attrib['id']
    hash_dict[id] = str(hash_idx)
    hash_idx += 1
    #print id

print len(hash_dict)

f = open('zhujiang.osm', 'r')
f_str = f.read()

for key, value in hash_dict.items():
    f_str = f_str.replace(key, value)
    #print key, value


f_w = file("target.osm", "w+")
f_w.write(f_str)
f_w.close()
print "OK"
