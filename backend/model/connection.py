from model.mongo_utility import MongoDBHandler
from model.schemas import (
    student_schema,
    llm_log_schema,
    chatbot_log_schema,
    assignment_schema,
    courses_schema,
    programming_assignment_schema,
    lecture_schema,
)
from bson import ObjectId
import json

# def mongoDB():

# MongoDB connection details
uri = "paste your MongoDB URI"  # Replace with your MongoDB URI , e.g. mongodb://localhost:27017/ or mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority (we have removed our URI for security reasons)
db_name = "paste your database name here"  # Replace with your database name , e.g. LLM , Chatbot , SE (we have removed our database name for security reasons)

# Initialize MongoDB handler
mongo_handler = MongoDBHandler(uri, db_name)


# Create the collections if they don't exist
def create_collection():
    mongo_handler.create_collection("StudentCluster", student_schema)
    mongo_handler.create_collection("LLMLogs", llm_log_schema)
    mongo_handler.create_collection("ChatbotLogs", chatbot_log_schema)
    mongo_handler.create_collection("AssignmentsCluster", assignment_schema)
    mongo_handler.create_collection("CoursesCluster", courses_schema)
    mongo_handler.create_collection(
        "ProgrammingAssignmentsCluster", programming_assignment_schema
    )
    mongo_handler.create_collection("LecturesCluster", lecture_schema)


# Custom JSON encoder to handle ObjectId while returning JSON response
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(JSONEncoder, self).default(obj)
