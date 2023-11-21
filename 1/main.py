import math
import re
from collections import defaultdict
from copy import copy


def print_welcome(message):
    print(f'{message}')


def read_file(file_path):
    file = open(file_path, encoding="utf8")
    return file.readlines()


def format_file(strings: list[str]):
    for i in range(len(strings)):
        low_string = strings[i].lower()
        string_without_punct = re.sub(r"[ \s\d]|[^\w\s]", "", low_string)
        strings[i] = string_without_punct
    return strings


def save_validated_file(stings: list[str], file_path: str):
    file = open(file_path, "r+", encoding="utf8")
    if file.writable():
        file.writelines(stings)
    else:
        raise FileNotFoundError("file is not writable")


def count_occurrence_combination(strings: list[str]):
    one_letter_occurrence = defaultdict()
    for string in strings:
        is_string_checked = defaultdict()
        for char in string:
            if not one_letter_occurrence.get(char):
                one_letter_occurrence[char] = string.count(char)
                is_string_checked[char] = True
            else:
                if not is_string_checked.get(char):
                    one_letter_occurrence[char] += string.count(char)
                    is_string_checked[char] = True

    two_letter_occurrence = defaultdict()
    for string in strings:
        is_string_checked = defaultdict()
        for i in range(len(string) - 1):
            if not is_string_checked.get(f"{string[i]}{string[i + 1]}"):
                two_letter_occurrence[f"{string[i]}{string[i + 1]}"] = string.count(f"{string[i]}{string[i + 1]}")
                is_string_checked[f"{string[i]}{string[i + 1]}"] = True
            else:
                if not is_string_checked.get(f"{string[i]}{string[i + 1]}"):
                    one_letter_occurrence[f"{string[i]}{string[i + 1]}"] += string.count(f"{string[i]}{string[i + 1]}")
                    is_string_checked[f"{string[i]}{string[i + 1]}"] = True

    one_letter_popularity = copy(one_letter_occurrence)

    one_letter_combinations = 0
    for combination_count in one_letter_occurrence.values():
        one_letter_combinations += combination_count
    for key in one_letter_occurrence.keys():
        one_letter_occurrence[key] = one_letter_occurrence.get(key) / one_letter_combinations

    two_letter_combinations = 0
    for combination_count in two_letter_occurrence.values():
        two_letter_combinations += combination_count
    for key in two_letter_occurrence.keys():
        two_letter_occurrence[key] = two_letter_occurrence.get(key) / two_letter_combinations
    return [one_letter_occurrence, two_letter_occurrence, one_letter_popularity]


def find_entropy(occurrences: list[defaultdict]):
    probabilities_one_letter = defaultdict()
    for probability in occurrences[0].keys():
        if not probabilities_one_letter.get(probability):
            probabilities_one_letter[probability] = 1
        else:
            probabilities_one_letter[probability] += 1

    probabilities_two_letter = defaultdict()
    for probability in occurrences[1].keys():
        if not probabilities_two_letter.get(probability):
            probabilities_two_letter[probability] = 1
        else:
            probabilities_two_letter[probability] += 1

    parts_of_expression = []

    for key in occurrences[0].keys():
        parts_of_expression.append(
            probabilities_one_letter.get(key) * occurrences[0].get(key) * math.log2(occurrences[0].get(key)))
    entropy_one_letter = 0
    for expression in parts_of_expression:
        entropy_one_letter += expression
    entropy_one_letter = entropy_one_letter * (-1)
    entropy_one_letter = round(entropy_one_letter, 2)

    parts_of_expression = []
    for key in occurrences[1].keys():
        parts_of_expression.append(
            probabilities_two_letter.get(key) * occurrences[1].get(key) * math.log2(occurrences[1].get(key)))
    entropy_two_letter = 0
    for expression in parts_of_expression:
        entropy_two_letter += expression
    entropy_two_letter = entropy_two_letter * (-1)
    entropy_two_letter = round(entropy_two_letter, 2)

    return [entropy_one_letter, entropy_two_letter]


