# encoding=utf8
import platform


def get_sys():
    arch = platform.architecture()
    ma = platform.machine()  # 机器型号
    node = platform.node()  # 网络名称
    pro = platform.processor()  # 处理器
    py = platform.python_build()
    py_c = platform.python_compiler()
    py_v = platform.python_version()  # python版本
    os_r = platform.release()  # 系统版本
    os_n = platform.system()  # 操作系统名称
    os_v = platform.version()  # 系统发布版本
    u = platform.uname()
    print locals()


if __name__ == '__main__':

    get_sys()

    a = {'node': 'VM_0_13_centos',
     'py': ('default', 'Nov 15 2018 17:28:26'),
     'ma': 'x86_64',
     'os_n': 'Linux',
     'pro': 'x86_64',
     'py_c': 'GCC 4.8.5 20150623 (Red Hat 4.8.5-28)',
     'u': ('Linux', 'VM_0_13_centos', '3.10.0-514.26.2.el7.x86_64', '#1 SMP Tue Jul 4 15:04:05 UTC 2017', 'x86_64', 'x86_64'),
     'os_r': '3.10.0-514.26.2.el7.x86_64',
     'arch': ('64bit', 'ELF'),
     'os_v': '#1 SMP Tue Jul 4 15:04:05 UTC 2017',
     'py_v': '2.7.14'
     }

