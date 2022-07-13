from app import get_prediction
import requests

# Check if prediction is positive
def test_prediction_is_positive():
    input = [[100,4,0],[120,5,1]]
    result = [get_prediction(setting[0], setting[1], setting[2]) for setting in input]
    assert all(price > 0 for price in result)

# Check if send 400 error when taille is negative
def test_taille_negative_error():
    X = {'_taille':-200,'_nb_rooms':6,'_garden':1}
    Y = requests.post('http://localhost:5000/prediction', json=X)
    assert Y.status_code == 400

# Check if send 400 error when nb_rooms is negative
def test_nb_rooms_negative_error():
    X = {'_taille':200,'_nb_rooms':-6,'_garden':1}
    Y = requests.post('http://localhost:5000/prediction', json=X)
    assert Y.status_code == 400

# Check if send 400 error when garden is not a boolean
def test_garden_not_boolean_error():
    X = {'_taille':200,'_nb_rooms':6,'_garden':3}
    Y = requests.post('http://localhost:5000/prediction', json=X)
    assert Y.status_code == 400
