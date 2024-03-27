class Course:
    def __init__(self, course_name):
        """
        Initialize a Course object with a given course name and a default grade of 101.

        Args:
        course_name (str): The name of the course.
        """
        self.course_name = course_name
        self.grade = 101

    def setGrade(self, Sgrade):
        """
        Set the grade for the course, ensuring it falls within a valid range (0-100).

        Args:
        Sgrade (float): The grade to be set for the course.
        """
        Sgrade = float(Sgrade)
        if Sgrade > 100 or Sgrade < 0:
            print("grade is not valid must be between 0-100\n")
            return
        self.grade = float(Sgrade)

    def getGrades(self):
        """
        Retrieve the grade for the course.

        Returns:
        int: The grade of the course.
        """
        return self.grade


class Student:
    def __init__(self, student_name, student_id):
        """
        Initialize a Student object with a given name, ID, and an empty list of courses.

        Args:
        student_name (str): The name of the student.
        student_id (str): The ID of the student.
        """
        self.student_name = student_name
        self.__student_id = student_id
        self.student_Courses = []

    def getID(self):
        """
        Retrieve the ID of the student.

        Returns:
        str: The ID of the student.
        """
        return self.__student_id

    def Dupliacted_courses(self, Course, added_course):
        """
        Check for duplicate courses and update the grade if a duplicate is found.

        Args:
        Course (Course): An existing course.
        added_course (Course): The course to be added.

        Returns:
        bool: True if a duplicate course is found and its grade is updated, False otherwise.
        """
        if Course.course_name == added_course.course_name:
            Course.setGrade(added_course.grade)
            return True

    def getStudentName(self):
        """
        Retrieve the name of the student.

        Returns:
        str: The name of the student.
        """
        return self.student_name

    def addCourse(self, Course):
        """
        Add a course to the student's list of courses, checking for duplicates and valid grades.

        Args:
        Course (Course): The course to be added.
        """
        if Course.grade > 100 or Course.grade < 0:
            print(
                f"The grade of Course {Course.course_name} must be between 0-100 so the course dose not added to list\n")
            return
        for i in range(0, len(self.student_Courses)):
            if self.Dupliacted_courses(self.student_Courses[i], Course):
                return
        self.student_Courses.append(Course)

    def AvrOfCourses(self):
        """
        Calculate and print the average grade of all courses taken by the student.
        """
        sums = list(map(lambda x: x.getGrades(), self.student_Courses))
        return (f"student id is: {self.__student_id} and the average is {float(sum(sums) / float(len(sums)))}")

    def getCourseGrade(self, CourseName):
        """
        Retrieve the grade for a specific course taken by the student.

        Args:
        CourseName (str): The name of the course.

        Returns:
        int: The grade of the specified course, or -1 if the course is not found.
        """
        CourseGrade = list(
            filter(lambda x: x.getGrades if x.course_name == CourseName else False, self.student_Courses))
        if not CourseGrade:
            return -1
        return CourseGrade[0].getGrades()

    def AvrOfAllstudents(self):
        """
        Calculate the average grade of all courses for the student.

        Returns:
        str: A string containing the student's ID and their average grade.
        """
        sums = list(map(lambda x: x.getGrades(), self.student_Courses))
        return f"{self.__student_id}  {float(sum(sums) / float(len(sums)))}"


