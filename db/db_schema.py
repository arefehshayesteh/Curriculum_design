def create_table(db):
            db.execute('''
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

            db.execute('''
                CREATE TABLE IF NOT EXISTS StudyField (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Description  TEXT 
                   
                )
            ''')

            db.execute('''
                CREATE TABLE IF NOT EXISTS Adviser (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    StudyField_ID INTEGER NOT NULL,
                    Person_ID INTEGER NOT NULL,
                    FOREIGN KEY (Person_ID) REFERENCES  Person(ID),
                    FOREIGN KEY (StudyField_ID) REFERENCES  StudyField(ID)
                )
            ''')

            db.execute('''
                CREATE TABLE IF NOT EXISTS Admin (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Person_ID INTEGER NOT NULL,
                    FOREIGN KEY (Person_ID) REFERENCES  Person(ID)
                )
            ''')

            db.execute('''
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

            db.execute('''
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

            db.execute('''
                CREATE TABLE IF NOT EXISTS Course (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Title TEXT NOT NULL,
                    Pages INTEGER NOT NULL,
                    Grade_ID INTEGER NOT NULL,
                    FOREIGN KEY (Grade_ID) REFERENCES  Grade(ID)

                )
            ''')

            db.execute('''
                CREATE TABLE IF NOT EXISTS Grade (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Title TEXT NOT NULL,
                    StudyField_ID INTEGER NOT NULL,       
                    FOREIGN KEY (StudyField_ID) REFERENCES  StudyField(ID)
                )
            ''')

            db.execute('''
                
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