# Проект FitLife - MVP версия 1.0
from constants import THE_CUTOFF, WATER_PER_KG

# Запрашиваем данные пользователя
user_name = (input("Как Вас зовут?  ")).strip().title()
print(f"Добрый день, {user_name}!")
while True:
    user_age_in = input("Сколько Вам полных лет?  ")
    try:
        user_age = int(user_age_in)
        if user_age <= 0:
            print('Возраст должен быть больше 0. Попробуйте еще раз.')
            continue
        break
    except ValueError:
        print('Пожалуйста, введите корректное число.')


while True:
    user_weight_in = input("Укажите Ваш вес (в кг): ").strip()
    user_weight_optim = user_weight_in.replace(',', '.')
    try:
        user_weight = float(user_weight_optim)
        break
    except ValueError:
        print('Пожалуйста, введите корректный вес (число).')


while True:
    user_height_in = input("Укажите Ваш рост (в м): ").strip()
    user_height_optim = user_height_in.replace(',', '.')
    try:
        user_height = float(user_height_optim)
        break
    except ValueError:
        print('Пожалуйста, введите корректный рост (число).')


# Вычисляем ИМТ и норму воды
bmi = user_weight / user_height ** 2
water_needed_l = user_weight * WATER_PER_KG


"""Условие для правильного отображения "л." или "г."
при выводе возраста в отчет"""
user_age_str = str(user_age)
if len(user_age_str) == 1:
    if 0 < int(user_age_str[0]) < 5:
        year_letter = "г."
    else:
        year_letter = "л."
else:
    if 10 <= int(user_age_str) <= 19:
        year_letter = "л."
    elif 0 < int(user_age_str[1]) < 5:
        year_letter = "г."
    else:
        year_letter = "л."


# Создаем отчет содержащий возраст, ИМТ (округленный до 1 знака) и норму воды.
report_text = (
    f'{THE_CUTOFF}\n'
    f"{THE_CUTOFF}\n"
    f"Отчёт для пользователя: {user_name} ({user_age} {year_letter})\n"
    f"{THE_CUTOFF}\n"
    f"Ваш Индекс Массы Тела: {round(bmi, 1)}\n"
    f"Рекомендованная норма воды: {round(water_needed_l, 1)} л. в день\n"
    f"{THE_CUTOFF}\n"
    f"Расчёт окончен. Будьте здоровы!"
)


print(report_text)
