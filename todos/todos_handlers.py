import azure.functions as func
from pydantic import ValidationError
from uuid import uuid4
import json


from .schema import Todo


todos = {}


def create_todo(req: func.HttpRequest) -> func.HttpResponse:
    try:
        todo = Todo.model_validate_json(req.get_body(), strict=True)
    except ValidationError:
        return func.HttpResponse("Invalid todo", status_code=400)
    todos[uuid4().hex] = todo.model_dump()
    return func.HttpResponse("New todo was added", status_code=201)


def list_all_todos(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"todos": todos})
    )


def get_todo_by_id(req: func.HttpRequest) -> func.HttpResponse:
    todo_id = req.route_params.get("todo_id")
    todo = todos.get(todo_id)
    if not todo:
        return func.HttpResponse("Not Found", status_code=404)
    return func.HttpResponse(json.dumps(todo))


def update_todo_by_id(req: func.HttpRequest) -> func.HttpResponse:
    todo_id = req.route_params.get("todo_id")
    todo = todos.get(todo_id)
    if not todo:
        return func.HttpResponse("Not Found", status_code=404)
    todo["completed"] = not todo["completed"]
    return func.HttpResponse("Todo checked")


def delete_todo_by_id(req: func.HttpRequest) -> func.HttpResponse:
    todo_id = req.route_params.get("todo_id")
    todo = todos.get(todo_id)
    if not todo:
        return func.HttpResponse("Not Found", status_code=404)
    del todos[todo_id]
    return func.HttpResponse("Todo deleted")
