# Code questions: 7, 8, 12, 14, 17, 20, 23, 26, 29, 30   
#---

# code question 7
def format_rgb(rgb):
    # Write your code here.
    formatted = f"rgb({','.join(map(str, rgb))})"
    return formatted

# You may alter the code below to test your solution or print help documentation.
# Only the format_rgb function will be graded for this assessment.

rgb_sample = [255, 165, 13]
#print(format_rgb(rgb_sample))
# help(help)
#---

# code question 8
def minutes_to_hours(minutes):
    # Write your code here.
    hours = minutes/60
    return hours

# You may alter the code below to test your solution or print help documentation.
# Only the minutes_to_hours function will be graded for this assessment.

mins = 60
#print(minutes_to_hours(mins))
# help(help)

#----

# code question 12 
def update_log_list(log_list):
   for log in log_list:
      if log.get("app") == "webserver":
         log["level"] = "ERROR"
      if log.get("app") == "database":
         log["timestamp"] = "2023-12-07T11:50:00"
   return log_list

log_sample = [
   {"app": "webserver", "level": "argh", "message": "Critical error", "timestamp": "2023-12-07T11:55:00"},
   {"app": "database", "level": "ERROR", "message": "Database connection lost", "timestamp": "me time"}]

#print(update_log_list(log_sample))
#---

# code question 14

# Write your code here.
def validate_id(ID: str):
    result = ""
    if len(ID) == 8 and ID[0:3].isalpha() and ID[0:3].isupper() and ID[3:8].isdigit():
        return bool(1)
    else:
        return bool(0)

# You may alter the code below to test your solution or print help documentation.
# Only the validate_id function will be graded for this assessment.

#print(validate_id("jJ333333"))
# help(help)
#---

# code question 17
# A Python function same_subnetconverts IP addresses and subnet mask to binary strings in order to determine if two IPv4 addresses are in the same subnet, returning a string indicating whether both IP addresses are in the same subnet or not.
# 
# Complete the Python function same_subnet. The function should accept three strings representing two IP addresses and a subnet mask, determine if both IP addresses are in the same subnet, and return a predefined string statement indicating if both IP addresses are in the same subnet.
# 
# Only the same_subnet function will be graded for this assessment. The function should work for any IP addresses or subnet masks passed to same_subnet beyond the examples provided.
# 
# Example: If the two IP addresses and subnet mask are
# 
# '192.168.1.100', '192.168.1.200', '255.255.255.0'
# 
# the expected return is
# 
# 192.168.1.100 and 192.168.1.200 are in the same subnet
# 
# Example: If the two IP addresses and subnet mask are
# 
# '192.168.1.100', '192.168.2.200', '255.255.255.0'
# 
# the expected return is
# 
# 192.168.1.100 and 192.168.2.200 are not in the same subnet
#def same_subnet(ip1, ip2, subnet_mask):
#    # convert IP addresses to binary strings
#    ip1_bin = ''.join([format(int(x), '08b') for x in ip1.split('.')])
#    ip2_bin = ''.join([format(int(x), '08b') for x in ip2.split('.')])
#
#    # convert subnet mask to binary string
#    subnet_bin = ''.join([format(int(x), '08b') for x in subnet_mask.split('.')])
#
#    # get network address portion for both IP addresses
#    subnet_len = subnet_bin.count('1')
#    network1_bin = ip1_bin[:subnet_len]
#    network2_bin = ip2_bin[:subnet_len]
#
#    # Predefined statement indicating if IP addresses are in the same subnet
#    x = f"{ip1} and {ip2} are in the same subnet"
#    y = f"{ip1} and {ip2} are not in the same subnet"
#    
#    # Write a conditional expression to check if both IP addresses are in the same subnet
#    # and return the appropriate string output x or y.
#    # Write your code here.
#---

# code question 20

#A list of float values measuring the percentage of CPU usage for servers has been collected. Servers with CPU usage greater than 90% should be flagged.
#
#Complete the Python function identify_high_cpu. The function should accept a list of floats representing the percentage of CPU usage for servers, determine which servers have higher than 90% CPU usage, and return the list of high-usage servers by index value.
#
#Only the identify_high_cpu function will be graded for this assessment. The function should work for any list of floats passed to identify_high_cpu beyond the examples provided.
#
#Example: If the stored CPU percentages are
#
#[85.0, 92.5, 88.0, 95.2]
#
#the expected return is
#
#[1, 3]
#
#Example: If the stored CPU percentages are
#
#[91.0, 88.8, 89.5]
#
#the expected return is
#
#[0]

#def identify_high_cpu(cpu_list):
#    # Write your code here.
#    pass

# You may alter the code below to test your solution or print help documentation.
# Only the identify_high_cpu function will be graded for this assessment.

# cpu_list = [85.0, 92.5, 88.0, 95.2]
# print(identify_high_cpu(cpu_list))
# help(help)
#---

# code question 23

