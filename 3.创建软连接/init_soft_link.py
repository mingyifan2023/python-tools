import os.path
import time

# os.path.islink(path)
# 判断路径是否为链接
#路径操作函数os.path.islink用于判断一个路径是否是软链，如果路径本身并不存在，则返回False。

# os.link(src, dst)
# 创建硬链接，名为参数 dst，指向参数 src。
# src：用于创建硬连接的源地址
# dst：用于创建硬连接的目标地址

# os.readlink(path)
# 返回软链接所指向的文件。
# path：要查找的软链接路径

# os.remove(path)
# 删除路径为 path 的文件。如果 path 是一个文件夹，将抛出 OSError; 查看下面的 rmdir() 删除一个 directory。
# path：要移除的文件路径

# os.removedirs(path)
# 递归删除目录。
# path：要移除的目录路径

# os.symlink(src, dst)
# 创建一个软链接。
# src：源地址
# dst：目标地址

# os.unlink(path)
# 删除文件路径。
# path：删除的文件路径


# 1. 检测软连接
# 2.创建软连接
# 3. 删除软连接

# 先用linux命令把软连接的创建删除完成
# 1. 创建  ln -s /home/main.log  /opt/main.log

src_path = "/home"
dst_path = "/opt"




# ok 
def init_soft_link(src_path,dst_path):
    soft_link_file = os.path.join(dst_path,"main.log")
    src_file = os.path.join(src_path,"main.log")
    if os.path.exists(soft_link_file):
        os.remove(soft_link_file)
        os.symlink(src_file,soft_link_file)
    else:
        os.symlink(src_file,soft_link_file)

init_soft_link(src_path,dst_path)







