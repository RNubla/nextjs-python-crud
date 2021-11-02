import requests
import json
import csv

response = requests.get("http://localhost:8000/users")
print(json.dumps(response.json(), indent=2))

names = []
with open('MOCK_DATA_NAMES.csv')as f:
    reader = csv.reader(f)
    # data = list(reader)[1::]
    for row in reader:
        names.append(row[0])
print(len(names))

for name in names:

    post_params = json.dumps({
        'email': f'{name}@mail.com',
        'password': 'string'
    })

    resp = requests.post('http://localhost:8000/users', data=post_params)
    print(json.dumps(resp.json(), indent=2))
