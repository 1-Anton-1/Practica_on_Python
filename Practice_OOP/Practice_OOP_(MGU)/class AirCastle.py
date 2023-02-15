class AirCastle:
    def __init__(self,height,count_clouds,colour):
        self.height=height
        self.count_clouds=count_clouds
        self.colour=colour

    def get_var_name(self):
        for k,v in globals().items():
            if v is self:
                return k

    def name(self):
        return {self.get_var_name()}

    def change_height(self,value):
        self.height-=value
        if self.height<0:
            self.height=0

    def __add__(self, other):
        self.count_clouds+=other
        self.height+=other//5
        # return

    def transparency(self,transpar):
        return self.height//(transpar*self.count_clouds)

    def __str__(self):
        return f'The AirCasle at an altitude of {self.height} with {self.count_clouds} clouds'

    def __gt__(self, other):
        if self.count_clouds>other.count_clouds:
            return f'больше по количеству облаков чем'
        else:
            if self.height>other.height:
                return f'больше по высоте чем'
            else:
                if self.colour>other.colour:
                    return f'больше по цвету чем'

    def __lt__(self, other):
        if self.count_clouds<other.count_clouds:
            return f'меньше по количеству облаков чем'
        else:
            if self.height<other.height:
                return f'меньше по высоте чем'
            else:
                if self.colour < other.colour:
                    return f'меньше по цвету чем'

    def __ge__(self, other):
        if self.count_clouds>=other.count_clouds:
            return f'не меньше по количеству облаков чем'
        else:
            if self.height>=other.height:
                return f'не меньше по высоте чем'
            else:
                if self.colour>=other.colour:
                    return f'не меньше по цвету чем'


    def __le__(self, other):
        if self.count_clouds<other.count_clouds:
            return f'не больше по количеству облаков чем'
        else:
            if self.height<other.height:
                return f'не больше по высоте чем'
            else:
                if self.colour < other.colour:
                    return f'не больше по цвету чем'

    def __eq__(self, other):
        if self.count_clouds==other.count_clouds:
            return f'равно по количеству облаков'
        else:
            if self.height==other.height:
                return f'равно по высоте'
            else:
                if self.colour==other.colour:
                    return f'равно по цвету '

    def __ne__(self, other):
        if self.count_clouds!=other.count_clouds:
            return f'не равно по количеству облаков'
        else:
            if self.height!=other.height:
                return f'не равно по высоте'
            else:
                if self.colour!=other.colour:
                    return f'не равно по цвету '

elisium=AirCastle(52,3,'Blue')
# elisium.change_height(10)
# elisium+5
# print(elisium.transparency(3))
# print(elisium.__str__())
acropol=AirCastle(51,4,'Red')
print(f'{elisium.name()} {elisium!=acropol} {acropol.name()}')