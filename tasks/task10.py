from datetime import datetime
import pymysql
pymysql.install_as_MySQLdb()

class db:

    def __init__(self):
        self.con = None
        self.cur = None
        
    def connect(self):
        self.con = pymysql.connect("localhost", "user", "pass", "test_db")
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        print("Connected to database.")
    
    def create(self):
        self.cur.execute("DROP TABLE IF EXISTS tutorials")
        sql = '''CREATE TABLE tutorials(
        tutorial_id INT NOT NULL AUTO_INCREMENT,
        tutorial_title VARCHAR(100) NOT NULL,
        tutorial_author VARCHAR(40) NOT NULL,
        submission_date DATE,
        PRIMARY KEY ( tutorial_id ));'''
        self.cur.execute(sql)
        self.con.commit()
        print("Creating tutorials table...")
        
    def insert(self):
        title = input("Please enter tutorial title: ")
        author = input("Please enter tutorial author: ")
        sql = "INSERT INTO tutorials (tutorial_title, tutorial_author) VALUES ('{0}', '{1}')".format(title, author)
        self.cur.execute(sql)
        self.con.commit()
        print("New tutorial added: '{0}' by '{1}'...".format(title, author))
        
    def update(self):
        fields = {
            1 : "tutorial_title",
            2 : "tutorial_author",
            3 : "submission_date"
            }
        
        tutorial = input("Please enter the tutorial name to be updated: ")
        update = input("Please enter the field number to be updated (1 = title, 2 = author, 3 = submission date): ")
        value = input("Please enter the updated value: ")
        sql = "UPDATE tutorials SET {1} = '{2}' WHERE tutorial_title = '{0}'".format(tutorial, fields.get(int(update)), value)
        self.cur.execute(sql)
        self.con.commit()
        print("Tutorial '{0}' updated...".format(tutorial))

    def delete(self):
        tutorial = input("Please enter the tutorial name to be deleted: ")
        sql = "DELETE FROM tutorials WHERE tutorial_title = '{0}'".format(tutorial)
        self.cur.execute(sql)
        self.con.commit()
        print("Tutorial '{0}' deleted...".format(tutorial))
        
    def retrieve(self):
        self.cur.execute("SELECT tutorial_id, tutorial_title, tutorial_author, submission_date FROM tutorials")
        if self.cur.rowcount == 0:
            print("No rows to retrieve...")
        else:
            csv = "tutorial_id"+","+"tutorial_title"+","+"tutorial_author"+","+"submission_date"+"\n"
            for row in self.cur.fetchall():
                print(row)
                csv += "{tutorial_id},{tutorial_title},{tutorial_author},{submission_date}\n".format(**row)
            file = r"D:\temp\tutorials_{0}.csv".format(datetime.now().strftime("%Y%m%d_%H%M%S"))
            with open(file, 'w') as w:
                w.write(csv)
            print("{0} rows retrieved...".format(self.cur.rowcount))
            
    def disconnect(self):
        self.cur.close()
        self.con.close()
        self.cur = None
        self.con = None
        print("Disconnected from database.")
