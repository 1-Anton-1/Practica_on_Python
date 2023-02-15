import datetime
now=datetime.datetime.now()

class Post:
    def __init__(self,nickname,count_likes,message:str,feedback:list):
        self.nickname=nickname
        self.time_post=now.strftime("%d-%m-%Y %H:%M")
        self.count_likes=count_likes
        self.message = message
        for i in ['гнусные','Умрите']:
            self.message=self.message.replace(i,'0')
        self.feedback=[[i] for i in feedback]

    def __str__(self):
        print(f'Имя пользователя: {self.nickname},\n время публикации: {self.time_post},\n количество лайков: {self.count_likes},\n текст сообщения: {self.message}')
        print('Комментарии:')
        for i in range(len(self.feedback)):
            print(f'{self.feedback[i]}')

    def like(self):
        self.count_likes+=1

user_5464572154=Post('aRgOn-777!',15,'Черви - гнусные существа! Умрите!', ['Лох','Fuck','Автор живодёр!','Поддерживаю','лайк'])
user_5464572154.__str__()
user_5464572154.like()
user_5464572154.__str__()