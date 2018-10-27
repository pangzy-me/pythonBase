print('----python logging module----')
'''
1.  logging模块日志级别：CRITICAL > ERROR > WARNING > INFO > DEBUG
2.  通过logging.basicConfig函数对日志的输出格式及方式做相关配置
3.  format参数：
        %(levelno)s：打印日志级别的数值
        %(levelname)s：打印日志级别的名称
        %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s：打印当前执行程序名
        %(funcName)s：打印日志的当前函数
        %(lineno)d：打印日志的当前行号
        %(asctime)s：打印日志的时间
        %(thread)d：打印线程ID
        %(threadName)s：打印线程名称
        %(process)d：打印进程ID
        %(message)s：打印日志信息

'''
# 1. 初步认识logging
# import logging,time
#
# logging.basicConfig(level=logging.DEBUG,
#                     # filename='log.txt',
#                     format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
#                     )   ## datefmt='%Y-%m-%d %H:%M:%S'
# logging.critical('第1优先级错误-critical信息.')
# logging.error('第2优先级错误-error信息')
# time.sleep(1)
# logging.warning('第3优先级错误-warning信息')
# logging.info('第4优先级错误-info信息')
# logging.debug('第5优先级错误-debug信息')

# 2. 将日志写入到文件和输出到屏幕
'''
1.Python 使用logging模块记录日志涉及四个主要类，使用官方文档中的概括最为合适：
    logger提供了应用程序可以直接使用的接口；
    handler将(logger创建的)日志记录发送到合适的目的输出；
    filter提供了细度设备来决定输出哪条日志记录；
    formatter决定日志记录的最终输出格式
2.具体步骤：
    a. 生成logger对象
    b. 生成handler 对象
    c. 生成formatter 对象
    d. 将formatter对象绑定到handler对象
    e. 把handler对象绑定到logger对象
3.logger级别优先级:logging.basicConfig < handler.setLevel < logger.setLevel
    a.脚本中没有配置logger.setLevel会使用handler.setLevel
    b.脚本中没有配置logger.setLevel和handler.setLevel会使用logging.basicConfig中的Level等级（默认WARNING）
4.logging有一个日志处理的主对象，其他处理方式都是通过addHandler添加进去，logging中包含的handler主要有如下几种：
    handler名称------位置------作用
    StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
    FileHandler：logging.FileHandler；日志输出到文件
    BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
    RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
    TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件
    SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
    DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
    SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址
    SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
    NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
    MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
    HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器
5.日志文件截取：按照文件大小截取/按照时间截取
    a.按照大小截取 logging.handlers.RotatingFileHandler()
        当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建一个新的同名日志文件继续输出。
        比如日志文件是chat.log。当chat.log达到指定的大小之后，RotatingFileHandler自动把文件改名为chat.log.1。
        此时，如果chat.log.1已经存在，会先把chat.log.1重命名为chat.log.2，最后重新创建 chat.log，继续输出日志信息。它的函数是：
        RotatingFileHandler( filename[, mode[, maxBytes[, backupCount]]]) 
            filename(文件名)
            mode(访问文件模式,r读,w写,a追加写)
            maxBytes用于指定日志文件的最大文件大小。maxBytes为0表示日志文件可以无限大
            backupCount用于指定保留的备份文件的个数。如指定为2，当上面描述的重命名过程发生时，原有的chat.log.2并不会被更名，而是被删除

    b.按照时间截取 logging.handlers.TimedRotatingFileHandler()
        间隔一定时间就自动创建新的日志文件。重命名的过程与RotatingFileHandler类似，不过新的文件不是附加数字，而是当前时间。它的函数是：
        TimedRotatingFileHandler( filename [,when [,interval [,backupCount]]])
            filename(文件名)
            backupCount用于指定保留的备份文件的个数。
            interval是时间间隔。
            when参数是一个字符串。表示时间间隔的单位，不区分大小写。
                取值：S秒 M分 H小时 D天 W每星期(interval==0时代表星期一) midnight每天凌晨
6.

'''
import logging,time
from logging import handlers

logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.CRITICAL)

# 其中模块日志级别只适用到WARNING级别，输出到文本和控制台
logtext = './logs/logtext.log'
file_handler = logging.FileHandler(logtext)
file_handler.setLevel(level=logging.WARNING)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# 日志文件截取
log_file_size = './logs/logsize.log'
log_file_time = './logs/logtime.log'
file_handler_size = logging.handlers.RotatingFileHandler(
    filename=log_file_size,maxBytes=100,backupCount=2)
file_handler_time = logging.handlers.TimedRotatingFileHandler(
    filename=log_file_time,when='S',interval=1,backupCount=5)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
file_handler_size.setFormatter(formatter)
file_handler_time.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(file_handler_size)
logger.addHandler(file_handler_time)

logger.critical("第1优先级错误-critical信息.")
time.sleep(1)
logger.error('第2优先级错误-error信息')
time.sleep(1)
logger.warning('第3优先级错误-warning信息')
logger.info('第4优先级错误-info信息')
logger.debug('第5优先级错误-debug信息')

# 捕获异常信息并写入到log文件中
try:
    open("try_open_file.txt","rb")
except(SystemExit,KeyboardInterrupt):
    raise
except Exception as e:
    logger.error('fail to open try_file.txt',exc_info=True)

