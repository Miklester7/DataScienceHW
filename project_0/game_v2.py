"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    predict_current = np.random.randint(1, 101)

    predict_max = 101
    predict_min = 0

    count = 1

    while True:
        if predict_current == number:
            break  # Выход из цикла если угадали

        # Уменьшаем диапазон при каждом шаге
        predict_current = (predict_min + predict_max) // 2
        count += 1

        if predict_current > number:
            predict_max = predict_current - 1
        else:
            predict_min = predict_current + 1
    return count


def game_score(random_predict) -> int:
    """Расчёт среднего кол-ва попыток угадывания числа за 1000 итераций

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: Среднее кол-во попыток
    """

    count_ls = list()
    np.random.seed(1)  # фиксируем для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает числов в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    game_score(random_predict)
