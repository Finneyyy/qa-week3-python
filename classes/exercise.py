class Students():
    def __init__(self, name, age, class_):
        self.name=name
        self.age=age
        self.class_="student"
    
    def score():
        score1=int(input("Enter first score: "))
        score2=int(input("Enter second score: "))
        score3=int(input("Enter third score: "))
        averageScore=(score1+score2+score3)/3
        return int(averageScore)
        

print(Students.score())