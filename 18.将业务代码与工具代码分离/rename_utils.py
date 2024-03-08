# 用python读取一个当前文件夹中的所有文件和文件夹，如果是文件就不管；
# 如果是文件夹就进入文件夹中，读取文件，并将所有文件移动到python脚本所在的顶层目录中，
# 如果文件夹中又有文件夹，就继续按照上面的步骤进行同样的处理，
# 直到重新命名并移动所有文件位置，新命名的文件名为 文件夹1_文件夹2_所有文件名

import os
import shutil

def move_files_to_top_directory(folder_path, prefix='', current_script_path=''):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if item_path == current_script_path:  # 排除当前脚本所在的目录
            continue
        if os.path.isdir(item_path):
            new_prefix = f"{prefix}_{item}" if prefix else item
            move_files_to_top_directory(item_path, new_prefix, current_script_path)
            # os.rmdir(item_path)  # 删除空文件夹
        elif os.path.isfile(item_path):
            new_file_name = f"{prefix}_{item}" if prefix else item
            destination_file = os.path.join(os.path.dirname(folder_path), new_file_name)
            shutil.move(item_path, destination_file)

current_directory = os.getcwd()
current_script_path = os.path.abspath(__file__)  # 获取当前脚本文件路径
move_files_to_top_directory(current_directory, current_script_path=current_script_path)
