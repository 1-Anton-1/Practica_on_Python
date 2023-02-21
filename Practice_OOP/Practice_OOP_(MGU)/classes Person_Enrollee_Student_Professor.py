class Person:
    def __init__(self,second_name,data):
        self.second_name=second_name
        self.data=data

    def age(self):
        return f'Возраст человека, лет: {2023-int(self.data[len(self.data)-4:])}'

    def __str__(self):
        return f'Фамилия: {self.second_name}, дата рождения {self.data}. Возраст, лет {2023-int(self.data[len(self.data)-4:])}'

class Enrollee(Person):
    def __init__(self,second_name,data,faculty):
        super().__init__(second_name,data)
        self.faculty=faculty

    def __str__(self):
        return f'Фамилия: {self.second_name}, дата рождения {self.data}. Возраст, лет {2023-int(self.data[len(self.data)-4:])}. Факультет: {self.faculty}'

class Student(Person):
    def __init__(self,second_name,data,faculty,course):
        super().__init__(second_name,data)
        self.faculty=faculty
        self.course = course

    def __str__(self):
        return f'Фамилия: {self.second_name}, дата рождения {self.data}. Возраст, лет {2023-int(self.data[len(self.data)-4:])}. Факультет: {self.faculty}. Курс: {self.course}'

class Professor(Person):
    def __init__(self,second_name,data,faculty,post, experience):
        super().__init__(second_name,data)
        self.faculty=faculty
        self.post=post
        self.experience=experience

    def __str__(self):
        return f'Фамилия: {self.second_name}, дата рождения {self.data}. Возраст, лет {2023-int(self.data[len(self.data)-4:])}. Факультет: {self.faculty}. Должность: {self.post}. Стаж, лет: {self.experience}'

l=[]
f=[]
human = Person ('Сидоров','01.02.1992')
# print(human)
f.append(human.second_name)
f.append(human.data)
# print(f'{f}')
l.append(f)
f=[]
oleg=Enrollee('Иванов','05.07.1995','Энергомашиностроение')
# print(oleg)
f.append(oleg.second_name)
f.append(oleg.data)
f.append(oleg.faculty)
l.append(f)
f=[]
semen=Student('Слепаков','07.10.1994','Ракетостроение',5)
# print(semen)
f.append(semen.second_name)
f.append(semen.data)
f.append(semen.faculty)
f.append(semen.course)
l.append(f)
f=[]
pavel=Professor('Кашимирский','11.05.1974','Биомедецинские технологии','Доцент','7')
# print(pavel)
f.append(pavel.second_name)
f.append(pavel.data)
f.append(pavel.faculty)
f.append(pavel.post)
f.append(pavel.experience)
l.append(f)
print('-'*50)
print('База содержит:')
# l.append(pavel)
for i in range(len(l)):
    print(l[i])
print('Введите начало возрастного диапазона:')
a=int(input())
print('Введите конец возрастного диапазона:')
b=int(input())
for i in range(len(l)):
    if a<=2023-int(l[i][1][len(l[i][1]) - 4:])<=b:
        print(f'{l[i]}, возраст: {2023-int(l[i][1][len(l[i][1]) - 4:])}')
# print(human.age())

