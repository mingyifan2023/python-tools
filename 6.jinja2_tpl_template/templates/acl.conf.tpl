{% for cmd in params.commands  %}
{% set command_name, interface, vlan_id = cmd|reset_info(["command_name", "interface", "vlan_id"]) %}
access-list 1 deny host {{ command_name }} {{ interface }} {{ vlan_id }}
{% endfor %}
