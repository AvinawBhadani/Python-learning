from flask import Flask, request, make_response, jsonify
from pyclasses import Test
app = Flask(__name__)


#Methods
#GET - Data Fetch, POST - Data POST, PUT - Data Update, DELETE - Delete, PATCH -- Partial Data Update
# application_type / mime_filetype -- text/html, application/json, 
@app.route("/add", methods=["GET"]) 
def home():
    a = int(request.args.get("a", 0)) # None
    b = int(request.args.get("b", 0))
    t1 = Test(a, b)
    resp = make_response(
        jsonify({"result": t1.add()}, 200)
    )
    return resp

@app.route("/test", methods=["GET"])
def test():
    return "dfhsvdfhjk"

if __name__ == "__main__":
    app.run(debug=True)

# REST - JSON