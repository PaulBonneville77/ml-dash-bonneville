## un petit tableau de bord qui utilise un model

# ml-dash-bonneville

# Build image 

docker build -t api-mldash .
# Run conteneur 

docker run -p 5000:5000 -d api-mldash 