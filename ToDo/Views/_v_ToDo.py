import datetime

from flask import request, render_template, url_for
from flask import redirect, session, jsonify, abort

from ToDo import app, auth
from ToDo.Model._m_Todo import _m_ToDo


@app.route("/api/todo", methods=["POST"])
@auth.login_required
def _v_todo_api_post():
    if request.method == "POST":
        username = request.authorization["username"]
        to_return = _m_ToDo(username=username).store_todo(content=request.json)
        return jsonify(to_return)


@app.route("/api/todo", methods=["GET"])
@app.route("/api/todo/<todo_id>", methods=["GET"])
@auth.login_required
def _v_todo_api_get(todo_id=None):
    if request.method == "GET":
        username = request.authorization["username"]
        if todo_id:
            to_return = _m_ToDo(username=username).get_todo(todo_id=todo_id)
            return jsonify(to_return)
        else:
            to_return = _m_ToDo(username=username).get_todos()
            return jsonify([x for x in to_return if (x["active"] is True or x["active"] is None) and x["username"] == username])


@app.route("/api/todo/<todo_id>", methods=["POST"])
@auth.login_required
def _v_todo_api_update(todo_id):
    if request.method == "POST":
        username = request.authorization["username"]
        if todo_id:
            to_return = _m_ToDo(username=username).update_todo(todo_id=todo_id, content=request.json)
            return jsonify(to_return)
        else:
            abort(400, "No valid todo specied!")


@app.route("/api/todo", methods=["DELETE"])
@app.route("/api/todo/<todo_id>", methods=["DELETE"])
@auth.login_required
def _v_todo_api_delete(todo_id=None):
    if request.method == "DELETE":
        username = request.authorization["username"]
        if todo_id:
            to_return = _m_ToDo(username=username).delete_todo(todo_id=todo_id)
            return jsonify(to_return)
        else:
            to_return = _m_ToDo(username=username).delete_all_todos()
            return jsonify(to_return)


@app.route("/api/todo/deactivate/<todo_id>", methods=["DELETE"])
@auth.login_required
def _v_todo_api_deactivate(todo_id=None):
    if request.method == "DELETE":
        username = request.authorization["username"]
        if todo_id:
            to_return = _m_ToDo(username=username).update_todo(todo_id=todo_id, content={"active": False})
            return jsonify(to_return)
        else:
            abort(400, "No valid todo specied!")