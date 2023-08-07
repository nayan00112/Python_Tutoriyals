class Univercity:
    univercityName = "ABCD Univercity"

    def AddStd(self):
        print("Collages can add students...")
    
    def Sylabus(self):
        print("Sylabus of Univercity")

    def usefulDocuments(self):
        print("useful materials for students can access.")

class Collage (Univercity):
    collageName = "PQRS Collage"
    def AddStd(self):
        print("Adding students...")
    
    def Students(self):
        print("Hello Students.!!!")

c = Collage()
c.AddStd()
c.Students()
print(c.univercityName)
print(c.collageName)
c.usefulDocuments()


# Output:
# Adding students...
# Hello Students.!!!
# ABCD Univercity
# PQRS Collage
# useful materials for students can access.