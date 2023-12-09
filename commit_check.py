# from flask import requests
from github import Github
import json
import requests
from datetime import datetime
# setup owner name , access_token, and headers
owner='RohanU307'
access_token='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'
import requests
repo = 'CI-CD_adv_rohan'
r = requests.get('https://api.github.com/repos/RohanU307/CI-CD_adv_rohan/commits')
commit = r.json()[0]["commit"]
author=commit['author']
latestCommitTime=author['date']
latestCommitTime=latestCommitTime[:len(latestCommitTime)-1]
latestCommitTime=latestCommitTime.split('T')
latestCommitTime=latestCommitTime[0]+' '+latestCommitTime[1]
lastCommitTime=latestCommitTime
latestCommitTime_obj=datetime.strptime(latestCommitTime,'%Y-%m-%d %H:%M:%S')
lastCommitTime_obj=latestCommitTime_obj
newCommit=False
try:
    file = open('json-dump.json', 'r')
    json_object = json.load(file)
    lastCommitTime_obj=datetime.strptime(json_object["lastCommitTime"],'%Y-%m-%d %H:%M:%S')
    print(lastCommitTime_obj)
except:
    file=None
    # file = open('json-dump.json', 'w+')
    # lastCommitTime_obj=latestCommitTime_obj
    # data = { "lastCommitTime": latestCommitTime }
    # json.dump(data, file)
    print("The file doesn't exist")
# print(latestCommitTime_obj-lastCommitTime_obj)
if(latestCommitTime_obj>lastCommitTime_obj):
    print("There is a new commit")
    newCommit=True
    # data = { "lastCommitTime": latestCommitTime, "newCommit":newCommit}
else:
    if(not file):
        newCommit=True
    else:
        newCommit=False
        print("There is no new commit")
data = { "lastCommitTime": latestCommitTime, "newCommit":newCommit}
file = open('json-dump.json', 'w+')
json.dump(data, file)