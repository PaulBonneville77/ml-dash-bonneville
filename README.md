## un petit tableau de bord qui utilise un model

# ml-dash-bonneville

# Build image 
docker build -t api-mldash .

# Run conteneur 
docker run -p 5000:5000 -d api-mldash 

# Request for prediction
Y = requests.post('http://localhost:5000/prediction', json={'_taille':200,'_nb_rooms':6,'_garden':1})