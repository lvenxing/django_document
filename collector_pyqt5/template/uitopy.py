import sys
import os


f_list = os.listdir(sys.path[0]) #获取当前目录
path = sys.executable #获取python安装目录
# 找bin文件
for i in f_list:
    if os.path.splitext(i)[1] == '.ui':
        os.system("%s -m PyQt5.uic.pyuic %s -o %s.py" % (path,i,os.path.splitext(i)[0]))