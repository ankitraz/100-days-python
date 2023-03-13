class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer,Swimmer):
    pass



# there is also an ambiguity that if both flyer class and swimmer class same method then 
# which of the method is going to inherited to flying fish class? 
