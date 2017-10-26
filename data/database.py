##==============================================================================
##	██████████████████████████████████████████████████████████████████
##	█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
##	█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
##	█░░░░█████████░█████░░████░██████████░█████░██████████░░█████░░░░█
##	█░░░███░░░░░░░░░███░░░░██░░░███░░░░███░███░░░███░░░░███░░███░░░░░█
##	█░░░░█████████░░███░░░░██░░░█████████░░███░░░█████████░░░███░░░░░█
##	█░░░░░░░░░░░███░███░░░░██░░░███░░░░░░░░███░░░███░░███░░░░███░░░░░█
##	█░░░██████████░░░███████░░░█████░░░░░░█████░█████░░████░█████░░░░█
##	█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
##	█░fb.com/isalapi | github.com/mrsupiri | linkedin.com/in/supiri░░█
##	█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
##	██████████████████████████████████████████████████████████████████
##==============================================================================



import sqlite3
import gc


class database:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('data/database.db')
            self.c = self.conn.cursor()
        except Exception as e:
            print(str(type(e).__name__) + " : " + str(e))

    def read(self, query, *pars):
        try:
            # query = _escape_unicode(query)
            self.c.execute(query, pars)
            return self.c.fetchall()
        except Exception as e:
            print(str(type(e).__name__) + " : " + str(e))

    def readall(self, query):
        try:
            # query = _escape_unicode(query)
            self.c.execute(query)
            return self.c.fetchall()
        except Exception as e:
            print(str(type(e).__name__) + " : " + str(e))



    def write(self, query, *pars):
        try:
            # query = _escape_unicode(query)
            self.c.execute(query, pars)
            self.conn.commit()
            return query
        except Exception as e:
            return str(str(type(e).__name__) + " : " + str(e))

    def delete(self, table, id):
        self.write("DELETE FROM '{}' WHERE id = '{}'".format(table, id))

    def close(self):
        self.c.close()
        self.conn.close()
        gc.collect()
