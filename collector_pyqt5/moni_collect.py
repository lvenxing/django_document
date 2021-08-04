import logging  # 引入logging模块
import os.path
import time
import sys

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.join(os.path.dirname(os.getcwd()), "Logs")
# os.mkdir("Logs")
log_name = log_path + rq + '.log'
# log_name = os.path.join(log_path, "{}.log".format(rq))
logfile = log_name
print(logfile)



fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

sh = logging.StreamHandler(stream=sys.stdout)  # 往屏幕上输出
sh.setFormatter(formatter)  # 设置屏幕上显示的格式

fh.setFormatter(formatter)
# 第四步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(sh)
# 日志

def write_log():
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')
    print("------------------")

# write_log()