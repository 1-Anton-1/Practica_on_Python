class Client:
    def __init__(self,id,full_name,data_of_opening,size_of_deposit,percent):
        self.id=id
        self.full_name=full_name
        self.data_of_opening=data_of_opening
        self.size_of_deposit=size_of_deposit
        self.percent=percent

class Bank:
    def __init__(self):
        self.clientBase=[]

    def addClient(self,other):
        l=[]
        l.append(other.id)
        l.append(other.full_name)
        l.append(other.data_of_opening)
        l.append(other.size_of_deposit)
        l.append(other.percent)
        self.clientBase.append(l)

    def showByMoney(self,money):
        b = False
        for i in range(len(self.clientBase)):
            if self.clientBase[i][3]>money:
                print(f'{self.clientBase[i]}')
                b = True
        if b == False:
            print(f'Нет клиентов с вкладом больше чем {money}')

    def showByCode(self,cod):
        b=False
        for i in range(len(self.clientBase)):
            if self.clientBase[i][0]==cod:
                print(f'{self.clientBase[i]}')
                b=True
        if b==False:
            print(f'Нет клиента с id {cod}')

    def showByProc(self,proc):
        b=False
        for i in range(len(self.clientBase)):
            if self.clientBase[i][4]>proc:
                print(f'{self.clientBase[i]}')
                b=True
        if b==False:
            print(f'Нет клиентов с процентной ставкой больше чем {proc}')

    def __str__(self):
        for i in range(len(self.clientBase)):
            print(f'{self.clientBase[i]}')

user_01=Client(2345932,'Петров Семен Григорьевич','01-12-2022',100_000,5)
user_02=Client(2345567,'Антипов Илья Петрович','14-12-2022',200_000,7)
user_03=Client(2312454,'Семенов Денис Сергеевич','04-03-2020',375_000,8.5)
user_04=Client(2312111,'Денисова Дарья Александровна','04-02-2021',54_000,5.5)
user_05=Client(2312134,'Зубарева Марина Алексеевна','01-04-2019',115_500,6)
b=Bank()
b.addClient(user_01)
b.addClient(user_02)
b.addClient(user_03)
b.addClient(user_04)
b.addClient(user_05)
b.__str__()
print()
b.showByMoney(500_000)
print()
b.showByCode(2312134)
print()
b.showByProc(6)
