class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personinfo(self):
        print(f"name: {self.name}, age: {self.age}, sex: {self.sex}.")

class Student(Person):
    def __init__(self, name, age, sex,college,_class):
        super().__init__(name, age, sex)
        self.college=college
        self._class=_class
    def personinfo(self):
        print(f"name: {self.name}, age: {self.age}, sex: {self.sex}, college: {self.college}, class: {self._class}")
    def __str__(self):
        return f'{self.name},{self.age},{self.sex},{self.college},{self._class}'
