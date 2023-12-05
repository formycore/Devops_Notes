def update_server_config(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n") # as files are in lines
            else:
                file.write(line)
                
                
        
update_server_config("server_conf", "SSL_ENABLED", "False")