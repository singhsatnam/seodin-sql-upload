import requests

login = {
  "password": "admin",
  "rememberMe": "true",
  "username": "admin"
}

jwt_endpoint = 'http://localhost:9000/api/'
path = 'C:/Users/admin/study/'

def token():
  jwt_token_response = requests.post(url=jwt_endpoint + 'authenticate', json=login)
  print jwt_token_response.text
  token = jwt_token_response.json()['id_token']
  print token
  print "hello"
  return token

def headers():
  headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token()}
  return headers

def request(name, type, data):
  print "Name: ", name , "\nType: ", type, "\nData: ", data
  response = requests.post(url=jwt_endpoint + type, headers=headers(), json=data)
  print name, response.status_code, response.reason
  return

def get(type, id):
  response = requests.get(url=jwt_endpoint + type + '/' + str(id), headers=headers())
  return response.json()

def getAll(type):
  response = requests.get(url=jwt_endpoint + type, headers=headers())
  return response.json()
