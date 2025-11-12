import azure.functions as func
from todos.todos_router import todo_bp


app = func.FunctionApp()


app.register_blueprint(todo_bp)
