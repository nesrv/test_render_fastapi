from langchain_gigachat.chat_models import GigaChat

# Запрашиваем путь к изображению
image_path = input("Введите путь к изображению: ")

# Создаем модель
model = GigaChat(
    model="GigaChat-2-Max",
    verify_ssl_certs=False,
    credentials="=="
)

print("Распознаю текст...")

# Загружаем изображение
with open(image_path, "rb") as image_file:
    file_uploaded_id = model.upload_file(image_file).id_

# Отправляем запрос на распознавание текста
message = {
    "role": "user",
    "content": "Распознай текст с этого изображения и выведи его полностью.",
    "attachments": [file_uploaded_id]
}

response = model.invoke([message])

# Выводим результат
print("\nРаспознанный текст:")
print("-" * 50)
print(response.content)
print("-" * 50)