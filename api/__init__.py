from flask_restful import Api
from app import flaskAppInstance
from .ProjectAPI import ProjectAPI
from .TaskAPI import Task
from .TaskByIDAPI import TaskByID

restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(ProjectAPI,"/")
restServerInstance.add_resource(Task,"/api/v1.0/task")
restServerInstance.add_resource(TaskByID,"/api/v1.0/task/id/<string:taskId>")