interface {{ interface }}
ip access-group 1 in
{% for host in disallow_ip %}
access-list 1 deny host {{ host }}
{% endfor %}
{% for host in allow_ip %}
access-list 1 permit host {{ host }}
{% endfor %}

{% for cmd in params.commands %}
{% set command_name, interface, vlan_id = cmd.values() %}
access-list 1 deny host {{ command_name }} {{ interface }} {{ vlan_id }}
{% endfor %}

直接就用set来处理即可，因为也都有if判断的就先这么处理吧
在jinja2中还是不能直接使用map和lambda来处理字典的值

就先这样吧
