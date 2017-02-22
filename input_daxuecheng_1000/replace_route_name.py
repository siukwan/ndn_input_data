#coding:utf-8

import os 
import logging 
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element
osmName = 'daxuecheng.osm'
tree = ET.parse(osmName)  # 载入数据
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

f = open(osmName, 'r')
f_str = f.read()

for key, value in hash_dict.items():
    f_str = f_str.replace(key, value)
    #print key, value


f_w = file("target.osm", "w+")
f_w.write(f_str)
f_w.close()
sumo_path = 'F:/sumo-win32-0.24.0/sumo-0.24.0/'
os.popen(sumo_path + 'bin/netconvert --osm-files target.osm -o input_net.net.xml')
print sumo_path + 'bin/netconvert --osm-files target.osm -o input_net.net.xml'
print "OK"
