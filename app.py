from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_db():
    with open('faqs.json', 'r') as f:
        return json.load(f)

@app.route('/get_faqs', methods=['GET'])
def get_faqs():
    return jsonify(load_db())

@app.route('/save_faqs', methods=['POST'])
def save_faqs():
    try:
        data = request.json
        with open('faqs.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify({"status": "success", "message": "Database updated"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get('message', '').lower().strip()
    db = load_db()
    
    triggers = ['staff', 'human', 'person', 'receptionist', 'speak to', 'talk to']
    if any(t in msg for t in triggers):
        return jsonify({
            "response": "Connecting you to the front desk receptionist immediately...",
            "handover_required": True
        })

    match_cat = None
    max_score = 0

    for cat, content in db.items():
        score = sum(1 for kw in content['keywords'] if kw in msg)
        if score > max_score:
            max_score = score
            match_cat = cat

    if max_score == 0:
        return jsonify({
            "response": "I'm passing this request to our team to help you directly.",
            "handover_required": True
        })

    return jsonify({
        "response": db[match_cat]['answer'],
        "handover_required": False
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
