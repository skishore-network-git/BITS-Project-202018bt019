### This Program is developed by:       ###
### S. Kishore Kumar                    ###
### ID: 202018bt019                     ###
### for Network Automation Project      ###

## This program renders the configuration for the network optimisation automation ###


import jinja2

# Define the path to the Jinja2 template file
template_file = 'net-optimisation.j2'

# Define the path to the output text file
output_file = 'net-opti-config.cfg'


# Define your input parameters as a dictionary
for params in template_file

	input_params = {
    	'param1': 'value1',
    	'param2': 'value2',
    	'param3': 'value3',
    	# Add more parameters as needed
	}

# Create a Jinja2 environment with the current directory
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))

# Load the Jinja2 template
template = env.get_template(template_file)

# Render the template with the input parameters
rendered_config = template.render(input_params)

# Write the rendered configuration to the output file
with open(output_file, 'w') as file:
    file.write(net-opti-config.cfg)
