你可以使用Python中的集合（set）来找到三个列表中的共同元素。以下是一个示例代码：

python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

common_elements = set(list1) & set(list2) & set(list3)

print(list(common_elements))  # 输出 [5]
在这个示例中，我们首先将三个列表转换为集合（set），然后使用交集操作符&来找到这三个集合的共同元素。最后，将共同元素转换回列表形式并输出结果。
