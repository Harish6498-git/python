def update_port(file_path, key, value):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            
            else:
                file.write(line)

server_config_file = 'server.conf'
key_to_update = 'PORT'
new_port_value = '5000'

update_port(server_config_file, key_to_update, new_port_value)