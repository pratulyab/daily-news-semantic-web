from flask import Flask, jsonify, request

@app.route('/', methods=['GET'])


if __name__ == '__main__':
	app = Flask(__name__)
	app.run(host='0.0.0.0', port=8000)