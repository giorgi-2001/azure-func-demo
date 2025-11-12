import azure.functions as func
from azure.functions import Blueprint

from . import todos_handlers


todo_bp = Blueprint()


todos = {}


@todo_bp.route(route="todos", auth_level=func.AuthLevel.ANONYMOUS)
def todos_routes(req: func.HttpRequest) -> func.HttpResponse:
    match req.method:
        case "GET":
            return todos_handlers.list_all_todos(req)
        case "POST":
            return todos_handlers.create_todo(req)
    return func.HttpResponse(
        "Method not allowed", status_code=405
    )


@todo_bp.route(route="todos/{todo_id}", auth_level=func.AuthLevel.ANONYMOUS)
def todo_routes(req: func.HttpRequest) -> func.HttpResponse:
    match req.method:
        case "GET":
            return todos_handlers.get_todo_by_id(req)
        case "PATCH":
            return todos_handlers.update_todo_by_id(req)
        case "DELETE":
            return todos_handlers.delete_todo_by_id(req)
    return func.HttpResponse(
        "Method not allowed", status_code=405
    )
