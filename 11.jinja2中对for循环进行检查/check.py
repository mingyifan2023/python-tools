您可以使用 jinja2 的自定义过滤器来实现这个功能。首先，您需要在 Python 中编写一个函数，并将其注册为 jinja2 的自定义过滤器。以下是一个示例：

python
from jinja2 import Environment, BaseLoader

def process_items(items):
    if isinstance(items, list):
        return items
    elif isinstance(items, str):
        return [items]
    else:
        raise ValueError("Items must be a list or a string")

env = Environment(loader=BaseLoader())

# 注册自定义过滤器
env.filters['process_items'] = process_items

# 在模板中使用
template = env.from_string("{% for item in items | process_items %}{{ item }}{% endfor %}")

# 测试示例
output = template.render(items="example")
print(output)  # 输出：example
在上面的示例中，我们定义了 process_items 函数来处理输入，然后将其注册为 jinja2 的自定义过滤器。接下来，在模板中就可以使用这个过滤器来对 items 进行处理。




2024/2/7 18:21:54

那怎么知道process_items 是针对于item还是items?

2024/2/7 18:21:58

对于 jinja2 中的自定义过滤器，其实是作用于整个变量而不是其中的元素。在您的例子中，process_items 过滤器将作用于整个 items 变量，而不是其中的每个 item。过滤器是在变量被迭代之前应用的。

如果您想要对列表中的每个元素应用过滤器，您可以使用内置的过滤器来分别对每个元素进行处理，例如：

jinja
{% for item in items %}
    {{ item | process_item }}
{% endfor %}
在这里，process_item 将作用于每个 item，而不是整个 items 变量。
