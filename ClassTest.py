class Mithilesh:
    fat = 30
    def __init__(self):
        self.name = 'Mithilesh'
        self.som = 0

    def printName(self):
        print(self.som)

mi = Mithilesh()
print(Mithilesh.fat) # output 30
print(Mithilesh.name) #Error as it is an object variable
mi.fat+=1  #update mi.fat by 1 but not the class variable
print(mi.fat)   #print 31
m2 = Mithilesh()
print(Mithilesh.fat) #print 30
Mithilesh.fat+=1  #update the class variable by 1
print(Mithilesh.fat) #print 31
m3 = Mithilesh()
print(m3.fat)  #since class variable is updated to 31 , so it will be assigned 31