import argparse
import csv
import requests
import base64
import json

def fetchURLDetails(user, repo_name, path_to_file):
    finalJson={}
    json_url = 'https://api.github.com/repos/'+user+'/'+repo_name+'/contents/'+path_to_file
    print(json_url)
    response = requests.get(json_url)
    if response.status_code == requests.codes.ok:
        jsonResponse = response.json() 
        content = base64.b64decode(jsonResponse['content'])
        jsonString = content.decode('utf-8')
        finalJson = json.loads(jsonString)
    else:
        print('Content was not found.')
    return finalJson

parser = argparse.ArgumentParser(description='This is a tool developed by Ayan Sadhukhan for the Dyte Assessment')

parser.add_argument(
    "--file",
    "-i",
    type=str,
    required=True,
    help = "Enter the file name"
)

# callling arg parser
args = parser.parse_args()

file_name = args.file

if file_name[-4:] == '.csv':
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            for i in range(len(line)):
                if i == 1:
                    if(line[i]!='repo'):
                        repo_name = line[i][27:]
                        repo_name = repo_name[0:-1] if repo_name[len(repo_name)-1] == '/' else repo_name
                        print(repo_name)
                        
                        fetchedJSON =(fetchURLDetails('dyte-in', repo_name, 'package.json'))
                        print(fetchedJSON['dependencies']['axios'])
                        print('\n')
                        # print(fetchURLDetails('dyte-in', repo_name, 'package-lock.json'))
                            # print(repo_name)    
                
            # print(line)

else:
    print("File not supported")


# print('Hello', file_name)

