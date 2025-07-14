class person:
    def __init__(self,age,address):
       
        self.age=age
        self.address=address


class student(person):
    def __init__(self,age,address,course,name):
        person.__init__(self,age,address)
        self.all_course=course
        self.students_name=name
    def enroll_course():
        student_name=[]  
        name=input("please enter your name: ")
        age=input("please enter your age: ")
        address=input("please enter your address: ")      
        student_name.append(name)
        all_courses=[]
        q_course=input("is there is any course you want to learn? ")        
        while q_course == "yes":
            course=input("which course? ")
            all_courses.append(course) 
            q_course=input("is there is any another course you want to learn? ")       
        return student(student_name,age,address,all_courses)    
  



student_courses=[]
all_students_names=[]
user_choice=input("please enter your choice 1 or 2 \n 1) Creat another student   \n2) see all users \nyou choice: ")
while user_choice != "2":
    all_students=[]
    if user_choice =="1":
        students=student.enroll_course().all_course
        all_students.append(students)
    user_choice=input("please enter your choice 1 or 2 \n 1) Creat another student   \n2) exit \nyou choice: ")
    student_courses += (all_students)
student_index=(input("enter the number of student that you want to see his enroll courses (ENTER 'all' to see all students): "))
if student_index == "all":
    print(all_students_names)     
    print(" ,".join(student_courses)) 
elif int(student_index) < len(all_students_names):
    print(all_students_names[student_index-1])     
    print(" ,".join(student_courses[student_index-1])) 
else:
    print("this student number isn't found")