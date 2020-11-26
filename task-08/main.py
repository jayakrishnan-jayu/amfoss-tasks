import subprocess
import requests
import json

user = 'snitch3s'
#user = 'opendistro-for-elasticsearch'
url = 'https://api.github.com/users/'+user+'/repos'
page = 1
counter = 0
while (True):

    response = requests.get(url+'?page='+str(page))
    if not response.json():
        break
    page += 1
    commits = ""
        
    for repo in response.json():
        counter+=1
        print(counter , "searching inside "+ repo["name"])
            
        result = subprocess.run(['perceval', 'git', '--json-line','https://github.com/'+user+'/'+ repo['name']], stdout=subprocess.PIPE)

        output = result.stdout.decode('utf-8')

        for data in output.split("\n")[:-1]:

            json_data = json.loads(data)
            commits += str(json_data) + '\n'

            print(json_data['data']['message'])


    with open("commits.json", "w") as myFile:
        myFile.write(commits)