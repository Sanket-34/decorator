class person:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.Iname = lname
        self.age   = age

    #getter and setter
    def getfname(self):
        return self.fname

    def setfname(self, newfname):
        self.fname = newfname

    def getlname(self):
        return self.lname

    def setIname(self, newlname):
        self.lname = newlname

    def getage(self):
        return self.age
    
    def setage(self, newage):
        self.age = newage

    