from flask import Flask, render_template, request, jsonify
import atexit
import cf_deployment_tracker
import os
import json
from mongo import Conn

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)



port = int(os.getenv('PORT', 8000))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/visitors', methods=['GET'])
def get_visitor():
        return jsonify(list(map(lambda doc: doc['name'], Conn().user_info.find({}))))


@app.route('/api/visitors', methods=['POST'])
def put_visitor():
    user = request.json['name']
    data = {'name':user}
    Conn().user_info.insert_one(data)
    return 'Hello %s! I added you to the database.' % user


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
