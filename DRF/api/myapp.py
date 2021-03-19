import requests
import json
url1 = "http://127.0.0.1:8000/stuinfo/"
url2 = "http://127.0.0.1:8000/stucreate/"
URL = "http://127.0.0.1:8000/studentapi/"
# data = {
#     'name': 'Lakshman',
#     'roll': 4,
#     'city': 'Ayodhya'
# }

# json_data = json.dumps(data)
# r = requests.post(url = url2, data = json_data)
# #r = requests.get(url1)
# data = r.json()
# print(data)

#Read
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

get_data(2)