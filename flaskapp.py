from flask import Flask, json, jsonify, request
app = Flask(__name__)

data = [
    {
        "Contact": "9876276539",
        "Name": "Raju",
        "id": 1
    },
    {
        "Contact": "1234567898",
        "Name": "Avikshit",
        "id": 2
    }
]

@app.route("/addTask",methods=["POST"])
def addContact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "plese provide the task to be added"
        }, 400)
    else:
        c = {
            "id": data[-1]["id"]+1,
            "Contact": request.json["Contact"],
            "Name": request.json["Name"]
        }
        data.append(c)
        return jsonify({
            "status": "success",
            "message": "added successfully"
        })


@app.route("/display")
def displayContacts():
    return jsonify({
        "data": data
    })


if(__name__=="__main__"):
    app.run(debug=True)