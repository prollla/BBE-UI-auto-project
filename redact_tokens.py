import json
import os
import re

def redact_sensitive_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    
    # Редактируем токен, используя шаблон для нахождения токена
    token_pattern = re.compile(r"Bot [A-Za-z0-9._-]+")
    def redact(match):
        return "Bot REDACTED"

    # Преобразуем JSON-данные в строку, чтобы заменить токен
    data_str = json.dumps(data)
    redacted_data_str = token_pattern.sub(redact, data_str)
    redacted_data = json.loads(redacted_data_str)
    
    # Перезаписываем файл с замаскированными данными
    with open(file_path, "w") as file:
        json.dump(redacted_data, file, indent=2)

# Проходим по папке allure-results
report_folder = "allure-results"
for filename in os.listdir(report_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(report_folder, filename)
        redact_sensitive_data(file_path)