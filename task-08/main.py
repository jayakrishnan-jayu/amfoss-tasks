import subprocess
import requests
import json

user = 'snitch3s'
#user = 'opendistro-for-elasticsearch'
url = 'https://api.github.com/users/'+user+'/repos'
hasNext = True
counter = 0
while (hasNext):

    response = requests.get(url)

    try:
        head = response.headers['link']
        if ('rel="prev"' in head.split(";")[1]):
            hasNext = False
        else:
            url = head.split(";")[0][1:-1]
    except KeyError:
        print("No other pages found")
        hasNext = False
    finally:
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