def find_code_length(one_letter_occurrence: defaultdict):
    total_codes_amount = 0
    for _ in one_letter_occurrence:
        total_codes_amount += 1
    return math.ceil(math.log2(total_codes_amount))

def find_information_redundancy(code_len, entropy_one_letter):
    return round(1 - (entropy_one_letter / code_len), 3)


def del_most_popular(procent_amount, valid_text, combination_rate_one_letter):
    sorted_chars = sorted(combination_rate_one_letter.items(), key=lambda item: item[1])
    chars_to_delete = int((procent_amount / 100) * len(sorted_chars))
    for char, _ in sorted_chars[:chars_to_delete]:
        valid_text = valid_text.replace(char, "")
    return valid_text.split(" ")


def del_rare_popular(procent_amount, valid_text, combination_rate_one_letter):
    sorted_chars = sorted(combination_rate_one_letter.items(), key=lambda item: item[1])
    chars_to_delete = int((procent_amount / 100) * len(sorted_chars))
    for char, _ in sorted_chars[-chars_to_delete:]:
        valid_text = valid_text.replace(char, "")
    return valid_text.split(" ")

if __name__ == '__main__':
    print_welcome('В качестве текста использованы 3 главы первой части пртступления и наказания')

    print("Читаю файл ...")
    strings_arr = read_file('task.txt')

    print("Избавляюсь от пробелов и знаоков препинаия...")
    valid_strings = format_file(strings_arr)
    valid_text = ' '.join(valid_strings)

    print("Сохраняю обработанный файл...")
    save_validated_file(valid_strings, "validated.txt")

    combination_rate = count_occurrence_combination(valid_strings)
    print(
        f'Частота появления однобуквенных сочетайний {combination_rate[0]}\nЧастота появления двухбуквенных сочетаний {combination_rate[1]}')

    entropies = find_entropy(combination_rate)
    print(f'Энтропия однобуквенных сочетаний {entropies[0]}\nЭнтропия двухбуквенных сочетаний {entropies[1]}')

    code_length = find_code_length(combination_rate[0])
    print(f'Длина кода при равномерном побуквенном кодировании {code_length}')

    redundancy = find_information_redundancy(code_length, entropies[0])
    print(f'Избыточность {redundancy}')
    valid_text_copy = copy(valid_text)

    print(f'Удалию 20% наиболее часто встречающихся символов и провожу повторные расчёты...')
    strings_without_popular = del_most_popular(20, valid_text, combination_rate[2])
    combination_rate_not_pop = count_occurrence_combination(strings_without_popular)
    print(
        f'Новая частота появления однобуквенных сочетайний {combination_rate_not_pop[0]}\nНовая частота появления двухбуквенных сочетаний {combination_rate_not_pop[1]}')
    entropies_not_pop = find_entropy(combination_rate_not_pop)
    print(
        f'Новая энтропия однобуквенных сочетаний {entropies_not_pop[0]} изменилась на {entropies[0] - entropies_not_pop[0]}\nНовая энтропия двухбуквенных сочетаний {entropies_not_pop[1]} изменилась на {entropies[1] - entropies_not_pop[1]}')

    print(f'Удаляю 20% наименее часто встречающихся символов и провожу повторные расчёты...')
    strings_without_rare = del_rare_popular(20, valid_text_copy, combination_rate[2])
    combination_rate_not_rare = count_occurrence_combination(strings_without_rare)
    print(f'Новая частота появления однобуквенных сочетайний {combination_rate_not_rare[0]}\nНовая частота появления двухбуквенных сочетаний {combination_rate_not_rare[1]}')
    entropies_not_rare = find_entropy(combination_rate_not_rare)
    print(f'Новая энтропия однобуквенных сочетаний {entropies_not_rare[0]} изменилась на {entropies[0] - entropies_not_rare[0]}\nНовая энтропия двухбуквенных сочетаний {entropies_not_rare[1]} изменилась на {entropies[1] - entropies_not_rare[1]}\n')
