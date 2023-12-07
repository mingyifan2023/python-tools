如果您想通过指定类中的函数名来直接引用类中的函数，可以使用getattr()函数来实现。

以下是一个示例：

python
class MyClass:
    def function1(self):
        print("This is function 1")

    def function2(self):
        print("This is function 2")

    def function3(self):
        print("This is function 3")
        
    def function4(self):
        print("This is function 4")

    def execute_function(self, function_name):
        func = getattr(self, function_name, None)
        if func is not None and callable(func):
            func()
        else:
            print("Invalid function name")

my_obj = MyClass()

# 通过指定函数名来执行相应的函数
my_obj.execute_function("function1")
my_obj.execute_function("function3")
在上述示例中，我们添加了一个名为 execute_function 的新方法。该方法接收一个 function_name 参数，通过调用 getattr() 函数并传递类实例和函数名，获取对应的函数对象。然后，我们进行检查以确保找到的函数对象是可调用的，并调用该函数；否则输出无效函数名的消息。

通过调用 execute_function 方法并传递所需的函数名，就能够根据指定的函数名直接引用并执行类中的函数。

请注意，在使用这种方式时，要确保传递的函数名是有效的类成员函数名称，并且与实际定义的函数名完全匹配。否则，可能会导致找不到函数或出现其他错误。
