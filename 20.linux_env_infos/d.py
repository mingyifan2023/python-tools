import platform
import psutil

# 获取系统信息
def get_system_info():
    print("***** 系统信息 *****")
    print(platform.uname())

# 获取内核版本
def get_kernel_version():
    print("\n***** 内核版本 *****")
    with open('/proc/version', 'r') as file:
        print(file.read())

# 获取CPU信息
def get_cpu_info():
    print("\n***** CPU 信息 *****")
    print(psutil.cpu_info())

# 获取内存信息
def get_memory_info():
    print("\n***** 内存信息 *****")
    print(psutil.virtual_memory())

# 获取硬盘信息
def get_disk_info():
    print("\n***** 硬盘信息 *****")
    print(psutil.disk_usage('/'))

# 获取网络信息
def get_network_info():
    print("\n***** 网络信息 *****")
    print(psutil.net_if_addrs())

# 调用各个函数来获取系统信息
get_system_info()
get_kernel_version()
get_cpu_info()
get_memory_info()
get_disk_info()
get_network_info()