#An existing function line_count is meant to open a text file, read the contents, and return the number of lines in the file. Several existing issues throw errors, and the function is not working as intended.
#
#Update the code within the Python function line_count. The function should accept a string identifying the name of a text file, read the contents of the text file, determine the number of lines in the text file, and return the number of lines in the text file. For simplicity, assume each line except the last ends with a newline character.
#
#Only the line_count function will be graded for this assessment. The function should work for any text file passed to line_count beyond the examples provided.
#
#Example: If the text file "test.txt" contains
#
#Line 1
#Line 2
#Line 3
#
#the expected return is
#
#3
#Example: If the text file "lorem.txt" contains
#
#Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#Pellentesque tincidunt velit non iaculis porttitor.
#Phasellus mattis, metus non posuere mollis, eros augue dictum.
#Quisque porttitor est nec eros maximus, id sodales.
#
#the expected return is
#
#4
# Modify this function.
#def line_count(filename):
#    f = Open(filename) 
#    contents = f.read
#    lines = contents.split("\n")
#    f.close()
#    return len(line)

# You may alter the code below to test your solution or print help documentation.
# Only the line_count function will be graded for this assessment.

# print(line_count('test.txt'))
# help(help)
#---

# code question 26
#Complete the python function named write_dict_to_csv that appends predefined data to an existing file config.csv using the CSV library.
#
#Note:
#
#    There should be a newline after the last row of data per CSV library defaults.
#    Only the file output will be graded for this assessment, standard output will be ignored.
#    Print to check your work; what you print to stdout does not affect the assessment
#
#Here is an example of the usage:
#
#write_dict_to_csv('config.csv')
#
#Here is an example of what the config.csv should look like when written:
#
#device_name,ip_address
#Router1,192.168.1.1
#Router2,192.168.1.2
#import csv
#
#def write_dict_to_csv(filename):
#    # Data to be written to the CSV file
#    fieldnames = ['device_name', 'ip_address']
#
#    data = [
#        {'device_name': 'Router1', 'ip_address': '192.168.1.1'},
#        {'device_name': 'Router2', 'ip_address': '192.168.1.2'}
#    ]

    # Write the data to the CSV file.
    # Write your code here.
    
    # Print to check your work; what you print to stdout does not affect the assessment.
    # print('\n'.join([','.join(fieldnames)] + [','.join(str(d[field]) for field in fieldnames) for d in data]))
   

# You may alter the code below to test your solution or print help documentation.
# Only the write_dict_to_csv functions file output will be graded for this assessment.
# help(help)
    
# The assessment requires the below driver code in order for Zybooks to check file ouput.
# Do not edit code below this line.
#write_dict_to_csv('config.csv')
#---

# code question 29
#A database contains user data uploads with varying submission times. To process the latest information first, a function is needed to identify the most recent upload time.
#
#Complete the Python function find_latest. The function should accept an unordered list of user upload time strings, convert each string value into a datetime object using the provided date_format pattern, and return the most recent upload time as a datetime object.
#
#Only the find_latest function will be graded for this assessment. The function should work for any patterned strings passed from a list to find_latest beyond the examples provided.
#
#Example: If the stored user upload values are
#
#['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
#
#the expected return is
#
#2023-12-16 11:20:00
#
#Example: If the stored user upload values are
#
#['12/20/2023 02:00 AM', '12/18/2023 10:30 AM', '12/16/2023 07:45 PM', '12/14/2023 04:15 PM']
#
#the expected return is
#
#2023-12-20 02:00:00
#from datetime import datetime
#
#def find_latest(submissions):
#    # Specify a date format
#    date_format = '%m/%d/%Y %I:%M %p'
#        
#    # Convert string values into datetime objects.
#    
#    # Determine and return latest
#    pass

# You may alter the code below to test your solution or print help documentation.
# Only the find_latest function will be graded for this assessment.

# submission_timestamps = ['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
# print(find_latest(submission_timestamps))
# help(datetime.strptime)
#---

# code question 30
#A bug has been submitted for a Python function named scan_ports. The function is supposed to use the socket library to scan the loopback address and check if ports 0-x are open/closed and return a list of tuples with the port status. Correct the logical errors in the code.
#
#Here is an example of the usage:
#
# print(scan_ports(5))
#
#Here is an example of the expected output:
#
#[(0, 'OPEN'), (1, 'OPEN'), (2, 'OPEN'), (3, 'OPEN'), (4, 'OPEN'), (5, 'OPEN')]
#
#    The Zybooks coding environment lacks outside connectivity, code to mock the return value for socket.connect_ex has been provided to allow normal use of the socket library for the socket.connect_ex function only. socket.connect_ex should always return 0 for this assessment.
#import socket
#import time
#import unittest.mock as mock
#
#def scan_ports(x):
#    # Mock socket
#    with mock.patch('socket.socket') as mock_socket:
#        mock_socket.return_value.connect_ex.return_value = 0 # do not edit
#        target_IP = '127.0.0.1'
#
#        # Instantiate a socket object.
#        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        
#        # Set a timeout for the socket operations.
#        s.settimeout(5)  
#
#        # Create an empty list to store port status as a list tuples.
#        open_ports = []  
#
#        # Iterate over ports checking the connection and appending the port status to the list.
#        for i in range(0, x+1):
#            conn = s.connect_ex((target_IP, i))
#            if(conn == 0):
#                open_ports.extend(open_ports + [i, 'CLOSED'])
#            else:
#                open_ports.extend(open_ports + [i, 'OPEN'])
#
#        # Close the socket connection.
#        s.close()
#
#        # Return the list of open ports as a list of tuples.
#        return open_ports

# You may alter the code below to test your solution or print help documentation.
# Only the scan_ports function will be graded for this assessment.

# print(scan_ports(5))
# help(socket.socket)
# help(socket.socket.connect_ex)
