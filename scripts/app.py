import os

from flask import Flask, request, jsonify, render_template

# create an instance of the Flask class
app = Flask(__name__)

# @app.route('/')
# def index():
#     """Render the index page."""
#     return jsonify({"status": "success"})

# @app.route('/api/generate')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', debug=True, port=port)