### This Program is developed by:       ###
### S. Kishore Kumar                    ###
### ID: 202018bt019                     ###
### for Network Automation Project      ###

## This program renders the configuration for predictive maintenance automation task ###

import jinja2

# Define the path to the Jinja2 template file
template_file = 'predictive-maint-device-template.j2'

# Define the output file where the rendered configuration will be saved
output_file = 'pred-maint-device-upgrade-config.cfg'

# Define the firmware upgrade parameters as a dictionary
firmware_params = {
    'bin_file': '7.0.3.I7.3.bin',
    'source_location': 'tftp://192.168.1.145/nxos/7.0.3.I7.3.bin',
    'destination_folder': 'bootflash:7.0.3.I7.3.bin',
    'md5_checksum_file': 'b5426867e49e2dec08491772e7b01f0c',
}

# Create a Jinja2 environment with the current directory
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))

# Load the Jinja2 template
template = env.get_template(template_file)

# Render the template with the firmware upgrade parameters
rendered_config = template.render(firmware_params)

# Write the rendered configuration to the output file
with open(output_file, 'w') as file:
    file.write(rendered_config)


# print(f"Firmware upgrade configuration has been rendered and saved to '{output_file}'.")


