# 示例包含重复字典的列表
original_list = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 3, "name": "Charlie"}
]

# 方法一：使用列表推导式和集合来剔除重复字典
unique_list = [dict(t) for t in {tuple(d.items()) for d in original_list}]

print(unique_list)




# 示例包含重复字典的列表
original_list = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 3, "name": "Charlie"}
]

# 方法二：使用列表推导式和字典来剔除重复字典
seen = set()
unique_list = [d for d in original_list if tuple(d.items()) not in seen and not seen.add(tuple(d.items()))]

print(unique_list)
