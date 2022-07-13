import requests

X = {'_taille':200,'_nb_rooms':6,'_garden':1}

Y = requests.post('http://localhost:5000/prediction', json=X)

if Y.status_code == 200:
    print(Y.json())
else:
    print(Y.text)