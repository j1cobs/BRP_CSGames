import os
import yaml
import json

in_path = ".\data_input\servers"
out_path = ".\data_output"


def loop_files():
    file_list=[]
    directory = os.fsencode(in_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        with open(in_path+"/"+filename, 'r') as file:
            current_file = yaml.safe_load(file)
        file_list.append(current_file)
    return file_list

def create_yaml_from_dict(output_filename,data):
    with open(out_path+"/"+output_filename, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
        
def create_json_from_dict(output_filename,data):
    with open(out_path+"/"+output_filename, 'w') as outfile:
        json.dump(data, outfile,indent=4)

def stat_apps():
    
    nb_servers_per_app = {}
    files = loop_files()
    for file in files:
        app=str(file["tags"]["app"])
    
        if app not in nb_servers_per_app.keys():
            nb_servers_per_app[app]=1
        else:
            nb_servers_per_app.update({app:nb_servers_per_app[app]+1})
    return nb_servers_per_app
    
create_json_from_dict("stat_apps.json",stat_apps())
print(stat_apps())
