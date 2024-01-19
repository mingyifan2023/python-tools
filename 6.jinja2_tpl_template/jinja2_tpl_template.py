

from jinja2 import Environment, FileSystemLoader

param_dict = {
    "params": {
        "commands": [
            {
                "command_name": "system_license_delete",
                "interface": "111",
                "vlan_id": "222",

            },
        ]
    }
}

def reset_info(param_dict, key_list):
    return [param_dict[key] for key in key_list]




loader = FileSystemLoader('templates')
environment = Environment(loader=loader)
environment.filters['reset_info'] = reset_info

tpl = environment.get_template('acl.conf.tpl')

out = tpl.render(param_dict)
print(out)
