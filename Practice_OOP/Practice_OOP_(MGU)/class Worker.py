class Worker:
    def __init__(self,name: str,post: str,experience: int):
        self.name=name
        self.post=post
        self.experience=experience

    def print_info(self):
        print(f'Имя: {self.name}')
        print(f'Должность: {self.post}')
        if self.experience<5:
            print(f'Стаж: {self.experience} года')
        else:
            print(f'Стаж: {self.experience} лет')

worker1=Worker('Алексей', 'Программист', 17)
worker1.print_info()
print()
worker2=Worker('Анна', 'Маркетолог', 2)
worker2.print_info()
print()
worker3=Worker('Дмитрий', 'Аналитик', 1)
worker3.print_info()
print()