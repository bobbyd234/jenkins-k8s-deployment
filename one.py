import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

emp = [
    {
        "name": "John Doe",
        "accessLevel": "dev,staging,production",
    },
    {
        "name": "Anderson Sterling",
        "accessLevel": "dev",
    },
    {
        "name": "Janel Tiffany",
        "accessLevel": "dev,Staging",
    },
    {
        "name": "Mary Anne Maitland",
        "accessLevel": "staging,Production",
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/employees', methods=['GET'])
def employees():
    return jsonify(emp)

@app.route('/divide/<int:numerator>/', methods=['GET']) #numerator is passed in in args curl request uri
def divide(numerator):
    denominator = request.args.get('denominator') #looks at the argument
    if not denominator:
        return jsonify({'error': 'Denominator not provided'}), 400
    try:
        denominator = int(denominator)
        result = numerator / denominator
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid denominator'}), 400
    except ZeroDivisionError:
        return jsonify({'error': 'Cannot divide by zero'}), 400

@app.route('/newdivide/', methods=['GET'])
def division():
    if 'a' in request.args:
        a = int(request.args['a'])
    else:
        return "No value passed." 
    
    if 'b' in request.args:
        b = int(request.args['b'])
    else:
        return "No b value passed." 
    
    if 'b' == 0:
        return 'The value of a b must not be zero, cannot divide.\n'
    
    result = a // b
    result1 = str(result)

    return f"The division result is {result1} \n."


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=801)