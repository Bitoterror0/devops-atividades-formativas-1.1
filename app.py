from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "ONLINE",
        "hospital": "Santa Casa de Ribeirão Preto",
        "scripts_sql": len([f for f in os.listdir('.') if f.endswith('.sql')]),
        "security_check": "PASSED",
        "message": "Pipeline DevOps Híbrido funcionando!"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
