class Person:
    name = "Ankit" # we can also create a empty variables
    occupation = "SDE"
    age = 20
    country = ""

    def info(self): # iska matlab wo object jispe ye call ho rha h
        print(f"{self.name} is a {self.occupation}. He lives in {self.country}")


a = Person()
b = Person()
c = Person()


# print(a.age,a.occupation,a.name)
a.info()
a.country = "india"   # we changed or override the default value of country of an object. similarly it can be changed for another object as well.
a.info()


b.name = "Rahul"
b.occupation = "HR"
c.name = "shobhit"
c.occupation = "CEO"


b.info()
c.info()

