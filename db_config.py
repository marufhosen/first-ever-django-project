import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connect_db():
    # Replace the placeholder with your Atlas connection string
    uri = "mongodb+srv://hello-django:ORGO6sBHRX2jIYgn@cluster0.lvals.mongodb.net/"

    # Set the Stable API version when creating a new client
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"{e} mongodb")


sys.modules[__name__] = connect_db
