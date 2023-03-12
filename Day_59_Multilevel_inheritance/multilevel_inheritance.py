class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    pass


class chicken(Bird):  # this may lead to inheritance abuse
    pass



# one or two level of inheritance is more than fine.
# going beyond than that may lead to unneccessary complexity. so avoid this.