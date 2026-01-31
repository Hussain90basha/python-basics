server_1 = "172.10.12.1"
server_2 = "172.10.12.2" 

servers = ["172.10.12.1", "172.10.12.2", True, 123, 123.45]
print(type(servers), servers, server_1, server_2)

# Python is zero index based
server_1 = servers[0]
print("server 1 IP address:", server_1)
