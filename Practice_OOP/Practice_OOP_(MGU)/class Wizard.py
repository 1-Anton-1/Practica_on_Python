class Wizard:
    def __init__(self,name,rating,age):
        self.name=name
        self.rating=rating
        self.age=age

    def change_rating(self,value):
        self.rating+=value
        if self.rating>100:
            self.rating=100
        if self.rating<1:
            self.rating=1
        if value>0:
            self.age = self.age-abs(value)//10
            if self.age<18:
                self.age=18
        if value<0:
            self.age = self.age+abs(value)//10
            if self.age<18:
                self.age=18
    def __str__(self):
        return f'Wizard {self.name} with {self.rating} rating looks {self.age} years old'

    def __iadd__(self, other:str):
        self.rating+=len(other)
        if self.rating>100:
            self.rating=100
        if self.rating<1:
            self.rating=1
        self.age = self.age-len(other)//10
        if self.age<18:
            self.age=18

    def __call__(self,args):
        return (args-self.age)*self.rating

    def __gt__(self,other):
        if self.rating>other.rating:
            return f'больше по рейтингу чем'
        else:
            if self.age>other.age:
                return f'больше по возрасту чем'
            else:
                if self.name>other.name:
                    return f'больше по имени чем'

    def __lt__(self,other):
        if self.rating<other.rating:
            return f'меньше по рейтингу чем'
        else:
            if self.age<other.age:
                return f'меньше по возрасту чем'
            else:
                if self.name<other.name:
                    return f'меньше по имени чем'

    def __ge__(self,other):
        if self.rating>=other.rating:
            return f'не меньше по рейтингу чем'
        else:
            if self.age>=other.age:
                return f'не меньше по возрасту чем'
            else:
                if self.name>=other.name:
                    return f'не меньше по имени чем'


    def __le__(self,other):
        if self.rating<=other.rating:
            return f'не больше по рейтингу чем'
        else:
            if self.age<=other.age:
                return f'не больше по возрасту чем'
            else:
                if self.name<=other.name:
                    return f'не больше по имени чем'

    def __eq__(self,other):
        if self.rating==other.rating:
            return f'равно по рейтингу'
        else:
            if self.age==other.age:
                return f'равно по возрасту'
            else:
                if self.name==other.name:
                    return f'равно по имени'

    def __ne__(self,other):
        if self.rating!=other.rating:
            return f'не равен по рейтингу'
        else:
            if self.age!=other.age:
                return f'не равен по возрасту'
            else:
                if self.name!=other.name:
                    return f'не равен по имени'

gendalf=Wizard('Gendalf',15,50)
saruman=Wizard('Saruman',15,50)
# print(gendalf)
# gendalf.change_rating(-100)
# print(gendalf)
# print(gendalf(45))
print(gendalf!=saruman)