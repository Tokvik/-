from PIL import Image
import os
from datetime import datetime

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        """Загружает изображение из указанного пути."""
        try:
            self.image = Image.open(self.image_path)
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")

    def get_image_info(self):
        """Возвращает информацию об изображении: размер, разрешение, дата создания."""
        if self.image:
            size = self.image.size  # (width, height)
            mode = self.image.mode
            creation_time = os.path.getctime(self.image_path)
            creation_date = datetime.fromtimestamp(creation_time)
            resolution = self.image.info.get('dpi', 'Нет информации о DPI')
            return {
                "size": size,
                "mode": mode,
                "creation_date": creation_date.strftime("%Y-%m-%d %H:%M:%S"),
                "resolution": resolution
            }
        else:
            return None

    def rename_image(self, new_name):
        """Переименовывает изображение на новое имя."""
        try:
            new_path = os.path.join(os.path.dirname(self.image_path), new_name)
            os.rename(self.image_path, new_path)
            self.image_path = new_path  # Обновляем путь к изображению
            print(f"Изображение переименовано в: {new_name}")
        except Exception as e:
            print(f"Ошибка при переименовании изображения: {e}")

# Пример использования модуля
if __name__ == "__main__":
    image_path = input("Введите путь к изображению: ")
    processor = ImageProcessor(image_path)
    
    processor.load_image()
    info = processor.get_image_info()
    
    if info:
        print("Информация об изображении:")
        print(f"Размер: {info['size']}")
        print(f"Режим: {info['mode']}")
        print(f"Дата создания: {info['creation_date']}")
        print(f"Разрешение: {info['resolution']}")
        
        new_name = input("Введите новое имя для изображения (с расширением): ")
        processor.rename_image(new_name)