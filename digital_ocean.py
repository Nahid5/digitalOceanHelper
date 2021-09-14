#!/usr/bin/env python3
import requests
import json

#Enter DO token
DOTOKEN = ""
HEADERS = {"Authorization": "Bearer " + DOTOKEN, "Content-Type": "application/json"}

##################################################################################
#                               Droplets
#
##################################################################################
def get_current_droplet_count():
    '''
    Returns the number of droplets currently created and total drolet limit
    Return: [CURRENT DROPLET NUMBERS, MAX ACCOUNT CAN MAKE]
    '''
    r2 = requests.get("https://api.digitalocean.com/v2/account", headers=headers) 
    jsonData2 = json.loads(r2.text)
    return[str(jsonData["meta"]["total"]), str(jsonData2["account"]["volume_limit"])]


def get_all_droplets():
    '''
    '''
    r = requests.get("https://api.digitalocean.com/v2/droplets?page=1&per_page=1000", headers=HEADERS)
    jsonData = json.loads(r.text)
    # Get All Droplets and tags
    for droplet in jsonData["droplets"]:
        #print(droplet)
        print(str(droplet["id"]) + ": " +str(droplet["name"]) + " " + str(droplet["created_at"]) + " " + str(droplet["tags"]))

def delete_droplet_by_id(id):
    '''
    '''
    r = requests.delete("https://api.digitalocean.com/v2/droplets/" + id, headers=HEADERS)
    print(r.status_code)


##################################################################################
#                               Projects
#
##################################################################################
def get_all_projects():
    '''
    '''
    r = requests.get("https://api.digitalocean.com/v2/projects", headers=HEADERS)
    jsonData = json.loads(r.text)
    #rint(jsonData)
    for project in jsonData["projects"]:
        if(is_project_empty(project["id"])):
            #print(project["name"] + " is empty")
            delete_project_by_id(project["id"])

def is_project_empty(id):
    '''
    '''
    r = requests.get("https://api.digitalocean.com/v2/projects/" + id + "/resources", headers=HEADERS)
    jsonData = json.loads(r.text)
    #print(jsonData)
    if(jsonData["meta"]["total"] == 0):
        return True
    return False

def delete_project_by_id(id):
    '''
    '''
    r = requests.delete("https://api.digitalocean.com/v2/projects/" + id, headers=HEADERS)
    #jsonData = json.loads()
    #print(r.status_code)

if(__name__ == "__main__"):
    get_all_projects()