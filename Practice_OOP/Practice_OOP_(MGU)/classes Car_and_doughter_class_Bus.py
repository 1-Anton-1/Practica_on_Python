import math
class Car:

    def __init__(self,x,y,direction):
        self.x=x
        self.y=y
        self.direction=direction
        self.dict={'Север':90,'Запад':180,'Юг':270,'Восток':0,'Северо-Восток':45,'Северо-Запад':135,'Юго-Запад':225,'Юго-Восток':315}
        self.angel=self.dict[direction]

    def move(self,distance,direction):
        self.direction = direction
        self.angel = self.dict[direction]
        self.y += distance * math.sin(self.angel * math.pi / 180)
        self.x += distance * math.cos(self.angel * math.pi / 180)

class Bus(Car):
    money = 0
    passengers=0

    def move_to_inside(self,passengers):
        Bus.passengers+=passengers

    def move_to_outside(self,passengers):
        Bus.passengers-=passengers

    def move(self,distance,direction):
        self.direction = direction
        self.angel = self.dict[direction]
        Bus.money=self.money+100*self.passengers*distance//10
        self.y += distance * math.sin(self.angel * math.pi / 180)
        self.x += distance * math.cos(self.angel * math.pi / 180)

    def __str__(self):
        print(f'Автомобиль имеет координаты: ({self.x:.2f};{self.y:.2f})')
        print(f'В каком направлении двигался автомобиль: >{self.direction}<')
        print(f'Количество пассажиров: {self.passengers}')
        print(f'Количество денег: {Bus.money}')

def autopark(car: Bus):
    car.__str__()
    print()
    car.move_to_inside(10)
    car.__str__()
    print()
    car.move(100,'Юг')
    car.__str__()
autopark(Bus(0,0,'Север'))