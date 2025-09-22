

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

