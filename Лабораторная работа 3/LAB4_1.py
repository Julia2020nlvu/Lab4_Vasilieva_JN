import csv
import json
from collections import OrderedDict

# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    try:
        with open(INPUT_FILENAME, 'r', encoding='utf-8') as csvfile:4
            reader = csv.DictReader(csvfile)
            data = list(reader)
    except FileNotFoundError:
        print(f"Ошибка: файл {INPUT_FILENAME} не найден.")
        return
    # TODO считать содержимое csv файла
    try:
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Ошибка записи в файл: {e}")
        return
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
  # Нужно для проверки
  task()

  try:
    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
      for line in output_f:
        print(line, end="")
  except FileNotFoundError:
    print(f"Ошибка: файл {OUTPUT_FILENAME} не найден.")