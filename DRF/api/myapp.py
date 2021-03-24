import requests
import json
url1 = "http://127.0.0.1:8000/stuinfo/"
url2 = "http://127.0.0.1:8000/stucreate/"
URL = "http://127.0.0.1:8000/studentapi/"
url3 = "http://127.0.0.1:8000/update/"
url4 = "http://127.0.0.1:8000/delete/"
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
# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)
#     r = requests.get(url = URL, data = json_data)
#     data = r.json()
#     print(data)

# get_data(2)


#create
def post_data():
    data = {
        'name':'Ram',
        'roll':10,
        'city': 'Ayodhya'
    }
    json_data = json.dumps(data)
    r = requests.post(url = url2, data = json_data)
    data = r.json()
    print(data)

post_data()

# #update
# def update_data():
#     data = {
#         'id':5,
#         'roll':5,
#     }
#     json_data = json.dumps(data)
#     r = requests.put(url = url3, data = json_data)
#     data = r.json()
#     print(data)

# update_data()

#delete
# def delete_data():
#     data = {'id': 4}
#     json_data = json.dumps(data)
#     r = requests.delete(url = url4, data = json_data)
#     data = r.json()
#     print(data)

# delete_data()