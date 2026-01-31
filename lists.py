server_1 = "172.10.12.1"
server_2 = "172.10.12.2" 

servers = ["172.10.12.1", "172.10.12.2", True, 123, 123.45, 123.456]
print(type(servers), servers, server_1, server_2)

# Python is zero index based
server_1 = servers[0]
print("server 1 IP address:", server_1)

# Slicing (Start_index:end_index +1step_size), as end_index in python is not inclusive 
# step_size = 1 (default)
simple_slice = servers[1:5:2]
print(simple_slice)

number = [11, 12, 13, 14, 13, 17, 18, 20]
slice = number[1:8:2]
print(slice)

# Negative indexing
simple_slice= servers[-1:-4:-1]
print(simple_slice)

print("length of list:", len(simple_slice))