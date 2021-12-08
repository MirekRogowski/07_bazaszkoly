
class Classroom:

    def __init__(self, class_name):
        print("create classrom\n")
        self.class_name = class_name
        self.students = []
        self.subjects = []
        self.teachers = []
        self.educators = []


def input_class_name():
    input_class_name = input("Podaj nazwę klasy: ")
    input_class_name_list = []
    while input_class_name:
        if input_class_name not in data_school:
            data_school[input_class_name ] = Classroom(input_class_name)
        input_class_name_list.append(input_class_name)
        input_class_name = input("Podaj nazwę klasy: ")
    return input_class_name_list


class Student:

    def __init__(self, name):
        print("create student\n")
        self.name = name
        self.class_name = ""

    def get_classes(self):
        self.class_name = input("Podaj klasę: ")
        if self.class_name not in data_school:
            data_school[self.class_name] = Classroom(self.class_name)
        data_school[self.class_name].students.append(self.name)


class Teacher:
    def __init__(self, name):
        print("Create Techaer")
        self.name = name
        self.subject = " "
        self.class_names = []

    def get_classes(self):
        self.subject = input("Podaj nazwę przedmiotu: ")
        self.class_names = input_class_name()
        # add teacher and subject
        for c in self.class_names:
            # data_school[c].teachers = self.name
            # data_school[c].subjects = self.subject
            data_school[c].teachers.append([self.name])
            data_school[c].subjects.append(self.subject)


class Tutor:

    def __init__(self, name):
        print("Create Tutor")
        self.name = name
        self.class_names = []

    def get_classes(self):
        self.class_names = input_class_name()
        for c in self.class_names:
            data_school[c].tutor = self.name


while True:
    user_type = input(("Podaj typ użytkownika: "))
    if user_type == "koniec" or user_type == "k":
        print("Koniec programu. ")
        break
    user_name = input("Wprowadź imie i nazwisko: ")
    if user_type == "uczen" or user_type == "u":
        person = Student(user_name)
        person.get_classes()
    elif user_type == "nauczyciel" or user_type == "n":
        person = Teacher(user_name)
        person.get_classes()
    elif user_type == "wychowawca" or user_type == "w":
        person = Tutor(user_name)
        person.get_classes()
    else:
        print("Nieprawidłowy typ uzytkownika: ")
        break


