def get_server_ip(server_name):
    return server_config.get(server_name, {}).get('ip')

def get_server_status(server_name):
   return server_config.get(server_name, {}).get('status', 'server not found')          


server_config = {
    'server1': {'ip': '192.168.1.1', 'port': '8000', 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': '80', 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': '9000', 'status': 'active'}
}

server_name = 'server3'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")

ip_address = get_server_ip(server_name)
print(f"{server_name} ip: {ip_address}")