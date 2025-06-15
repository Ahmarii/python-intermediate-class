class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses
    #Function -> Method
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("-" * 20)

student1 = Student("Alice","Wonder", 20, ["Math", "English"])
student2 = Student("Bob","Builder", 22, ["Physics", "History"])

student1.display_info()
student2.display_info()