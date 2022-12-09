from OSLogManagement import os_log_parameters

# +1 cube. Questions:  To get the flag, start the above exercise, then use cURL to download the file returned by '/download.php' in the server shown above.

target_ip = input('Paste the Target ip: ') # Example: 46.101.22.232:30201

# Searches for a flag in the contents of the file on the remote server using a specified regular expression
# Returns the result as a list                                                                                                    
flag = os_log_parameters(f'curl {target_ip}/download.php', regex_function='search', regex_parameters='HTB{[a-zA-Z0-9_$!@]+}')

# Convert list to string
flag = ''.join(flag)
print(flag)
