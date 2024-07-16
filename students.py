class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in self.courses_in_progress or course in lecturer.courses_attached:

            for course in lecturer.courses_attached:
                if course in lecturer.rate_lecturer:
                    lecturer.rate_lecturer[course] += [grade]
                else:
                    lecturer.rate_lecturer[course] = [grade]
        else:
            return 'Ошибка' 

    def __str__(self):
        self.courses_in_progress = ' '.join(self.courses_in_progress)
        self.finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nПол: {self.gender}\nКурсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\nСредняя оценка за домашние задания: {self.average_grade():.1f}\n')         

    def average_grade(self): 
        for grade in self.grades.values():
            average_s = sum(grade) / len(grade)
        return average_s
    
    def average_course_score_student(self):
        course_score=[]
        for course in self.finished_courses:
            for grade in self.grades.values():
                print(course,grade)


    def __gt__(self, other):
        print(self.average_grade() > other.average_grade())

    def __lt__(self, other):
        print(self.average_grade() < other.average_grade())

    def __eq__(self, other):
        print(self.average_grade == other.average_grade())
                
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rate_lecturer = {}
    
    def average_grade(self): 
        for grade in self.rate_lecturer.values():
            average_l = sum(grade) / len(grade)   
        return average_l
    
    def average_course_score_lectors():
        pass
        
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.average_grade():.1f}\n')
    
   
    def __gt__(self, other):
        print(self.average_grade() > other.average_grade())

    def __lt__(self, other):
        print(self.average_grade() < other.average_grade())

    def __eq__(self, other):
        print(self.average_grade == other.average_grade())    
                
       
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
         return (f'Имя:{self.name}\nФамилия: {self.surname}\n')    

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            
            for course in student.finished_courses:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
      
# Lecturer 1
lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached = 'Основы'
# Lecturer 2
lecturer_2 = Lecturer('Алена', 'Батицкая')
lecturer_2.courses_attached = ['Git']
# Lecturer 3
lecturer_3 = Lecturer('Тимур', 'Анвартдинов')
lecturer_3.courses_attached = ['ООП']

# student_1
student_1 = Student('Игорь', 'Балабанов', 'мужской')
student_1.rate_hw(lecturer_1, 'Основы', 7)
student_1.rate_hw(lecturer_2, 'Git', 9)
student_1.rate_hw(lecturer_3, 'ООП',10)
student_1.courses_in_progress += ['ООП']
student_1.finished_courses += ['Основы']
student_1.finished_courses += ['Git']

#student_2
student_2 = Student('Иван', 'Иванов', 'мужской')
student_2.rate_hw(lecturer_1, 'Основы', 6)
student_2.rate_hw(lecturer_2, 'Git',10)
student_2.rate_hw(lecturer_3,'ООП', 9 )
student_2.courses_in_progress += ['ООП']
student_2.finished_courses += ['Основы']
student_2.finished_courses += ['Git']

#student_3
student_3 = Student('Юлия', 'Джумаева', 'женский')
student_3.rate_hw(lecturer_1, 'Основы', 4)
student_3.rate_hw(lecturer_2, 'Git',5)
student_3.rate_hw(lecturer_3,'ООП', 9 )
student_3.courses_in_progress += ['ООП']
student_3.finished_courses += ['Основы']
student_3.finished_courses += ['Git']

#reviewer_1
reviewer_1 = Reviewer('Александр', 'Бардин')
reviewer_1.courses_attached = ['Основы', 'ООП']
reviewer_1.rate_hw(student_1, 'Основы', 10)
reviewer_1.rate_hw(student_2, 'Основы', 7)
reviewer_1.rate_hw(student_3, 'Основы', 10)

#reviewer_2
reviewer_2=Reviewer('Алена', 'Батицкая')
reviewer_2.courses_attached=['Git']
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 8 )
reviewer_2.rate_hw(student_3, 'Git', 8)



print('Студенты: \n')
print(student_1)
print(student_2)
print(student_3)
print('Проверяющие: \n')
print(reviewer_1)
print(reviewer_2)
print('Преподаватели: \n')
print(lecturer_1)
print(lecturer_2)
print(lecturer_3) 
Lecturer.__eq__(lecturer_2, lecturer_3)
Lecturer.__gt__(lecturer_2, lecturer_3)
Lecturer.__lt__(lecturer_2, lecturer_3)
Student.__gt__(student_2, student_3)
Student.__lt__(student_2, student_3)
Student.__eq__(student_2, student_3)
Student.average_course_score_student(student_1)
