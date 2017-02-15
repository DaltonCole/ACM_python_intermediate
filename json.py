import json

json_string = ''

# Open File
with open('jsonExample.json', 'r') as f:
	json_string = f.read()

# Parse Json
parsed_json = json.loads(json_string)

print(type(parsed_json)) # <class 'list'>

print(parsed_json[0]['_id']) # 58a4c09d6d2ce156e646b494

for thing in parsed_json:
	for person in thing['friends']:
		print(person['id'], person['name'])

'''
0 Rachael Tran
1 Christian Cameron
2 Kirsten Wooten
0 Watson Rosales
1 Grimes Wolf
2 Alison Hanson
0 Paul Daniel
1 Stone Medina
2 Allyson Caldwell
0 Maribel Holt
1 Jensen Salazar
2 Adela Nichols
0 Elaine Wells
1 Conley Coleman
2 Long Jacobson
'''

string_json = json.dumps(parsed_json)

print(type(string_json)) # <class 'str'>