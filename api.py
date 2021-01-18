from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "hola goku"})


@app.route('/pizzas')
def get_pizza():
    pizza = {
        "p1": "napolitana",
        "p2": "hawiana",
        "p3": "vegetariana"
     }
    return jsonify(pizza)


colegios = {
    "happy place" : {"inicial"},
    "santa cruz" : {"primaria"},
    "Javier Heraud" : {"secundaria"}
}

@app.route("/<slug>")

def get_colegios(slug):
    try:
      return jsonify(colegios[slug])
    except KeyError:
      abort(404)

if __name__ == "__main__":
   app.run(debug=True)
