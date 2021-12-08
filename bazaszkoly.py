
class Classroom:

    def __init__(self, class_name):
        print("create classrom\n")
        self.class_name = class_name
        self.students = []
        self.subjects = []
        self.teachers = []
        self.educators = []


class Student:

    def __init__(self, name):
        print("create student\n")
        self.name = name
        self.class_name = ""


class Teacher:

    def __init__(self, name):
        print("create techaer - nauczyciel\n")
        self.name = name
        self.subject = ""
        self.class_names = []


class Tutor:

    def __init__(self, name):
        print("Create Tutor")
        self.name = name
        self.class_names = []





