import server_inventory

def incoming():
    
    files = server_inventory.loop_files()
    
    incoming={}
    
    for file in files:
        
        name = file["name"]
        
        for port,servers in file["outgoing"].items():
            for server in servers:
                if server not in incoming.keys():
                    incoming[server]= {name:[port]}
                elif name not in incoming[server]:
                    incoming[server][name]=[port]
                elif port not in incoming[server][name]:
                    incoming[server][name].append(port)
    return incoming

server_inventory.create_json_from_dict("incoming.json",incoming())
    
# incoming()