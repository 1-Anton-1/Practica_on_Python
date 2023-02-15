class GoodIfrit:
    def __init__(self,height,name,goodness):
        self.height=height
        self.name=name
        self.goodness=goodness

    def change_goodness(self,value):
        self.goodness += value
        if self.goodness<0:
            self.goodness=0
        # return self.goodness

    def __add__(self, other):
        self.height+=other
        return GoodIfrit(self.height,self.name,self.goodness)

    def __call__(self, value):
        return f'{value*self.goodness//self.height}'

    def __str__(self):
        return f'Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}'


gi=GoodIfrit(80,'Hazrul',3)
gi.change_goodness(4)
print(gi)
gi1=gi+15
print(gi1)
print(gi(31))