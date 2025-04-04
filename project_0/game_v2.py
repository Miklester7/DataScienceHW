"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1

        predict_number = np.random.randint(1, 101)  # Предполагаемое число
        if number == predict_number:
            break  # Выход из цикла если угадали

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
