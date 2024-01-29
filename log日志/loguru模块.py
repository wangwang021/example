from loguru import logger

# 输入到屏幕
logger.info('Hello, World!')
logger.warning('Hello, World!')
logger.error('Hello, World!')
logger.debug('Hello, World!')

# 保存到日志文件
logger.add('log日志/info.log', level='DEBUG')
logger.info('Hello, World!')
logger.warning('Hello, World!')
logger.error('Hello, World!')
logger.debug('Hello, World!')

#rotation 日志文件分隔
"""
add() 函数的 rotation 参数，可以实现按照固定时间创建新的日志文件，比如设置每天 0 点新创建一个 log 文件：
logger.add('runtime_{time}.log', rotation='00:00')

设置超过 500 MB 新创建一个 log 文件：
logger.add('runtime_{time}.log', rotation="500 MB")

设置每隔一个周新创建一个 log 文件：
logger.add('runtime_{time}.log', rotation='1 week')
"""
# retention 日志保留时间
'''
add() 函数的 retention 参数，可以设置日志的最长保留时间，比如设置日志文件最长保留 15 天：
logger.add('runtime_{time}.log', retention='15 days')

设置日志文件最多保留 10 个：
logger.add('runtime_{time}.log', retention=10)

也可以是一个 datetime.timedelta 对象，比如设置日志文件最多保留 5 个小时：
import datetime
from loguru import logger
logger.add('runtime_{time}.log', retention=datetime.timedelta(hours=5))
'''
# compression 日志压缩格式
'''
add() 函数的 compression 参数，可以配置日志文件的压缩格式，这样可以更加节省存储空间，比如设置使用 zip 文件格式保存：
logger.add('runtime_{time}.log', compression='zip')
其格式支持：gz、bz2、xz、lzma、tar、tar.gz、tar.bz2、tar.xz
'''
