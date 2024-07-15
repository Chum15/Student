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
    
    def comparison_grade(self):
        if student_1.average_grade() > student_2.average_grade() and student_1.average_grade() > student_3.average_grade():
            print(f'Самая высокаая оценка: {student_1.average_grade():.1f}\nУ студента: {student_1.name} {student_1.surname}!\n')
        elif student_2.average_grade() > student_3.average_grade() and student_2.average_grade() > student_1.average_grade():
            print(f'Самая высокаая оценка: {student_2.average_grade():.1f}\nУ студента: {student_2.name} {student_2.surname}!\n')
        elif student_3.average_grade() > student_1.average_grade() and student_3.average_grade() > student_2.average_grade():
            print(f'Самая высокаая оценка: {student_3.average_grade():.1f}\nУ студента: {student_3.name} {student_3.surname}!\n')
        elif student_1.average_grade() == student_2.average_grade() == student_3.average_grade():
            print('Оценки студентов равны!')
   

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
    
        
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.average_grade():.1f}\n')
    
   
    def comparison_grade(self):
        if lecturer_3.average_grade() > lecturer_2.average_grade() and lecturer_3.average_grade() > lecturer_1.average_grade():
            print(f'Самая высокаая оценка: {lecturer_3.average_grade():.1f}\nУ преподавателя: {lecturer_3.name} {lecturer_3.surname}!\n')
        elif lecturer_2.average_grade() > lecturer_3.average_grade() and lecturer_2.average_grade() > lecturer_1.average_grade():
            print(f'Самая высокаая оценка: {lecturer_2.average_grade():.1f}\nУ преподавателя: {lecturer_2.name} {lecturer_2.surname}!\n')
        elif lecturer_1.average_grade() > lecturer_2.average_grade() and lecturer_1.average_grade() > lecturer_3.average_grade():
            print(f'Самая высокаая оценка: {lecturer_1.average_grade():.1f}\nУ преподавателя: {lecturer_1.name} {lecturer_1.surname}!\n')
        elif lecturer_1.average_grade() == lecturer_2.average_grade() == lecturer_3.average_grade():
            print('Оценки преподавателей равны!')          
                
       
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
Lecturer.comparison_grade(lecturer_2)
Student.comparison_grade(student_1)
