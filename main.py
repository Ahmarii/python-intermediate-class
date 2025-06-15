class Student:
    #class variable
    student_count = 0
    
    def __init__(self, fname,lname, age, courses,salary):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.courses = courses
        self.pocket_money = 0
        self.salary = salary
        
        Student.student_count += 1
    
    #Method
    def get_fullname(self):
        return f"{self.fname} {self.lname}"
    
    #Function -> Method
    def display_info(self):
        print("Name:", self.get_fullname())
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("-" * 20)

student1 = Student("Alice","Wonder", 20, ["Math", "English"],1000)
student2 = Student("Bob","Builder", 22, ["Physics", "History"],2000)
student3 = Student("Timmy","Builder", 22, ["Physics", "History"],2000)

student1.display_info()
student2.display_info()

student1.get_fullname()

print(Student.student_count)