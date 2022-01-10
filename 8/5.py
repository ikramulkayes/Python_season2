class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
class ScienceExam(Exam):
    def __init__(self, marks,time,*args):
        super().__init__(marks)
        self.time = time
        self.sublist = args
    def __str__(self) -> str:
        return f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {len(self.sublist) + 2}"
    def examSyllabus(self):
        sum1 = ""
        for elm in self.sublist:
            sum1 += elm + " , "
        sum1 = sum1.rstrip(" , ")
        return super().examSyllabus()+" , "+  sum1
    def examParts(self):
        sum1 = ""
        count = 3

        for elm in self.sublist:
            sum1 += f"Part {count} - {elm}\n"
            count += 1
        sum1 = sum1.rstrip("\n")
        return super().examParts()+ sum1
    



engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())