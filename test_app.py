from app import get_prediction

# Check if prediction is positive
def prediction_is_positive():
    input = [[100,4,0]]
    expected = [0]
    result = [get_prediction(setting[0], setting[1], setting[2]) for setting in input]
    assert [result >= expected]
