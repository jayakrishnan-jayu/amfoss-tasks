import subprocess
import requests
import json

user = 'snitch3s'

response = requests.get('https://api.github.com/users/'+user+'/repos')

commits = ""

for repo in response.json():
    print("searching inside "+ repo["name"])

    result = subprocess.run(['perceval', 'git', '--json-line','https://github.com/'+user+'/'+ repo['name']], stdout=subprocess.PIPE)

    output = result.stdout.decode('utf-8')

    for data in output.split("\n")[:-1]:

        json_data = json.loads(data)
        commits += str(json_data) + ','

        print(json_data['data']['message'])


with open("commits.json", "w") as myFile:
    myFile.write(commits[:-1])