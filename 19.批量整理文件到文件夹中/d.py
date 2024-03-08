import os
import shutil

# 获取当前目录下除了本脚本文件之外的所有文件列表
file_list = [f for f in os.listdir() if os.path.isfile(f) and f != os.path.basename(__file__)]

# 创建文件夹并移动文件
for i, chunk in enumerate([file_list[i:i+5] for i in range(0, len(file_list), 5)], start=1):
    folder_name = str(i)
    os.makedirs(folder_name, exist_ok=True)
    for file in chunk:
        shutil.move(file, os.path.join(folder_name, file))

print("文件整理完成")
