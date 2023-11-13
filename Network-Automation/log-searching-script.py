#!/usr/bin/python

### This program is developed by:       ###
### S. Kishore Kumar                    ###
### ID: 202018bt019                     ###
### for Network Automation Project      ###

## This script developed for Log processing on remote server ###


import re

# Input log file name
log_file = '/var/log/remote.log'

# Output Jinja2 template file name
output_file = 'anm_output_template.j2'

# Regular expression to match IP addresses (IPv4 and IPv6)
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{1,4}\b'

# Pattern to search in log lines
search_pattern = r'%ETHPORT-5-IF_DOWN_ADMIN_DOWN:: \d+'

# Initialize a list to store extracted information
info_list = []

# Open the log file for reading
with open(log_file, 'r') as log:
    for line in log:
        # Find all IP addresses in the current line
        ip_addresses = re.findall(ip_pattern, line)
        
        # Search for the pattern in the log line
        match = re.search(search_pattern, line)
        
        if ip_addresses and match:
            # Extract information from the log line
            ip_info = {
                'ip_address': ip_addresses[0],
                'error_code': match.group()
            }
            info_list.append(ip_info)

# Open the Jinja2 template file for writing
with open(output_file, 'w') as template:
    # Write the Jinja2 template format
    template.write("This is a Jinja2 template generated from log messages:\n")
    template.write("{% for info in info_list %}\n")
    template.write("IP Address: {{ info.ip_address }}\n")
    template.write("Error Code: {{ info.error_code }}\n")
    template.write("{% endfor %}\n")

# Output the extracted information
print("Information collected from log messages:")
for info in info_list:
    print(f"IP Address: {info['ip_address']}, Error Code: {info['error_code']}")
