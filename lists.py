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

print("Before modify:", servers)
servers[-3] = 1234 # Inplace operation
print("After modification:", servers)

print("list of operation:", dir(servers))
"""
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
servers = ["172.10.12.1", "172.10.12.2", True, 123, 123.45, 123.456]
print("Before:", servers)
servers.append(False)
print("After:", servers)
servers.append(["a", "b"])
print("After append:", servers, len(servers))
# Multi indexing
# print(servers[-1][0])
servers.extend(["c", "d"])
print("After extend:", servers, len(servers))
print(servers.index(True))
servers.insert(0, 12)
print(servers)
servers.remove(True)
print(servers)
servers.reverse()
print(servers)
servers = servers[::-1]
print(servers)

servers = [1, 5, 8, 0, 3, 2, 6]
servers.sort()
print(servers)




