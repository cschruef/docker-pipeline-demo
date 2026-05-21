from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(status="ok", service="greeter")


@app.get("/greet")
def greet():
    name = request.args.get("name", "Welt")
    return jsonify(greeting=f"Hallo, {name}!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)