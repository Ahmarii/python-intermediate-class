class Student:
    def __init__(self, fname,lname, age, courses):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.courses = courses
    
    #Method
    def get_fullname(self):
        return f"{self.fname} {self.lname}"
    
    #Function -> Method
    def display_info(self):
        print("Name:", self.get_fullname())
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("-" * 20)

student1 = Student("Alice","Wonder", 20, ["Math", "English"])
student2 = Student("Bob","Builder", 22, ["Physics", "History"])

student1.display_info()
student2.display_info()

student1.get_fullname()