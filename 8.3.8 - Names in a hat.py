
class Hat():
    def __init__(self, name):
        self.name = name

    def insert_name(self):
        global namelist
        namelist = []
        how_many_names = int(input("How many names do you want to enter? "))
        for i in range(how_many_names):
            newname = input("Enter name: ")
            if len(namelist)==0:
                namelist.append(newname)
            else:
                for i, each in enumerate(namelist):
                    if newname != each:
                        namelist.append(newname)
                        break
                    else:
                        continue

    def __repr__(self, namelist):
        print("The hat contains the following names: " + str(namelist))

h = Hat(0)
h.insert_name()
h.__repr__(namelist)