class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    # setter functions
    def setAddress(self, address):
        self.__address = address

    # getter functions
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    # return the information in form of a string
    def __str__(self):
        return f'Name: {self.getName()} \nAddress: {self.getAddress()}'


class Student(Person):
    def __init__(self, name, address, numCourses=0):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = []
        self.__grades = []
        self.AverageGrade()

    def AddCourse(self, course):
        self.__courses.append(course)

    def AddCourseGrade(self, grade):
        self.__grades.append(grade)

    def getCourses(self):
        return self.__courses

    def getGrades(self):
        return self.__grades

    def getNumCourses(self):
        return self.__numCourses

    def getCourseAndGrade(self):
        AllCourses = {}
        for i in range(0, len(self.__grades)):
            AllCourses[self.getCourses()[i]] = self.getGrades()[i]
        return AllCourses

    def AverageGrade(self):
        total = 0
        for i in range(0, len(self.__grades)):
            total = total + self.__grades[i]
        return total / self.__numCourses

    def __str__(self):
        return f'Student: \nName: {self.getName()} \nAddress: {self.getAddress()}' \
               f'\nnumber of courses: {self.getNumCourses()} \nSummary: ' \
               f'{self.getCourseAndGrade()} \n' \
               f'Average: {self.AverageGrade()}'


# Example
s = Student('Arish', 'Antananarivo', 3)
s.AddCourse('Math')
s.AddCourseGrade(90)
s.AddCourse('History')
s.AddCourseGrade(85)
s.AddCourse('Programming')
s.AddCourseGrade(101)
print(s.__str__())


class Teacher(Person):
    def __init__(self, name, address, numCourses):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = []

    def AddCourse(self, course):
        if course in self.__courses:
            self.__numCourses -= 1
        else:
            self.__courses.append(course)

    def getNumCourses(self):
        return self.__numCourses

    def getCourses(self):
        return self.__courses

    def __str__(self):
        return f'Teacher: \nName: {self.getName()} \nAddress: {self.getAddress()}' \
               f'\nnumber of courses: {self.getNumCourses()} \nCourses: ' \
               f'{self.getCourses()}'


# Example
t = Teacher('Jude', 'Jakarta', 3)
t.AddCourse('Coding')
t.AddCourse('HCI')
t.AddCourse('Coding')
print(t.__str__())
