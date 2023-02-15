class Talking:
    def __init__(self, name):
        self.name=name
        self.number_answer=0
        self.yes=0
        self.no=0

    def to_answer(self):
        if self.number_answer%2==0:
            self.number_answer+=1
            self.yes+=1
            return 'moore-moore'
        else:
            self.number_answer+=1
            self.no+=1
            return 'meow-meow'

    def number_yes(self):
        return self.yes

    def number_no(self):
        return self.no

# tk=Talking('Pussy')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
tk=Talking('Pussy')
tk1=Talking('Barsik')
print(tk.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no" {tk1.number_no()} times')