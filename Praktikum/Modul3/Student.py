from Praktikum.Modul3.Person import Person


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
