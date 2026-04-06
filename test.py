import json

# 1
# data = '{"name": "Ali", "age": 20, "city": "Tashkent"}'

# py_data = json.loads(data)
# print(py_data["name"], py_data["city"])


# 2
# user = {
#     "username": "coder123",
#     "email": "coder@mail.com",
#     "is_active": True
# }

# json_data = json.dumps(user, indent=4)
# print(json_data)


# # 3
# data = '''
# [
#     {"name": "Ali", "age": 20},
#     {"name": "Vali", "age": 25},
#     {"name": "Hasan", "age": 17}
# ]
# '''

# py_data = json.loads(data)
# for user in py_data:
#     if user["age"] > 18:
#         print(f"Name: {user['name']}")


# # 4
# data = '''
# [
#     {"name": "Ali", "age": 20},
#     {"name": "Vali", "age": 25},
#     {"name": "Hasan", "age": 17}
# ]
# '''

# py_data = json.loads(data)
# for user in py_data:
#     if user["name"] == "Vali":
#         print(f"Name: {user['name']}, Age: {user['age']}")



# # 5
# with open("users.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# for user in data:
#     print(user)


# # 6
# data = '''
# {
#   "user": {
#     "name": "Ali",
#     "address": {
#       "city": "Tashkent",
#       "zip": 100000
#     }
#   }
# }
# '''

# py_data = json.loads(data)

# print(py_data['user']['address']['city'])



# # 7
# data = '''
# {
#   "user": {
#     "name": "Ali",
#     "address": {
#       "city": "Tashkent",
#       "zip": 100000
#     }
#   }
# }
# '''

# with open("user.json", "w", encoding="utf=8") as file:
#     json.dump(data, file, indent=4)

# py_data = json.loads(data)
# py_data['user']['is_student'] = True

# with open("user.json", "w", encoding="utf=8") as file:
#     json.dump(py_data, file, indent=4)



# # 8
# data = '''
# {
#   "user": {
#     "name": "Ali",
#     "age": 20,
#     "address": {
#       "city": "Tashkent",
#       "zip": 100000
#     }
#   }
# }
# '''

# py_data = json.loads(data)
# py_data["user"]["age"] = 21
# print(py_data)



# 9
response = '''
{
  "status": "success",
  "data": [
    {"id": 1, "title": "Post 1"},
    {"id": 2, "title": "Post 2"}
  ]
}
'''

py_data = json.loads(response)
for post in py_data["data"]:
    print(f"Title: {post['title']}")

