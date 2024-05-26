from random import choice 

easylevel = {'Кто живет на новогоднем столе под шубой?': 'селёдка', 
           'Назовите имя парня, который остался дома один и весело провёл время.':'кевин', 
           'Какие смешные вымышленные персонажи помогают Санта Клаусу?': 'эльфы',
           'Какой балет уже давно признан традиционно новогодней постановкой?':'щелкунчик', 
           'Какой волшебный предмет всегда носит Дед Мороз?':'посох', 
           'Что надевают на голову снеговику вместо шапки?':'ведро'
           }


hardlevel = {
             'Какой любимый цвет у Деда Мороза?':'красный',
             'Что находится внутри новогодней хлопушки?':'конфетти',
             'Какой основной символ польского Нового года?':'звезда',
             'В какой стране началась традиция фейерверков?':'китай',
             'Какой город является родиной Снегурочки?':'кострома',
             'Назовите имя самого популярного оленя Санты':'рудольф'
             }

def start_easy_game(scores):
    for key, value in easylevel.items():
        answer = input(f'{key} ').strip().lower()
        if answer == value:
            print('Правильный ответ!')
            scores += 1
        else:
            print('Ответ неправильный')
    return scores

def start_hard_level(scores):
    for key, value in hardlevel.items():
        answer = input(f'{key} ').strip().lower()
        if answer == value:
            print('Правильный ответ!')
            scores += 1
        else:
            question = choice(list(easylevel.keys()))
            answer = input(f'{question} ').strip().lower()
            if answer == easylevel[question]:
                print('Правильный ответ!')
                scores += 0.5
            else:
                print('Ответ неправильный. Попыток больше нет')
    return scores

level = input('Выберите уровень: лёгкий (1) или сложный (2). Укажите число.')
if level == '1':
    scores = start_easy_game(0)
elif level == '2':
    scores = start_hard_level(0)
else:
    print('Вы ошиблись, выберите только 1 или 2')

print(f'Игра окончена! Ваши баллы: {scores}')