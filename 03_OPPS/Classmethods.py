class student:
    collage_name = "UEM"
    def showCollage(self):
        print(f"The collage name is {self.collage_name}")

    @classmethod
    def changeName(self,newName):
        self.collage_name = newName


s1 = student()
s1.showCollage()
s1.changeName("IEM")
s1.showCollage()
print(student.collage_name)