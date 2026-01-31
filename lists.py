server_1 = "172.10.12.1"
server_2 = "172.10.12.2" 

servers = ["172.10.12.1", "172.10.12.2", True, 123, 123.45, 123.456]
print(type(servers), servers, server_1, server_2)

# Python is zero index based
server_1 = servers[0]
print("server 1 IP address:", server_1)

# Slicing (Start_index:end_index +1step:size), as end_index in python is not inclusive 
simple_slice = servers[0:5:2]
print(simple_slice)