def inputFromFile(filename):
    """
    Read student data from a file and create a list of Student objects.

    Args:
    filename (str): The name of the file containing student data.

    Returns:
    list: A list of Student objects.
    """
    student_list = []

    with open(filename, "r") as file:
        char = file.read(0)
        for line in file:
            counter = 0
            counter2 = 0
            word = ""
            S_name = ""
            Course_Name = ""
            i = 0
            for char in line:
                word += char
                if char == "\t":
                    if counter == 0:
                        word = word[:-1]
                        S_name = word
                        if not S_name:
                            print(f"a problem was accorded please check your file ")
                            return False
                        counter += 1
                        word = ""
                    elif counter == 1:
                        word = word[:-1]
                        S_id = word
                        if not S_id:
                            print("a problem was accorded please check your file")
                            return False
                        word = ""
                        counter += 1
                        student = Student(S_name, S_id)
                if counter == 2:
                    if char == "#" or char == ";" or i + 1 == len(line):
                        if counter2 == 0 :
                            word = word[:-1]
                            Course_Name = word
                            if not Course_Name:
                                print("a problem was accorded please check your file")
                                return False
                            counter2 += 1
                            word = ""
                        elif counter2 == 1 :
                            if i + 1 != len(line):
                                word = word[:-1]
                            Course_grade = word
                            if not Course_grade:
                                print("a problem was accorded please check your file")
                                return False
                            word = ""
                            course = Course(Course_Name)
                            course.setGrade(Course_grade)
                            student.addCourse(course)
                            counter2 = 0
                if i + 1 == len(line):
                    student_list.append(student)
                i += 1
    file.close()
    return student_list


def studentAvr(S_list, name):
    """
    Calculate and print the average grade of courses for a particular student.

    Args:
    S_list (list): A list of Student objects.
    name (str): The name of the student.
    """
    names = list(map(lambda student_name: student_name.getStudentName(), S_list))
    StudentName = list(filter(lambda student_name: student_name.getStudentName() == name, S_list))

    if len(StudentName) <= 0:
        print(f"student {name} was not found\n")
        return
    names = list(filter(lambda x: x if x.getStudentName() == name else False, S_list))
    print(names[0].getStudentName())
    N=list(map(lambda x :x.AvrOfCourses(),names))
    print(N)


def CourseAvr(S_list, c_name):
    """
    Calculate and print the average grade of a specific course across all students.

    Args:
    S_list (list): A list of Student objects.
    c_name (str): The name of the course.
    """
    CourseGrades = list(filter(lambda grade: 0 <= grade <= 100, map(lambda x: x.getCourseGrade(c_name), S_list)))
    if len(CourseGrades) == 0:
        print(f"Not Grades found for {c_name} Course")
        return
    print(f"The average of course {c_name} is: {sum(CourseGrades) / len(CourseGrades)}\n")


def AverageOfStudents(S_list, filename):
    """
    Calculate the average grade of all courses for each student and write it to a file.

    Args:
    S_list (list): A list of Student objects.
    filename (str): The name of the file to write the results to.
    """
    with open(filename, 'w') as file:
        listOfStudentAvr = list(map(lambda x: str(x.AvrOfAllstudents()), S_list))
        line = map(lambda x: x + '\n', listOfStudentAvr)
        file.writelines(line)
    file.close()


def MainMenu(S_list):
    """
    Display the main menu and handle user choices.

    Args:
    S_list (list): A list of Student objects.
    """
    while True:
        print("Choose your option\n"
              "1.Calculate the average of a particular student\n"
              "2.Calculation of the average in a certain course\n"
              "3.Average of all students\n"
              "4.Exit")
        choice = int(input("Enter your choice: \n"))
        if choice == 1:
            name = input("choose a name of a student: \n")
            studentAvr(S_list, name)
        elif choice == 2:
            course_name = input("choose a name of a course: \n")
            CourseAvr(S_list, course_name)
        elif choice == 3:
            file = input("please enter file name to output to:\n")
            AverageOfStudents(S_list, file)
            pass
        elif choice == 4:
            print("Goodbye")
            return
        else:
            print("invalid choice\n")


if __name__ == '__main__':
    student_list = []
    flag = True
    try:
        file = input("please enter file name:\n")
        student_list = inputFromFile(file)
    except:
        flag = False
    if not flag:
        print("FILE PATH IS NOT VALID\n")
    elif len(student_list) == 0:
        print("list of students is empty\n")
    elif flag == True:
        print("student added to the student list successfully")
        MainMenu(student_list)
