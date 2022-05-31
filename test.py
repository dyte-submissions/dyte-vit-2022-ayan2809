# import os
# import git
# import shutil
# import tempfile

# # Create temporary dir
# t = tempfile.mkdtemp()
# # Clone into temporary dir
# # gh repo clone dyte-in/react-sample-app
# # https://github.com/dyte-in/react-sample-app.git
# git.Repo.clone_from('stack@127.0.1.7:/home2/git/stack.git', t, branch='main', depth=1)
# # Copy desired file from temporary dir
# shutil.move(os.path.join(t, 'setup.py'), '.')
# # Remove temporary dir
# shutil.rmtree(t)


import requests
import base64
import json

finalJson={}

user = 'dyte-in'
repo_name = 'javascript-sample-app'
path_to_file = 'package.json'

json_url ='https://api.github.com/repos/'+user+'/'+repo_name+'/contents/package.json'

# json_url = constructURL(user,repo_name,path_to_file,json_url) #forms the correct URL
response = requests.get(json_url) #get data from json file located at specified URL 
print(response)
if response.status_code == requests.codes.ok:
    jsonResponse = response.json()  # the response is a JSON
    #the JSON is encoded in base 64, hence decode it
    content = base64.b64decode(jsonResponse['content'])
    #convert the byte stream to string
    jsonString = content.decode('utf-8')
    finalJson = json.loads(jsonString)
else:
    print('Content was not found.')

for key, value in finalJson.items():
    print("The key and value are ({}) = ({})".format(key, value))