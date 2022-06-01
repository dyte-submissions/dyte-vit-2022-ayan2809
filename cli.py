import argparse
import csv
import requests
import base64
import json
import os
import dotenv
from github import Github
dotenv.load_dotenv()
token = os.getenv("token")
# print(token)
def fetchURLDetails(user, repo_name, path_to_file):
    finalJson={}
    json_url = 'https://api.github.com/repos/'+user+'/'+repo_name+'/contents/'+path_to_file
    # print(json_url)
    response = requests.get(json_url)
    if response.status_code == requests.codes.ok:
        jsonResponse = response.json() 
        content = base64.b64decode(jsonResponse['content'])
        jsonString = content.decode('utf-8')
        finalJson = json.loads(jsonString)
    else:
        print('Content was not found.')
    return finalJson

def fetchFullJSON(user, repo_name, path_to_file):
    finalJson={}
    json_url = 'https://api.github.com/repos/'+user+'/'+repo_name+'/contents/'+path_to_file
    # print(json_url)
    response = requests.get(json_url)
    if response.status_code == requests.codes.ok:
        jsonResponse = response.json() 
        content = base64.b64decode(jsonResponse['content'])
        jsonString = content.decode('utf-8')
        finalJson = json.loads(jsonString)
    else:
        print('Content was not found.')
    return finalJson

def fetchSHAnumber(user, repo_name, path_to_file):
    json_url = 'https://api.github.com/repos/'+user+'/'+repo_name+'/contents/'+path_to_file
    # print(json_url)
    response = requests.get(json_url)
    if response.status_code == requests.codes.ok:
        jsonResponse = response.json()
    else:
        print('Content was not found.')
    return jsonResponse['sha']   

def getLibraryName(dependency):
    return dependency.split('@')[0]

def getLibraryVersion(dependency):
    return dependency.split('@')[1]

def makeCSVforDependencyCheck(repo_name, repo, version, version_satisfied):
    csv_file = open('output1.csv', 'a')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([repo_name, repo, version, version_satisfied])
    csv_file.close()

def makeCSVforDependencyUpdate(repo_name, repo, version, version_satisfied, updateLink):
    csv_file = open('output2.csv', 'a')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([repo_name, repo, version, version_satisfied, updateLink])
    csv_file.close()

def createPullRequest(user, repo_name, branch_name, base_branch_name, title, body):
    # url = 'https://api.github.com/repos/'+user+'/'+repo_name+'/pulls'
    url = "https://api.github.com/repos/"+user+"/"+repo_name+"/pulls"
    headers = {
        "Authorization" : "token {}".format(token),
        "Accept" : "application/vnd.github.v3+json"
    }
    data= {
        "title":"Amazing new feature",
        "body":"Please pull these awesome changes in!",
        "head":"dev",
        "base":"main"
        # "title" : "PullRequest-Using-GithubAPI",
        # "body" : "I have amazing new Features",
        # "head" : "pull-request",
        # "base" : "main"
    }
    # print(url)
    # headers = {'Authorization': 'token '+token}
    # data = {'title': title, 'body': body, 'head': branch_name, 'base': base_branch_name}
    response = requests.post(url, headers=headers, data=data)
    # print(response)
    if response.status_code == requests.codes.ok:
        print('Pull request created successfully.')
    else:
        print('Pull request creation failed.')

def versionCompare(v1, v2):
     
    arr1 = v1.split(".")
    arr2 = v2.split(".")
    n = len(arr1)
    m = len(arr2)
     

    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]
  

    if n>m:
      for i in range(m, n):
         arr2.append(0)
    elif m>n:
      for i in range(n, m):
         arr1.append(0)
  
    for i in range(len(arr1)):
      if arr1[i]>arr2[i]:
         return 1
      elif arr2[i]>arr1[i]:
         return -1
    return 0

