# ndn_input_data

1.在ndn的运行程序中，需要把input文件夹放置到根目录 /home/xxxxx/

2.下载数据集后，需要把名字改为input，放到用户根目录

git clone git@github.com:siukwan/ndn_input_data

cp -rf ndn_input_data/input_556 input

数据集说明：

input_556:556辆车的数据集

input_eason:eason的53辆车的数据集


##生成命令：

###//osm文件转换成net.xml
H:\sumo-0.23.0\bin\netconvert --osm-files map.osm.xml -o map.net.xml

###生成仿真轨迹信息
D:\sumo-0.23.0\bin\sumo -c cfg.sumocfg --fcd-output fcdoutput.xml  
###运行
D:\sumo-0.23.0\bin\sumo-gui.exe cfg.sumocfg 
###生成仿真轨迹信息
D:\sumo-0.23.0\bin\sumo -c cfg.sumocfg --fcd-output fcdoutput.xml --no-internal-links=true 