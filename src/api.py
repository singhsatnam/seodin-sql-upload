import requests

login = {
  "password": "admin",
  "rememberMe": "true",
  "username": "admin"
}

jwt_endpoint = 'http://localhost:9060/api/'
path = '/home/sat/Documents/Data'

def token():
  jwt_token_response = requests.post(url=jwt_endpoint + 'authenticate', json=login)
  # print jwt_token_response.text
  token = jwt_token_response.json()['id_token']
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
  print "From api get: ", type, id
  print jwt_endpoint + type + '/' + str(id)
  h = headers()
  print "From get: ", h
  response = requests.get(url=jwt_endpoint + type + '/' + str(id), headers=h)
  print response
  print response.text
  return response.json()

def getAll(type):
  print jwt_endpoint + type
  print headers()
  response = requests.get(url=jwt_endpoint + type, headers=headers())
  print response.json()
  return response.json()

