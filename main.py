from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def draw_12(text): # Функция для рисования на исходнике
    my_coords = [(0, 1075, 940, 58), (1, 1160, 940, 58),
                 (3, 1260, 1170, 120), (4, 1225, 1560, 58)]
    # Открываем изображение
    image = Image.open('Certificate.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('MyriadPro.ttf', 58)
    word = text[2]
    new_word = word.replace("ия", "ии")

    draw.text((1430, 918), new_word, font=font,
              fill=(12, 12, 12))
    for numText, coordinates_x, coordinates_y, sizeFont in my_coords:
        # Создаем объект ImageDraw
        # Определяем шрифт и размер шрифта
        font = ImageFont.truetype('MyriadPro.ttf', sizeFont)
        # Определяем размеры контейнера
        container_width = 1
        container_height = 1
        # Определяем координаты верхнего левого угла контейнера
        container_x = coordinates_x
        container_y = coordinates_y
        # Определяем размеры текста
        text_bbox = draw.textbbox((0, 0), text[numText], font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        # Определяем координаты верхнего левого угла текста
        text_x = container_x + (container_width - text_width) / 2
        text_y = container_y + (container_height - text_height) / 2
        # Рисуем текст
        draw.text((text_x, text_y), text[numText], font=font,
                  fill=(12, 12, 12))
    # Сохраняем изображение
    #image.save(f'{text[3]}.jpg')
    return image

# Текст из базы данных нужно будет привести к такому формату
text = ["1", "А", "Гимназия №108", "Казаков Салават", datetime.now().strftime('%d.%m.%Y')]
# Вызов функции, по идееи должна вернуть изображение
d = draw_12(text)
#Проверял что возврощается
d.save("123.jpg")

