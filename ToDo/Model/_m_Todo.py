import os, json, sys, datetime, time
from ToDo.Library.TimeCalculator import TimeCalculator
from ToDo.Library.JsonDatabaseLibrary import JsonDatabaseLibrary
import uuid


class _m_ToDo:
    def __init__(self, username):
        self.dtnow = str(datetime.datetime.now())
        self.username = username

    def all_todos(self):
        to_return = []
        if JsonDatabaseLibrary().list_of_all_files():
            for _i in JsonDatabaseLibrary().list_of_all_files():
                to_return.append(JsonDatabaseLibrary().read_file(filename=_i))
            return to_return
        else:
            return False

    def store_todo(self, content):

        if self.get_todos():
            if [x for x in self.get_todos() if x["todo"] == content["todo"]]:
                return {
                    "message": "Already Exists !"
                }

        _id = str(uuid.uuid4())
        json_db_file = _id + ".json"

        to_store = {
            "id": _id,
            "todo": content["todo"],
            "created_at": self.dtnow,
            "updated_at": self.dtnow,
            "completed": False,
            "active": True,
            "username": self.username
        }

        try:
            JsonDatabaseLibrary(json_db_file=json_db_file).create_file(content=to_store)
            return {
                "message": "Successfully Stored !"
            }
        except Exception:
            return {
                "message": "Failed !"
            }

    def get_todos(self):
        all_todos = self.all_todos()
        if all_todos:
            # return [x for x in all_todos if x["active"] is True or x["active"] is None]
            # return [x for x in all_todos][::-1]
            print("AT", all_todos)
            return sorted(all_todos, key=lambda i: i['created_at'])
        else:
            return False

    def get_todo(self, todo_id):
        if self.get_todos():
            return [x for x in self.get_todos() if x["id"] == todo_id][0]
        else:
            return False

    def update_todo(self, todo_id, content):
        old_todo = self.get_todo(todo_id=todo_id)
        updated_todo = {
            "id": todo_id,
            "created_at": old_todo["created_at"],
            "updated_at": self.dtnow,
            "username": self.username
        }

        try:
            if "todo" in content.keys():
                if content["todo"] != old_todo["todo"]:
                    updated_todo["todo"] = content["todo"]
                else:
                    updated_todo["todo"] = old_todo["todo"]
            else:
                updated_todo["todo"] = old_todo["todo"]
        except Exception as e:
            updated_todo["todo"] = old_todo["todo"]

        try:
            if "completed" in content.keys():
                if content["completed"] != old_todo["completed"]:
                    updated_todo["completed"] = content["completed"]
                else:
                    updated_todo["completed"] = old_todo["completed"]
            else:
                updated_todo["completed"] = old_todo["completed"]
        except Exception as e:
            updated_todo["completed"] = old_todo["completed"]

        try:
            if "active" in content.keys():
                if content["active"] != old_todo["active"]:
                    updated_todo["active"] = content["active"]
                else:
                    updated_todo["active"] = old_todo["active"]
            else:
                updated_todo["active"] = old_todo["active"]
        except Exception as e:
            updated_todo["active"] = old_todo["active"]

        json_db_file = todo_id + ".json"

        try:
            JsonDatabaseLibrary(json_db_file=json_db_file).create_file(content=updated_todo)
            return {
                "message": "Successfully Stored !"
            }
        except Exception:
            return {
                "message": "Failed !"
            }

    def delete_todo(self, todo_id):
        try:
            JsonDatabaseLibrary().delete_file(filename=todo_id+".json")
            return {
                "message": f"Successfully Deleted todo: {todo_id} !"
            }
        except Exception:
            return {
                "message": f"Failed to delete {todo_id} !"
            }

    def delete_all_todos(self):
        all_todo_files = JsonDatabaseLibrary().list_of_all_files()
        if all_todo_files:
            try:
                for i in all_todo_files:
                    JsonDatabaseLibrary().delete_file(filename=i)
                return {
                    "message": f"Successfully Deleted todo's !"
                }
            except Exception:
                return {
                    "message": f"Failed to delete all ToDo !"
                }
        else:
            return {
                "message": f"Failed to delete all ToDo !"
            }