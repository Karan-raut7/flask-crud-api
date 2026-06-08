from flask import Flask, request

app = Flask(__name__)
notes = []
@app.route("/notes", methods=["POST"])
def create_note():
    try:
        data = request.get_json()
        if not data:
            return {"error":"no JSON data provided"},400
        
        if "title" not in data:
            return {"error": "Title is required"}, 400
        notes.append(data)

        return {
        "message": "Success"
    },201
    except Exception as e:
        return{
            "error":str(e)
        },500
@app.route("/notes", methods=["GET"])
def get_notes():
    
   
    return notes,200
@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    if id>= len(notes):
        return {"error":"Note not found"},400
    notes.pop(id)
    return{
        "message": "note deleted"
    }

@app.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):
    if id>= len(notes):
        return {"error":"note not found"},404
    data = request.get_json()
    if not data:
        return{"error":"no json data provided"},400
    notes[id] = data
    return {
        "message": "note updated"
    }

if __name__ == "__main__":
    app.run(debug=True)