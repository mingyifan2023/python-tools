interface {{ interface }}
ip access-group 1 in
{% for host in disallow_ip %}
access-list 1 deny host {{ host }}
{% endfor %}
{% for host in allow_ip %}
access-list 1 permit host {{ host }}
{% endfor %}
