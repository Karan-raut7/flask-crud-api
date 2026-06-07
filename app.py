from flask import Flask, request

app = Flask(__name__)
notes = []
@app.route("/notes", methods=["POST"])
def create_note():

    data = request.get_json()
    notes.append(data)

    return {
        "message": "Success"
    }
@app.route("/notes", methods=["GET"])
def get_notes():
    
   
    return notes
@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    notes.pop(id)
    return{
        "message": "note deleted"
    }

@app.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):
    data = request.get_json()

    notes[id] = data
    return {
        "message": "note updated"
    }
@app.route("/")
def home():
    return "Server is alive"
if __name__ == "__main__":
    app.run(debug=True)