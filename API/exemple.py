import requests
import json



#The dataset that will be used has already been transformed to an all integer file to easy up the transition to Json
#The numbers indicate the following:
#Gender: male 0 female 1 the rest is in ascending order of the original dataset

data = [[0, 22, 0, 1, 3, 3, 1, 0,0, 2, 0, 1, 2, 1, 4]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
url = 'http://localhost:5000/predict'
r = requests.post(url, data=j_data, headers=headers)
print(r.json())