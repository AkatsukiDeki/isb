import hashlib
import multiprocessing as mp
import time
import work_to_file

from matplotlib import pyplot as plt
from tqdm import tqdm


def check_card_number(part: int, bins: list, last_digit: int, original_hash: str) -> str:
    """
    Проверяет, может ли данная часть номера карты быть полным номером карты.

    Параметры:
        part: Часть номера карты для проверки.
        bins: Список возможных префиксов номеров карт (BIN).
        last_digit: Последняя цифра номера карты.
        original_hash: Хеш-значение полного номера карты, для которого нужно найти совпадение.
    Возвращает:
        Полный номер карты
    """
    for card_bin in bins:
        card_number = f"{card_bin}{str(part).zfill(6)}{last_digit}"
        if hashlib.md5(card_number.encode()).hexdigest() == original_hash:
            return card_number


def get_card_number(original_hash: str, bins: list, last_digit: int, count_process: int = mp.cpu_count()) -> str:
    """
    Находит полный номер карты, проверяя все возможные комбинации заданных параметров.

    Параметры:
        original_hash: Хеш-значение полного номера карты, для которого нужно найти совпадение.
        bins: Список возможных префиксов номеров карт (BIN).
        last_digit: Последняя цифра номера карты.
        count_process: Количество процессов для поиска. По умолчанию равно количеству доступных ЦП.
    Возвращает:
        Полный номер карты
    """
    with mp.Pool(count_process) as p:
        for result in p.starmap(check_card_number,
                                [(i, bins, last_digit, original_hash) for i in list(range(0, 999999))]):
            if result:
                print(f"Номер выбранной карты с использованием количества процессов = {count_process} : {result}")
                p.terminate()
                return result


def luhn_algorithm(card_number: str) -> bool:
    """
    Проверяет достоверность номера кредитной карты с использованием алгоритма Луна.

    Параметры:
        card_number: Номер кредитной карты для проверки.
    Возвращает:
        True, если номер карты действителен, False в противном случае.
    """
    digits = [int(digit) for digit in reversed(card_number)]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] = (digits[i] // 10) + (digits[i] % 10)
    return sum(digits) % 10 == 0


def graphing(original_hash: str, bins: list, last_digit: int) -> None:
    """
    Строит график времени выполнения функции `get_card_number` в зависимости от количества использованных процессов.

    Параметры:
        original_hash: Хеш-значение полного номера карты, для которого нужно найти совпадение.
        bins: Список возможных префиксов номеров карт (BIN).
        last_digit: Последняя цифра номера карты.
    """
    time_list = list()
    for count_process in tqdm(range(1, int(mp.cpu_count() * 1.5)), desc="Поиск коллизии"):
        start_time = time.time()
        if get_card_number(original_hash, bins, last_digit, count_process):
            time_list.append(time.time() - start_time)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(range(1, int(mp.cpu_count() * 1.5)), time_list, color='#4CAF50', edgecolor='black', linewidth=1)
    ax.set_xlabel('Количество процессов')
    ax.set_ylabel('Время, с')
    ax.set_title("Статистика времени выполнения")
    plt.show()


if __name__ == "__main__":
    setting = work_to_file.read_json("parametrs.json")
    number = work_to_file.read_json("card.json")
    print(f'The card number is correct: {luhn_algorithm(number["card_number"])}')
    graphing(setting["hash"], setting["bins"], setting["last_numbers"])
    get_card_number(setting["hash"], setting["bins"], setting["last_numbers"])
