from flask import Flask, request, jsonify, abort
import joblib

app = Flask(__name__)

def load_model():
    return joblib.load('regression.joblib')

def get_prediction(_taille, _nb_rooms, _garden):   
   model = load_model()

   if _taille > 0 and _nb_rooms > 0:      
      X = [[_taille, _nb_rooms, _garden]]
      prediction = model.predict(X)

   return prediction


@app.route("/")
def main_page():
   return "<h1>This is the main page</h1>"

@app.route("/prediction", methods=['POST'])
def predict():

   data = request.get_json(force=True)

   _taille = data['_taille']
   _nb_rooms = data['_nb_rooms']
   _garden = data['_garden']

   if _taille <= 0:
      return abort(400, description="mettre une taille positive")
   if _nb_rooms < 0:
      return abort(400, description='mettre nombre de chambre positif')
   if (_garden != 0) and (_garden != 1):
      return abort(400, description="_garden doit être un boolean")

   prediction = get_prediction(_taille, _nb_rooms, _garden)
   
   value = '{"prediction":'+str(prediction[0])+'}'

   return jsonify(value)

if __name__== "__main__":
   app.run('0.0.0.0')