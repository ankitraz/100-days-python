class ParentClass:


    def parent_method(self):
        print("This is the parent method.")



class ChildClass(ParentClass):


    def child_method(self):
        print("This is the child method.")
        super().parent_method()

    def parent_method(self):
        print("This is the parent method form child class. Now calling parent method.")
        super().parent_method()




child_object = ChildClass()
child_object.child_method()
child_object.parent_method()