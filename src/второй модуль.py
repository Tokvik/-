from PIL import Image
import os
import imghdr


def get_image_info(image_path):
    """Получает и отображает информацию об изображении."""
    try:
        img = Image.open(image_path)
        image_format = imghdr.what(image_path)
        width, height = img.size
        
        # Добавьте информацию о цветовом режиме (RGB, L и т.д.)
        mode = img.mode

        print(f"Информация об изображении:")
        print(f"Путь: {image_path}")
        print(f"Формат: {image_format}")
        print(f"Ширина: {width} пикселей")
        print(f"Высота: {height} пикселей")
        print(f"Цветовой режим: {mode}")  # Добавлен вывод цветового режима

        # Дополнительный вывод для оптимизации.
        img.close()  # Закрытие объекта Image, важно для освобождения ресурсов.
        return {"path": image_path, "format": image_format, "width": width, "height": height, "mode": mode}

    except FileNotFoundError:
        print(f"Ошибка: Файл {image_path} не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при обработке изображения: {e}")
        return None



def get_image_path_from_user():
    """Запрашивает путь к изображению у пользователя."""
    while True:
        image_path = input("Введите полный путь к изображению: ")
        if os.path.exists(image_path):
            return image_path
        else:
            print("Файл не найден. Попробуйте снова.")

if __name__ == "main":
    image_path = get_image_path_from_user()
    if image_path:
        image_data = get_image_info(image_path)
        if image_data:
            print(image_data)  # Выводим словарь с информацией