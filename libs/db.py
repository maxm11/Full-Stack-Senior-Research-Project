import psycopg2
from pandas import DataFrame

class DBSRP():
    def init():
        conn = psycopg2.connect("dbname=srp user=python password=python host=localhost")
        cur = conn.cursor()

        return conn, cur

    def add_entity_record(self, name, magnitude, score, t_create):
        # Get the database connection and the cursor
        conn, cur = self.init()

        # Validate all parameters
        if type(name) != str:
            raise Exception("Invalid Data Passed")
        if type(magnitude) != int:
            raise Exception("Invalid Data Passed")
        if type(score) != int:
            raise Exception("Invalid Data Passed")
        if type(t_create) != int:
            raise Exception("Invalid Data Passed")

        # Execute command
        cur.execute("INSERT INTO entities (name, magnitude, score, tcreate) VALUES (%s, %s, %s, %s)", ((name, ), magnitude, score, t_create))

        # Commit change
        conn.commit()

        # Close Connection and Cursor
        cur.close()
        conn.close()

        # Check that connections closed
        return True

    def add_experience(self, name, content, sent_score, sent_magnitude, t_create):
        # Get the database connection and the cursor
        conn, cur = self.init()

        # Validate all parameters
        if type(name) != str:
            raise Exception("Invalid Data Passed")
        if type(content) != str:
            raise Exception("Invalid Data Passed")
        if type(sent_score) != int:
            raise Exception("Invalid Data Passed")
        if type(sent_magnitude) != int:
            raise Exception("Invalid Data Passed")
        if type(t_create) != int:
            raise Exception("Invalid Data Passed")

        # Execute command
        cur.execute("INSERT INTO experiences (name, content, sent_score, sent_magnitude, processed, tcreate) VALUES (%s, %s, %s, %s, %s, %s)", ((name, ), content, sent_score, sent_magnitude, False, t_create))

        # Commit change
        conn.commit()

        # Close Connection and Cursor
        cur.close()
        conn.close()

        # Check that connections closed
        return True

    def get_entity(self, name):
        # Get the database connection and the cursor
        conn, cur = self.init()

        # Validate all parameters
        if type(name) != str:
            raise Exception("Invalid Data Passed")
        
        # Execute command
        cur.execute("SELECT * FROM entities WHERE name=%s", (name, ))

        # Return records as an array
        df = DataFrame.from_records(cur, columns=['name', 'magnitude', 'score', 't_create'])

        # Close Connection and Cursor
        cur.close()
        conn.close()

        return df
    
    def get_experience(self, id):
        # Get the database connection and the cursor
        conn, cur = self.init()

        # Validate all parameters
        if type(id) != int:
            raise Exception("Invalid Data Passed")
        
        # Execute command
        cur.execute("SELECT * FROM experiences WHERE id=%s", (id, ))

        # Return records as an array
        df = DataFrame.from_records(cur, columns=['name', 'content', 'sent_score', 'sent_magnitude', 'processed', 't_create', 'id'])

        # Close Connection and Cursor
        cur.close()
        conn.close()

        return df