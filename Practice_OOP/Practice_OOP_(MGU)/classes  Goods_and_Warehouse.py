from operator import itemgetter

class Good:
    names_of_product = ['calculator', 'pen', 'pencil', 'rubber', 'notebook', 'office_paper']
    name_of_shope = ["Funny_office_seller", "Funny_office_seller", 'G&g', 'Partners_of_papers','G&g','G&g']
    price_list = [500, 25, 28, 15, 150, 300]

    def __init__(self,i):
        self.i=i
        self.names_of_product[i]=Good.names_of_product[i]
        self.name_of_shope[i]=Good.name_of_shope[i]
        self.price_list[i]=Good.price_list[i]

    def __add__(self, other):
        return f'Сумма цен двух товаров: {self.price_list[self.i]+other.price_list[other.i]}'

    def __str__(self,):
        return f'Товар: {self.names_of_product[self.i]} {self.name_of_shope[self.i]} {self.price_list[self.i]}'

class Waterhouse:
    list_of_product = []
    for i in range(len(Good.names_of_product)):
        list_of_product.append((Good.names_of_product[i]) + ' ' + str(Good.price_list[i]) + ' ' + Good.name_of_shope[i])
        list_of_product[i]=list_of_product[i].split(' ')

    def __init__(self):
        self.list_of_product=Waterhouse.list_of_product

    def __contains__(self, item):
        b=False
        for i in range(len(self.list_of_product)):
            if item in self.list_of_product[i]:
                b = True
                print('Товар есть на складе!')
                print(self.list_of_product[i])
        if b==False:
            print('Товара на складе нет!')

    def sortparam(self,st):
        if st=='names_of_product':
            sorted(self.list_of_product, key=itemgetter(0), reverse=True)
            print('Отсортированный список товаров по параметру: "names_of_product"')
            for i in range(len(self.list_of_product)):
                print(self.list_of_product[i])
        if st=='name_of_shope':
            sorted(self.list_of_product, key=itemgetter(1), reverse=True)
            print('Отсортированный список товаров по параметру: "name_of_shope"')
            for i in range(len(self.list_of_product)):
                print(self.list_of_product[i])
        if st=='price_list':
            sorted(self.list_of_product, key=itemgetter(2), reverse=True)
            print('Отсортированный список товаров по параметру: "price_list"')
            for i in range(len(self.list_of_product)):
                print(self.list_of_product[i])

pr=Waterhouse()
print('Введите номер товара:')
i=int(input())
if 0<=i<len(Waterhouse.list_of_product):
    print(f'Вы выбрали товар: {" ".join(Waterhouse.list_of_product[i])}')
else:
    print(f'Введен некорректный номер товара, введите значение от 0 до {len(Waterhouse.list_of_product)}')

print()
pr.sortparam('names_of_product')
print()
pr1=Good(0)
pr2=Good(5)
print(pr1+pr2)
print(pr1)