import random
from time import sleep

answers = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно",
]
print("Привет, Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Как тебя зовут? ")
print("Привет, ", name)
do_want = "да"
while do_want.lower() == "да":
    question = input('Введите вопрос, на которые можно ответить "да" или "нет": ')
    sleep(2)
    print(random.choice(answers))
    do_want = input(
        'Хочешь задать еще один вопрос? Напиши "да", если хочешь, или введи любое другое слово, если не хочешь:'
    )
if do_want.lower() != "да":
    print("Возвращайся, если возникнут вопросы!")