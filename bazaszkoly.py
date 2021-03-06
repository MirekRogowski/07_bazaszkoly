import sys

data_school = {}
action = ["uczen", "nauczyciel", "wychowawca", "koniec" ]


class Classroom:
    def __init__(self, class_name):
        print("Create Classrom")
        self.class_name = class_name
        self.students = []
        self.tutor = None
        self.subjects = []
        self.teachers = []

    def display(self):
        for c in self.class_name:
            print(f"Klasa:  {data_school[c].class_name} - Wychowawca: {data_school[c].tutor} "
                  f"\nUczniowie:  {data_school[c].students} ")

    # def __repr__(self) -> str:
    #      return f"Classrom: '{self.class_name}, {self.students}, {self.tutor}, {self.subjects}, {self.teachers}"


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
        print("Create Student")
        self.name = name
        self.class_name = ""

    def get_classes(self):
        self.class_name = input("Podaj klasę: ")
        if self.class_name not in data_school:
            data_school[self.class_name] = Classroom(self.class_name)
        data_school[self.class_name].students.append(self.name)

    def display(self):
        if self.name in data_school:
            print(f"Uczeń - {self.name} - klasa: {self.class_name}")
            for c in self.class_name:
                for item in range(len(data_school[c].teachers)):
                    print(f"Nauczyciel - {data_school[c].teachers[item]} - {data_school[c].subjects[item]} ")

    # def __repr__(self) -> str:
    #      return f"Students: '{self.name}, {self.class_name}"


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
            data_school[c].teachers.append([self.name])
            data_school[c].subjects.append(self.subject)


    def display(self):
        if self.name in data_school:
            print(f"Nauczyciel - {self.name} - {self.subject},  klasy: {self.class_names}")
            for c in self.class_names:
               print(f"Wychowawca - {data_school[c].tutor}, klasa: {data_school[c].class_name}")

    # def __repr__(self) -> str:
    #     return f"Teacher: '{self.name}, {self.subject}, {self.class_names}"


class Tutor:

    def __init__(self, name):
        print("Create Tutor")
        self.name = name
        self.class_names = []

    #metoda, wywołuje  funkcje input_class_name(), która przypisze wartości zwrcone przez funkcja
    #do atrybutu tej klasy
    def get_classes(self):
        self.class_names = input_class_name()
        for c in self.class_names:
            data_school[c].tutor = self.name

    def display(self):
        for c in self.class_names:
            print(f"Wychowawca {data_school[c].tutor} - klasa:{data_school[c].class_name} ")
            print(f"Uczniowie {data_school[c].students}")

    # def __repr__(self) -> str:
    #     return f"Tutor: '{self.name}, {self.class_names}"


print(f"\nDostępne akcje: {action }")
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
        print(f"\nDozwolone akcje: {action }")        

        break

    data_school[user_name] = person

# # print(data_school)
# dictionary_items = data_school.items()

for item in data_school.items():
    print(item)


# for key, object in data_school.items():
#     print(key)
#     for attribute, value in object.class_name:
#         print(f"{attribute} : {value}")

if len(sys.argv) == 2:
    phrase = sys.argv[1]
    print("_" * 60)
    data_school[phrase].display()
