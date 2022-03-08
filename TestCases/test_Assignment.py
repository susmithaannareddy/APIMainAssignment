import requests
import json
import pandas as pd
import matplotlib as plt


def json_reader(path):
    with open(path) as json_file:
        return json.load(json_file)


data_2 = pd.read_csv('/Users/asusmitha/Desktop')
print(data_2.shape)


def to_json(data):
    url = "https://documenter.getpostman.com/view/8858534/SW7dX7JG#f5ee09d6-b9e7-4dc8-b382-7904a882d145"
    response = requests.get(url)
    print(response)
    payload = {
        "name": "Susmitha",
        "email": "asusmitha@hashedin.com",
        "password": "admin",
        "age": "20"
    }
    resp = requests.put("https://hbs-ob-stage.herokuapp.com/user", data=payload)
    print(resp)
    print(resp.json())
    print(resp.headers.get("Content_Type"))


if __name__ == '__main__':
    all_data = json_reader('template.json')
    for data in all_data:
        print(data['name'])
        print(data['email'])
        print(data['password'])
    to_json(all_data)
    for a in all_data:
        print(a)