# this function does not work and hence had to find a library which can do the same
def updateGitHubFile(user, repo_name, path_to_file, sha, content):
    url = 'https://api.github.com/repos/'+user+'/'+repo_name+'/contents/'+path_to_file
    # print(content, sha, token)
    # print(base64.urlsafe_b64encode(json.dumps(content).encode()).decode())
    headers = {
        "Authorization" : "token {}".format(token),
        "Accept" : "application/vnd.github.v3+json"
    }
    data = {
        "message":"a new commit message",
        "committer":
        {
            "name":"Ayan Sadhukhan",
            "email":"ayan.sadhukhan2019@vitstudent.ac.in"
        },
        "content": base64.urlsafe_b64encode(json.dumps(content).encode()).decode(),
        "sha": sha
    }
    # print(data)
    response = requests.put(url, headers=headers, data=data)
    # print(response.status_code)
    if response.status_code == requests.codes.ok:
        print('File updated successfully.')
    else:
        print('File update failed.')

def updateGitHubFile2(user, repo_name, path_to_file, shaPassed, content):
    g = Github(token)
    # print('--> Logged in')
    # Get User from the token used to login
    user = g.get_user()
    repo = g.get_repo(user.login+"/"+repo_name)
    contents = repo.get_contents(path_to_file)
    repo.update_file(contents.path, "Updated Package.json", json.dumps(content, indent=2, sort_keys=False), contents.sha, branch="dev")

def updateGitHubFile3(user, repo_name, path_to_file, shaPassed, content):
    g = Github(token)
    # print('--> Logged in')
    # Get User from the token used to login
    user = g.get_user()
    repo = g.get_repo(user.login+"/"+repo_name)
    contents = repo.get_contents(path_to_file)
    repo.update_file(contents.path, "Updated package-lock.json", json.dumps(content, indent=2, sort_keys=False), contents.sha, branch="dev")

def createPullRequest(user, repo_name, wantedLibrary, wantedVersion, fetchedVersion, branch_name, base_branch_name):
    g= Github(token)
    user = g.get_user()
    repo = g.get_repo(user.login+"/"+repo_name)
    title= 'chore: updates '+wantedLibrary+' to '+wantedVersion
    body ='Updates the version of '+wantedLibrary+' from '+fetchedVersion+' to '+wantedVersion
    pr = repo.create_pull(title=title, body=body, head=branch_name, base=base_branch_name)
    # print(pr)
    return pr.html_url

parser = argparse.ArgumentParser(description='This is a tool developed by Ayan Sadhukhan for the Dyte Assessment')

parser.add_argument('-update', action='store_true')

parser.add_argument(
    "--file",
    "-i",
    type=str,
    required=True,
    help = "Enter the file name"
)

parser.add_argument(
    "dependency_name",
    type=str,
    help = "Enter the dependency name"
)

# callling arg parser
args = parser.parse_args()
file_name = args.file
dependency_name = args.dependency_name

