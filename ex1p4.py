class Student():
    def get_student_info(self, name, last_name, department, year_of_entrance):
        print(name.title() + " " + last_name.title() + " " + "поступил в " + 
        year_of_entrance + "г. на факультет: " + department + ".")
student = Student()
student.get_student_info('Вася', 'Иванов', 'Программирование', '2017' )