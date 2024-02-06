from jinja2 import Template

# 定义模板字符串
template_string = """
<ul>
  {% for item in items %}
    {% if item.startswith('A') %}
      <li>{{ item }} starts with 'A'</li>
    {% else %}
      <li>{{ item }} does not start with 'A'</li>
    {% endif %}
  {% endfor %}
</ul>
"""

# 创建模板对象
template = Template(template_string)

# 定义数据
data = {
    "items": ["Apple", "Banana", "Orange"]
}

# 渲染模板并输出结果
output = template.render(**data)
print(output)




from jinja2 import Template

# 定义模板字符串
template_string = """
<ul>
  {% for item in [items] %}
    {% if item.startswith('A') %}
      <li>{{ item }} starts with 'A'</li>
    {% else %}
      <li>{{ item }} does not start with 'A'</li>
    {% endif %}
  {% endfor %}
</ul>
"""

# 创建模板对象
template = Template(template_string)

# 定义数据
data = {
    "items": "abc"
}

# 渲染模板并输出结果
output = template.render(**data)
print(output)
