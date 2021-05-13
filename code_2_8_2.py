class Human:
    def __init__(self, name, age, favorite_lesson):
        self.name = name
        self.age = age
        self.favorite_lesson = favorite_lesson


class Teacher(Human):
    def __init__(self, name, age, specialty, salary, favorite_lesson):
        super().__init__(name, age, favorite_lesson)
        self.specialty = specialty
        self.salary = salary


class Student(Human):
    def __init__(self, name, age, grade, favorite_lesson):
        super().__init__(name, age, favorite_lesson)
        self.grade = grade

teacher_1 = Teacher('John', 32, 'Programmer', 35000, 'Programming')
student_1 = Student('Nick', 20, 5.0, 'Mathematics')

# Я перенес свойство favorite_lesson потому, что это свойство повторялось у обоих подклассов)
