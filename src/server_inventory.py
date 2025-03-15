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

def stat_countries():
    
    nb_servers_per_countries = {}
    files = loop_files()
    for file in files:
        country=str(file["tags"]["country"])
    
        if country not in nb_servers_per_countries.keys():
            nb_servers_per_countries[country]=1
        else:
            nb_servers_per_countries.update({country:nb_servers_per_countries[country]+1})
    return nb_servers_per_countries

def stat_roles():
    
    nb_servers_per_role = {}
    files = loop_files()
    for file in files:
        role=str(file["tags"]["role"])
    
        if role not in nb_servers_per_role.keys():
            nb_servers_per_role[role]=1
        else:
            nb_servers_per_role.update({role:nb_servers_per_role[role]+1})
    return nb_servers_per_role
    
def stat_all():
    
    app_dict = {}
    files = loop_files()
    for file in files:
        app=str(file["tags"]["app"])
        country=str(file["tags"]["country"])
        role=str(file["tags"]["role"])
    
        if app not in app_dict.keys():
            app_dict[app]= {
                "count":1,
                "country":{},
                "role":{}
                            }
        else:
            count = app_dict[app]["count"]
            country_dict=app_dict[app]["country"]
            role_dict=app_dict[app]["role"]
            
            if country not in country_dict.keys():
                country_dict[country]=1
            else:
                country_dict.update({country:country_dict[country]+1})
            
            if role not in role_dict.keys():
                role_dict[role]=1
            else:
                role_dict.update({role:role_dict[role]+1})
            
            app_dict[app]["count"]=count+1
            app_dict[app]["country"]=country_dict
            app_dict[app]["role"]=role_dict
            
            # app_dict.update({
            #     app["count"]:count,
            #     app["country"]:country_dict,
            #     app["role"]:role_dict
            #     })
    return app_dict
    


create_json_from_dict("stat_all.json",stat_all())
# stat_all()