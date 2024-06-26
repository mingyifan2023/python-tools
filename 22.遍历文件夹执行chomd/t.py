import os

def set_permissions(directory):
    # 设置当前文件夹权限
    os.chmod(directory, 0o777)

    # 遍历文件夹中的所有文件并设置权限
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            os.chmod(os.path.join(root, d), 0o777)
        for f in files:
            os.chmod(os.path.join(root, f), 0o777)

# 获取当前工作目录
directory = os.getcwd()

# 调用函数设置权限
set_permissions(directory)
