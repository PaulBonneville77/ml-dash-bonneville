import requests

x = requests.post('http://localhost:5000/prediction', json={'_taille':150,'_nb_rooms':4,'_garden':0})

print(x.text)