import json

def calculate_sum_of_products(file_path: str) -> float:

  try:
    with open(file_path, 'r') as f:
      data = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Ошибка при чтении файла: {e}")
    return 0.0 # Возвращаем 0.0 в случае ошибки

  total_sum = 0.0
  for item in data:
    try:
      score = item["score"]
      weight = item["weight"]
      total_sum += score * weight
    except (KeyError, TypeError) as e:
      print(f"Ошибка обработки словаря: {e}, словарь: {item}")
      # Можно было бы и прервать выполнение, но лучше продолжить обработку других словарей
      continue

  return round(total_sum, 3)


# Пример использования:
file_path = 'data.json' # Замените на путь к вашему JSON файлу

# Создадим тестовый JSON файл
test_data = [
  {"score": 0.0009456152645028281, "weight": 1},
  {"score": 0.5, "weight": 2},
  {"score": 0.2, "weight": 10},
  {"score": 0.1, "weight": 5}

]
with open(file_path, 'w') as f:
  json.dump(test_data, f)

sum_of_products = calculate_sum_of_products(file_path)
print(f"Сумма произведений: {sum_of_products}")

