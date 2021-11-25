from flask import jsonify
from flask import request


@api.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)


@api.route('/test', methods=['POST'])
def test():
    res = request.form['text']
    print(res)
    return jsonify(res)