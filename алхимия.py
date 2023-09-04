from tkinter import *
from random import randint
window = Tk()
window.geometry('600x600')
window.title('Игра: Алхимия')
canvas = Canvas(window, width=600, height=600)
canvas.pack()

# создаем классы элементов с одним атрибутом - картинкой 
class Clay:
    image = PhotoImage(file='free-icon-pottery-7942410.png').subsample(4,4)

class Aroma:
    image = PhotoImage(file='aroma.png').subsample(4,4)

class Fire:
    image = PhotoImage(file='free-icon-fire-9509865.png').subsample(4,4)
    # складываем огонь и землю, чтобы получить глину (возвращаем этот класс)
    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay

class Water:
    image = PhotoImage(file='free-icon-water-drop-4246703.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Wind):
            return Aroma

class Wind:
    image = PhotoImage(file='wind.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Water):
            return Aroma

class Earth:
    image = PhotoImage(file='ground.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

# отрисовываем на окне наши элементы - картинки
elements = [Water(), Fire(), Wind(), Earth()]
for elem in elements:
    elem = canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)


def move(event):
    # получаем номер объекта, который попал в область курсора
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    # получаем номера двух объектов, а затем - по индексам ищем их в списке и складываем 
    if len(images_id) == 2:
        elem_id_1, elem_id_2 = images_id[0], images_id[1]
        element_1 = elements[elem_id_1 - 1]
        element_2 = elements[elem_id_2 - 1]

        new_element = element_1 + element_2
        # добавляем новый элемент в список, чтобы не было его повторного создания 
        if new_element not in elements:
            # отрисовывыаем на окне новый элемент
            canvas.create_image(event.x, event.y, image=new_element.image)
            elements.append(new_element)
    # перемещаем картинки вслед за курсором 
    canvas.coords(images_id, event.x, event.y)
# биндим левую кнопку мыши для передвижения картинок
window.bind('<B1-Motion>', move)

window.mainloop()