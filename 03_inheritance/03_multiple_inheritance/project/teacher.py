from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    def __init__(self):
        super().__init__()
        Employee.__init__(self)

    def teach(self):
        return "teaching..."

