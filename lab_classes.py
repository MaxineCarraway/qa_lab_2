# Part one
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# creating objects of the student class
student1 = student("John", 20)
student2 = student("Jane", 22)

# getting the age of student1
print(student1.age)

# Part two
class Student:
    def __init__(self, name, age, current_class):
        self.name = name
        self.age = age
        self.current_class = current_class
    
    def calculate_average_score(self, score1, score2, score3):
        average_score = (score1 + score2 + score3) / 3
        return average_score
        
# creating objects of the student class
student3 = Student("John", 20, "Class A")
student4 = Student("Jane", 22, "Class B")

# calculating average test score for student3
print("Average test score: ",  average_score)



