#coding:utf-8

import os 

sumo_path = 'F:/sumo-win32-0.24.0/sumo-0.24.0/'
os.popen(sumo_path + 'bin/sumo -c cfg.sumocfg --fcd-output fcdoutput.xml')

