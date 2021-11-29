import requests
from flask import jsonify
from flask import request

from . import api


@api.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        res = requests.post('https://hooks.slack.com/services/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', json={
            'text': 'Hello world'
        }, headers={'Content-Type': 'application/json'})
    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)


@api.route('/test', methods=['POST'])
def test():
    res = request.form['text']
    print(res)
    return jsonify(res)