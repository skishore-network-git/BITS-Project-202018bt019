### This Program is developed by:       ###
### S. Kishore Kumar                    ###
### ID: 202018bt019                     ###
### for Network Automation Project      ###

## This program renders the configuration for the capacity addition automation ###


import jinja2

# Define the path to the Jinja2 template file
template_file = 'capacity-addition-device-template.j2'

# Define the output file where the rendered configuration will be saved
output_file = 'capacity-addition-device-config'

# Define the switch-specific parameters as a dictionary
switch_params = {
    'hostname': 'Sw1',
    'interface': 'GigabitEthernet1/0/1',
    'description': 'Connected to ServerFarm',
    'vlan_id': 100,
    'ip_address': '192.168.1.225',
    # Add more parameters as needed
}

# Create a Jinja2 environment with the current directory
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))

# Load the Jinja2 template
template = env.get_template(template_file)

# Render the template with the switch parameters
rendered_config = template.render(switch_params)

# Write the rendered configuration to the output file
with open(output_file, 'w') as file:
    file.write(rendered_config)

# print(f"Switch configuration has been rendered and saved to '{output_file}'.")