# Connecting the Batabase

import sqlite3

class StudentModel:
    def __init__(self, db_name='Project.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Person (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Family TEXT NOT NULL,
                    Code TEXT NOT NULL,
                    Phone TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    Role TEXT NOT NULL
                    
                ) 
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS StudyField (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Description  TEXT 
                   
                )
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Adviser (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    StudyField_ID INTEGER NOT NULL,
                    Person_ID INTEGER NOT NULL,
                    FOREIGN KEY (Person_ID) REFERENCES  Person(ID),
                    FOREIGN KEY (StudyField_ID) REFERENCES  StudyField(ID)
                )
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Admin (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Person_ID INTEGER NOT NULL,
                    FOREIGN KEY (Person_ID) REFERENCES  Person(ID)
                )
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS StudyTitle (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,         
                    Adviser_ID INTEGER NOT NULL,
                    Title TEXT NOT NULL, 
                    Course_ID INTEGER NOT NULL, 
                    StartPage INTEGER NOT NULL,
                    EndPage INTEGER NOT NULL, 
                    CreatDate  DATE NOT NULL,
                    FOREIGN KEY (Course_ID) REFERENCES  Course(ID),
                    FOREIGN KEY (Adviser_ID) REFERENCES  Adviser(ID)
                    
                )
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS StudyPlan (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,         
                    Student_ID INTEGER NOT NULL, 
                    StudyTitle_ID INTEGER NOT NULL,    
                    StartTime DATE NOT NULL,
                    EndTime DATE NOT NULL, 
                    Description TEXT ,
                    Status  TEXT NOT NULL,
                    FOREIGN KEY (Student_ID) REFERENCES  student(ID),
                    FOREIGN KEY (StudyTitle_ID) REFERENCES  StudyTitle(ID)
                    
                )
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Course (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Pages INTEGER NOT NULL,
                    Grade_ID INTEGER NOT NULL,
                    Title TEXT NOT NULL,
                    FOREIGN KEY (Grade_ID) REFERENCES  Grade(ID)
                )
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Grade (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Title TEXT NOT NULL,
                    StudyField_ID INTEGER NOT NULL,       
                    FOREIGN KEY (StudyField_ID) REFERENCES  StudyField(ID)
                )
            ''')

            self.conn.execute('''
                
                CREATE TABLE IF NOT EXISTS student (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Grade_ID INTEGER NOT NULL,
                    StudyField_ID INTEGER NOT NULL,
                    Adviser_ID INTEGER NOT NULL,
                    StudyPlan_ID INTEGER NOT NULL,
                    Person_ID INTEGER NOT NULL,
                    FOREIGN KEY (Person_ID) REFERENCES  Person(ID),
                    FOREIGN KEY (StudyField_ID) REFERENCES  StudyField(ID),
                    FOREIGN KEY (StudyPlan_ID) REFERENCES  StudyPlan(ID),
                    FOREIGN KEY (Grade_ID) REFERENCES  Grade(ID),
                    FOREIGN KEY (Adviser_ID) REFERENCES  Grade(ID) 
                              
                )
            ''')
        self.conn.commit()

          

StudentModel() 
# اتصال به دیتابیس
conn = sqlite3.connect('Project.db')

StudyField_Data = [
    (1, 'Tajrobi', 'رشته تجربی'),
    (2, 'Riazi', 'رشته ریاضی'),
    (3, 'Ensani', 'رشته انسانی')
] 


Grade_Data = [
    (1,'Tenth', 1),
    (2, 'Eleventh', 1),
    (3, 'Twelfth', 1),
    (4, 'Tenth', 2),
    (5, 'Eleventh', 2),
    (6, 'Twelfth', 2),
    (7, 'Tenth', 3),
    (8, 'Eleventh', 3),
    (9, 'Twelfth', 3)
] 


Course_Data = [
    (1, 111, 1, 'زیست شناسی'),
    (2, 120, 1, 'فیزیک'),
    (3, 170, 1,  'ریاضی'),
]


conn.executemany(''' 
     INSERT INTO StudyField (ID, Name, Description)
     VALUES (?, ?, ?)
 ''', StudyField_Data) 


conn.executemany(''' 
     INSERT INTO Grade (ID, Title, StudyField_ID)
     VALUES (?, ?, ?)
 ''', Grade_Data)

conn.commit() 
conn.close()



class PersonRepository:
    def __init__(self, db_path='Project.db'):
        self.db_path = db_path

    def check_code_and_role(self, code):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT Role FROM Person WHERE Code = ? " ,(code,))
        result = cursor.fetchone()
        conn.close()
        #بررسی نقش مجاز
        if result:
            role = result[0]
            if role  in ["Admin", "Adviser"]:
               return True
            else:
               raise ValueError("Your role does not allow you to log in")
        else:
            raise ValueError("National code not found")

