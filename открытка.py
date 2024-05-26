from tkinter import *
from random import randint
# создаем окно
window = Tk()
window.geometry('600x600')
# создаем холст и помещаем на окно
canvas = Canvas(window, width=600, height=600)
canvas.pack()
bg_photo = PhotoImage(file='forest.png')
# создаем класс рыцаря - одного из наших персонажей 
class Santa:
    # создаем атрибуты: внешний фид (картинка), координаты по x, y, v (рыцарь стоит у левой вертикальной границы, в центре и без движения - скорость равна 0)
    def __init__(self):
        self.photo = PhotoImage(file='santa.png')
        self.x = 100
        self.y = 500
        self.v = 0
    # создаем методы движения: вверх, вниз и остановка 
    ## self - параметр события, наше событие - клавиши, которые нажимают пользователи 
    def left(self, event):
        # если рыцарь движется вверх, то y уменьшается, получается скорость будет отрицательной
        self.v = -10
    
    def right(self, event):
        # если рыцарь движется вниз, то y увеличивается, получается скорость будет положительной
        self.v = 10
    
    def stop(self, event):
        # во время остановки скорость равна 0
        self.v = 0
# создаем класс дракона- одного из наших персонажей 
class Ball:
    def __init__(self):
        self.photo = PhotoImage(file='snowball.png')
        self.x = randint(15, 620)
        self.y = randint(10, 150)
        self.ball = None
# создаем рыцаря и трех драконов 
santa = Santa()
list_1 = []
for i in range(randint(25, 50)):
    list_1.append(Ball())

# создаем функцию игры 
def game():
    # при каждой отрисовке удаляем все с холста, чтобы добавить все заново
    canvas.delete('all')
    # добавляем фон
    canvas.create_image(300, 300, image=bg_photo)
    # добавляем изображения рыцаря по координатам
    canvas.create_image(santa.x, santa.y, image=santa.photo)
    # указываем движения рыцаря - прибавляем к y скорость (если отрицательная, y уменьшается, идем вверх и наоборот)
    santa.x += santa.v
    # чтобы функция постоянно запускалась и происходила отрисовка, используем метод after, который откладывает запуск функцию на 5 миллимиллисекунд

    for i in list_1:
        canvas.create_image(i.x, i.y, image=i.photo)
        i.y += 1
    canvas.create_text(300, 50, text='С Новым Годом! Успехов в обучении!', fill='red', font=('Georgia', 20, 'bold'))
    window.after(5, game)


# вызываем функцию
game()

# связываем метод движения рыцаря и клавишу на клавиатуре
window.bind('<Key-Left>', santa.left)
window.bind('<Key-Right>', santa.right)
window.bind('<KeyRelease>', santa.stop)

window.mainloop()