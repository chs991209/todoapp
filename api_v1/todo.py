import datetime

import requests
from flask import jsonify
from flask import request

from models import Todo, db
from . import api


def send_slack(msg):
    res = requests.post('https://hooks.slack.com/services/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', json={
        'text': msg
    }, headers={'Content-Type': 'application/json'})


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


@api.route('/slack/todos', methods=['POST'])
def slack_todos():
    res = request.form['text'].split(' ')
    cmd, *args = res

    global ret_msg
    ret_msg = ''

    if cmd == 'create':
        todo_name = args[0]

        todo = Todo()
        todo.title = todo_name

        db.session.add(todo)
        db.session.commit()

        ret_msg = 'Todo Generated!'
        send_slack('[%s] "%s" 할 일을 만들었습니다' % (str(datetime.datetime.now()), todo_name))

    elif cmd == 'list':
        todos = Todo.query.all()
        for idx, todo in enumerate(todos):
            # ret_msg += "" + str(idx+1) + " " + todo.title + " " + str(todo.tstamp)
            ret_msg += '%d %s (~ %s)\n' % (idx+1, todo.title, str(todo.tstamp))

    return ret_msg
