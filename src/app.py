
from flask import Flask, request, jsonify
from .script_runner import main

app = Flask(__name__)

@app.route('/inp',  methods=['POST'])
def moist_inp():
    data = request.json.get('data')
    if data is None:
        return jsonify({'error': 'No data provided'}), 400
    result = main(data)
    if result is None:
        return jsonify({'error': 'Invalid URL provided'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)