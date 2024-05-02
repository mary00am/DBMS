import os

class databaseCred:
    DB_PORT=None
    DB_USER=None
    DB_PASSWORD=None
    DB_NAME=None
    DB_HOST=None
    def __init__(self):
        self.DB_PORT=os.environ['DB_PORT']
        self.DB_USER=os.environ['DB_USER']
        self.DB_PASSWORD=os.environ['DB_PASSWORD']
        self.DB_NAME=os.environ['DB_NAME']
        self.DB_HOST=os.environ['DB_HOST']

    def getCred(self):
        return self.DB_PORT, self.DB_USER, self.DB_PASSWORD, self.DB_NAME, self.DB_HOST