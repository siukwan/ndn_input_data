#coding:utf-8

import os 
import logging 
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element
  
log = logging.getLogger("Core.Analysis.Processing") 

node_count = 2000
interval = 0.05
total_count = node_count * interval

sumo_path = 'F:/sumo-win32-0.24.0/sumo-0.24.0/'

node = dict()

while len(node) < node_count :
    print len(node)
    os.popen('python ' + sumo_path + '/tools/randomTrips.py -n input_net.net.xml -e ' + str(total_count) + ' -p ' + str(interval))
    os.popen(sumo_path + 'bin/duarouter.exe --trip-files=trips.trips.xml --net-file=input_net.net.xml --output-file=routes.rou.xml')
    tree = ET.parse('routes.rou.xml')  # 载入数据
    root = tree.getroot()  # 获取根节点
    for child in root:
        # print child.tag, child.attrib  # vehicle {'depart': '0.00', 'id': '0'}
        idx = int(child.attrib['id'])
        if idx in node:
            continue
        node[idx] = dict()
        for subchild in child:
            # print subchild.tag, subchild.attrib  # route {'edges': '29141670#0
            node[idx]['route_str'] = subchild.attrib['edges']
            node[idx]['route'] = subchild.attrib['edges'].split(' ')
            node[idx]['from'] = node[idx]['route'][0]
            node[idx]['to'] = node[idx]['route'][len(node[idx]['route']) - 1]

print len(node)
try:
    os.remove('trips.trips.xml')
except  WindowsError:
    pass

f = file("trips.trips.xml", "w+")
f.writelines('<?xml version="1.0"?>\n')
f.writelines('<trips>\n')

for i in range(0, len(node)):
    trip_str = '    <trip id="' + str(i) + '" depart="' + str(i * interval) + '" from="' + node[i]['from'] + '" to="' + node[i]['to'] + '" />\n'
    f.writelines(trip_str)

f.writelines('</trips>\n')
f.close()

os.popen(sumo_path + 'bin/duarouter.exe --trip-files=trips.trips.xml --net-file=input_net.net.xml --output-file=routes.rou.xml')
os.popen(sumo_path + 'bin/sumo -c cfg.sumocfg --fcd-output fcdoutput.xml')


print 'OK'