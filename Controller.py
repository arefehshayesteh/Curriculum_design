from Model import PersonRepository

class PersonService:
    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def is_code_valid(self, code):
        #بررسی کد و نقش
        return self.repository.check_code_and_role(code)

    def fetch_person_info(self, code):
        return "خوش امدید"
