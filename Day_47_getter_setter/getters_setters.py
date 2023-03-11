class MyClass:
    def __init__(self,value) -> None:
        self._value = value

    @property
    def value_name(self):
        print("Getting value...")
        return self._value
    

    @value_name.setter    # by adding property wrapper on value_name getter, it provides setter and other property methods automatically
    def value_name(self, val):
        self._value = val



obj = MyClass(10)
print(obj.value_name)  # getting value 

obj.value_name = 34     # setting value
print(obj.value_name) 
