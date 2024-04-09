def get_file_name(file_path):
    if '/' in file_path:
        # 对于Linux系统路径，使用"/"进行分割取最后一个元素作为文件名
        return file_path.split('/')[-1]
    elif '\\' in file_path:
        # 对于Windows系统路径，使用"\\"进行分割取最后一个元素作为文件名
        return file_path.split('\\')[-1]
    else:
        # 如果既不包含"/"也不包含"\"，则直接返回原始文件路径
        return file_path
