class StudentService:
    def __init__(self):
        self.dao = StudentDao()

    def add_students(self, student):
        print('#### add_student ####')
        self.dao.create()
        self.dao.insert_many()
        print(f'>>> 입력된 학생 수: {self.dao.fetch_count()}')

    def login(self, id, pwd):
        return self.dao.login(id, pwd)
