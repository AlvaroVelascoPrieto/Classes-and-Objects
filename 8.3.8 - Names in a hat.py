
class Hat():
    def __init__(self, name):
        self.name = name

    def insert_name(self):
        namelist = []
        how_many_names = int(input("How many names do you want to enter? "))
        for i in range(how_many_names):
            newname = input("Enter name: ")
            for i, each in enumerate(namelist):
                if newname != each:
                    namelist = namelist + newname
                else:
                    continue
    
h = Hat(0)
h.insert_name()
