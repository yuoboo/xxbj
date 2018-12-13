# encoding=utf8
import platform


def get_sys():
    arch = platform.architecture()
    ma = platform.machine()  # 机器型号
    node = platform.node()  # 网络名称
    pro = platform.processor()  # 处理器
    py = platform.python_build()
    py_c = platform.python_compiler()
    py_v = platform.python_version()  # python版本\
    os_r = platform.release()  # 系统版本
    os_n = platform.system()  # 操作系统名称
    os_v = platform.version()  # 系统发布版本
    u = platform.uname()
    print locals()


get_sys()
