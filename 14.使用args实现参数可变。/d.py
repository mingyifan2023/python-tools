   def common_item(self,list1,list2,list3):
        # 其实只需要得到nikkei中的的属于三个指数的共同成分股即可，其他的两个没有必要 其实可以不用知道
        # 你可以使用Python中的集合（set）来找到三个列表中的共同元素。以下是一个示例代码：

        common_elements = set(list1) & set(list2) & set(list3)
        return list(common_elements)

上面的函数参数是固定的，如何实现参数是可变的情况
如果你希望函数的参数是可变的，可以使用*args来接收不定数量的参数。以下是一个修改后的示例代码：

python
def common_item(self, *lists):
    # 使用集合的交集操作找到所有列表的共同元素
    common_elements = set(lists[0]).intersection(*lists)
    return list(common_elements)

# 示例调用
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

result = common_item(list1, list2, list3)
print(result)  # 输出 [5]
在这个修改后的示例中，函数common_item的参数现在是*lists，它可以接收不定数量的参数。在函数内部，我们使用set(lists[0]).intersection(*lists)来找到所有列表的共同元素。最后返回共同元素的列表形式。