if args.update == True:
    # print('Update is True')
    if file_name[-4:] == '.csv':
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                for i in range(len(line)):
                    if i == 1:
                        if(line[i]!='repo'):
                            repo_name = line[i][27:]
                            repo_name = repo_name[0:-1] if repo_name[len(repo_name)-1] == '/' else repo_name
                            # print(repo_name)
                            fetchedJSON =(fetchURLDetails('ayan2809', repo_name, 'package.json'))

                            wantedLibrary = getLibraryName(dependency_name)
                            wantedVersion = getLibraryVersion(dependency_name)
                            fetchedVersion = fetchedJSON['dependencies'][wantedLibrary].split('^')[1]

                            ans = versionCompare(fetchedVersion ,wantedVersion)
                            if ans < 0:
                                updateLink=''
                                # createPullRequest('ayan2809', repo_name, 'main', 'main', 'Update dependency', 'Update dependency')
                                
                                shaNumber=fetchSHAnumber('ayan2809', repo_name, 'package.json')
                                # print(shaNumber)
                                # fullJSON =fetchFullJSON('ayan2809', repo_name, 'package.json')
                                
                                fetchedJSON['dependencies'][wantedLibrary]='^'+wantedVersion
                                # print(fetchedJSON)
                                
                                # baseEncodedContent=base64.urlsafe_b64encode(json.dumps(fetchedJSON).encode()).decode()
                                fetchedJSON2=fetchFullJSON('ayan2809', repo_name, 'package-lock.json')
                                updateGitHubFile2('ayan2809', repo_name, 'package.json', shaNumber, fetchedJSON)
                                fetchedJSON2['packages'][""]['dependencies'][wantedLibrary]='^'+wantedVersion

                                fetchedJSON2['packages']['node_modules/'+wantedLibrary]['version']='^'+wantedVersion
                                # print(fetchedJSON2['packages']['node_modules/'+wantedLibrary]['resolved'])

                                fetchedJSON2['packages']['node_modules/'+wantedLibrary]['resolved']=fetchedJSON2['packages']['node_modules/'+wantedLibrary]['resolved'].split(wantedLibrary+'-')[0]+wantedLibrary+'-'+wantedVersion+'.tgz'

                                fetchedJSON2['dependencies'][wantedLibrary]['version']='^'+wantedVersion

                                fetchedJSON2['dependencies'][wantedLibrary]['resolved']=fetchedJSON2['dependencies'][wantedLibrary]['resolved'].split(wantedLibrary+'-')[0]+wantedLibrary+'-'+wantedVersion+'.tgz'

                                # print(fetchedJSON2)

                                updateGitHubFile3('ayan2809', repo_name, 'package-lock.json', shaNumber, fetchedJSON2)
                                # fullJSON['content']=baseEncodedContent
                                getPRurl=createPullRequest('ayan2809', repo_name, wantedLibrary, wantedVersion, fetchedVersion, 'dev', 'main')
                                # print(getPRurl)
                                # updateGitHubFile('ayan2809', repo_name, 'package.json', shaNumber, fetchedJSON)
                                makeCSVforDependencyUpdate(repo_name, line[i], fetchedVersion, 'false', updateLink=getPRurl)
                                # print(line[i], fetchedVersion, wantedVersion, 'false')
                            elif ans >= 0:
                                makeCSVforDependencyUpdate(repo_name, line[i], fetchedVersion, 'true', '')
                                # print(line[i], fetchedVersion, wantedVersion, 'No true')
                            # print('\n')
                        else:
                            csv.writer(open('output2.csv', 'w'))
                            makeCSVforDependencyUpdate('name', 'repo', 'version', 'version_satisfied', 'update_pr')
                       

    else:
        print("File not supported")
else:
    if file_name[-4:] == '.csv':
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                for i in range(len(line)):
                    if i == 1:
                        if(line[i]!='repo'):
                            repo_name = line[i][27:]
                            repo_name = repo_name[0:-1] if repo_name[len(repo_name)-1] == '/' else repo_name
                            # print(repo_name)
                            fetchedJSON =(fetchURLDetails('ayan2809', repo_name, 'package.json'))

                            wantedLibrary = getLibraryName(dependency_name)
                            wantedVersion = getLibraryVersion(dependency_name)
                            fetchedVersion = fetchedJSON['dependencies'][wantedLibrary].split('^')[1]

                            ans = versionCompare(fetchedVersion ,wantedVersion)
                            if ans < 0:
                                makeCSVforDependencyCheck(repo_name, line[i], fetchedVersion, 'false')
                                # print(line[i], fetchedVersion, wantedVersion, 'false')
                            elif ans >= 0:
                                makeCSVforDependencyCheck(repo_name, line[i], fetchedVersion, 'true')
                                # print(line[i], fetchedVersion, wantedVersion, 'No true')
                            # print('\n')
                        else:
                            csv.writer(open('output1.csv', 'w'))
                            makeCSVforDependencyCheck('name', 'repo', 'version', 'version_satisfied')
                       

    else:
        print("File not supported")

