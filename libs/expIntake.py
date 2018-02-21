import cgi
from db import DBSRP as db
from textSent import TextSent as ts

# Debug Only
import cgitb
cgitb.enable()

class Intake():
    def main(self):
        form = cgi.FieldStorage()

        # Runs for production input
        if 'prod_name' in form:
            name = form['prod_name'].value
            content = form['prod_content'].value
            t_create = db.get_time(db)
            sent_score, sent_mag = ts.textSent(ts, content)

            db.add_entity_record(db, name, sent_mag, sent_score, t_create)

