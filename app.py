from flask import Flask, request, make_response, jsonify
#from pyclasses import Test
from calculator import Calc
app = Flask(__name__)


#Methods
#GET - Data Fetch, POST - Data POST, PUT - Data Update, DELETE - Delete, PATCH -- Partial Data Update
# application_type / mime_filetype -- text/html, application/json, 
#@app.route("/add", methods=["GET"]) 
#def home():
   # a = int(request.args.get("a", 0)) # None
    #b = int(request.args.get("b", 0))
    #t1 = Test(a, b)
    #resp = make_response(
     #   jsonify({"result": t1.add()}, 200)
    #)
    #return resp

@app.route("/calc", methods=["POST"])
def calculate():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    
    a = data.get("a")
    b = data.get("b")
    operation = request.args.get("op")
    operation = data.get("op")

    if a is None or b is None or not operation:
        return jsonify({"error": "a, b and op are required"}), 400

    calc = Calc(a, b)

    if operation == "add":
        result = calc.add()
    elif operation == "sub":
        result = calc.sub()
    elif operation == "mul":
        result = calc.multiply()
    elif operation == "div":
        result = calc.divide()
    elif operation == "avg":
        result = calc.average()
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }) , 200

if __name__ == "__main__":
    app.run(debug=True)
