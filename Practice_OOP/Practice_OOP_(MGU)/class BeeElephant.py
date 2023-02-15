class BeeElephant:
    def __init__(self,bee,elephant):
        self.bee=bee
        self.elephant=elephant

    def fly(self):
        return True if self.bee>=self.elephant else False

    def trumpet(self):
        return 'tu-tu-doo-doo!' if self.elephant>=self.bee else 'wzzzzz'

    def eat(self,meal,value):
        if meal=='grass':
            self.bee-=value
            self.elephant+=value
            if self.bee<0:
                self.bee=0
            if self.elephant>100:
                self.elephant=100
        if meal=='nectar':
            self.bee+=value
            self.elephant-=value
            if self.bee>100:
                self.bee=100
            if self.elephant<0:
                self.elephant=0
    def get_parts(self):
        return f'({self.bee},{self.elephant})'

# be=BeeElephant(3,2)
# print(be.fly())
# print(be.trumpet())
# be.eat('grass',4)
# print(be.get_parts())
be=BeeElephant(13,87)
print(be.fly())
print(be.trumpet())
be.eat('nectar',90)
print(be.get_parts())