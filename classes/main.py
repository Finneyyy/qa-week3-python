class Person():
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age
        
obj1=Person("Tim",23)
obj2=Person("Dave",24)
obj3=Person("Tam",18)

print(obj1,obj2,obj3)