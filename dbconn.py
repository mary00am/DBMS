import psycopg2
import config

databaseCredentials = config.databaseCred()
datacred=databaseCredentials.getCred()
class DBConn:
    def __init__(self):
        self.host=datacred[4]
        self.port=datacred[0]
        self.dbname=datacred[3]
        self.user=datacred[1]
        self.password=datacred[2]
        self.conn=None
    def connect_to_postgresql(self):
        try:
            # Establish a connection to the database
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            print("Connected to PostgreSQL database!")
            return True
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
            return False
            # Create a cursor object using the cursor() method
    def executeQuery(self,query,options=None):
        cursor = self.conn.cursor()
        # Execute a SQL query
        if options is None:
            cursor.execute(query)
        else:
            cursor.execute(query, options)
        self.conn.commit()
        # Fetch result
        try:
            results=cursor.fetchall()
        except psycopg2.ProgrammingError:
            results={'result':True}
        # Close the cursor and connection
        self.conn.close()
        cursor.close()
        return results