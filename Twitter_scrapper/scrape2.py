import json
import csv
from msilib.schema import Directory
from path import Path
import requests,shutil
import os
from os import path
from operator import itemgetter

def remove_duplicates(test_list):
    newlist=[]
    memo = set()
    k='text'
    for l in test_list:
        if l[k] not in memo:
            newlist.append(l)
            memo.add(l[k])
    return newlist

def remove_duplicates_all(test_list):
    res_list = []
    for i in range(len(test_list)):
        if test_list[i] not in test_list[i + 1:]:
            res_list.append(test_list[i])

    return res_list
def name_dir(directory):
    parent_dir="C:\StudyMaterials\Flipkart_GRID4.0\Flipkart-GRID-4.0"
    Path=path.join(parent_dir,directory)
    return Path
def write_json_file(dict,name):
    Dir=name_dir(name)
    if path.isfile(path.join(Dir,f"{name}.json")) is False:
        if not path.isdir(Dir):
            os.mkdir(Dir)
        json_object = json.dumps(dict, indent=3)
        with open (path.join(Dir,f"{name}.json"),"w") as file:
            file.write(json_object)
    else: 
        with open(path.join(Dir,f"{name}.json")) as fp:
            listObj = json.load(fp)
            for d in dict:
                listObj.append(d)
        listObj1=remove_duplicates_all(listObj)
        with open(f"{name}.json", 'w') as json_file:
            json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))

def download_img(url,file_name,name):
    res=requests.get(url,stream=True)
    if res.status_code==200:
        Dir=name_dir(name)
        if not path.isdir(Dir):
            os.mkdir(Dir)
        with open(os.path.join(Dir,file_name),'wb') as f:
            shutil.copyfileobj(res.raw,f)
        print('Image sucessfully Downloaded',file_name)
    else:
        print("image couldnt be retrieved")

def in_csv():
    # with open('hashtags.csv', 'w') as f:
    pass

def sort__(list_to_be_sorted,name):
    newlist = sorted(list_to_be_sorted, key=itemgetter(f'{name}'), reverse=True) 
    return newlist

def get_img_url(test_list):    
    img=[]
    for sub in test_list:
        if sub['IMAGE_URL']!="null":
            img_id={f"{sub['id']}":f"{sub['IMAGE_URL']}"}
            img.append(img_id)
    return img


   










