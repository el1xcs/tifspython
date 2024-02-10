class Person:
    def __init__(self, nume, varsta):
        self.nume=nume
        self.varsta=varsta

    def get_details(self):
        pass

class Student(Person):
    def __init__(self, nume, varsta, grade):
        super().__init__(nume,varsta)
        self.__grade=grade
        if 1<=grade<=12:
            self.__grade=grade
        else:
            raise AttributeError('Clasa nu este valabila')
    
    def get_details(self):
        return f"Elevul {self.nume} de vasrta {self.varsta} ani, invata in clasa {self.__grade} "


class Teacher(Person):
    def __init__(self, nume, varsta, subject):
        super().__init__(nume,varsta)
        self.subject=subject


    def get_details(self):
        return f"Profesorul {self.nume} de vasrta {self.varsta} ani, preda obiectul {self.subject} "

Artur=Teacher('Artur',32,'Informatica')
Maria=Teacher('Maria',36,'Matematica')
Dan=Student('Dan',17,11)
Ion=Student('Ion',15,9)

def school_directory(people):
    for person in people:
        print(person.get_details())

school_people=[Dan,Ion,Artur,Maria]

print(school_directory(school_people))