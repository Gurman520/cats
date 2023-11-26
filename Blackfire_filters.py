from PIL import Image
from PIL import ImageEnhance


class Photo_filter:
    """
    Базовый класс для создания фильтров
    """
    def __init__(self, name, text):
        self.name = name
        self.text = text


class Red_and_blue(Photo_filter):
    def __init__(self):
        super().__init__(
            "Красно-синий",
            "Оставляет в картинке только красный и синий цвета, а также их оттенки."
                         )

    def filter(self, img: Image.Image) -> Image.Image:
        n, m = img.size
        new_img = Image.new("RGB", (n, m))
        for i in range(n):
            for j in range(m):
                color = img.getpixel((i, j))
                new_color = (color[0], 0, color[2])
                new_img.putpixel((i, j), new_color)

        return new_img


class Squares(Photo_filter):
    def __init__(self):
        super().__init__(
            "По квадратам",
            "Разделяет фото на 4 равных кусочка, которое переводит в ч/б, при этом инверсируя 2 из них."
        )

    def black_and_white_inversion(self, part):
        n, m = part.size
        new_img = Image.new("L", (n, m))
        for i in range(n):
            for j in range(m):
                new_img.putpixel((i, j), 255 - part.getpixel((i, j)))
        return new_img

    def filter(self, img: Image.Image) -> Image.Image:
        n, m = img.size
        new_img = Image.new("L", (n, m))
        part1 = img.crop((0, 0, n // 2, m // 2))
        part1 = part1.convert("L")
        part2 = img.crop((n // 2 + 1, 0, n, m // 2))
        part2 = part2.convert("L")
        part2 = self.black_and_white_inversion(part2)
        part3 = img.crop((0, m // 2 + 1, n // 2, m))
        part3 = part3.convert("L")
        part3 = self.black_and_white_inversion(part3)
        part4 = img.crop((n // 2 + 1, m // 2 + 1, n, m))
        part4 = part4.convert("L")
        new_img.paste(part1, (0, 0))
        new_img.paste(part2, (n // 2 + 1, 0))
        new_img.paste(part3, (0, m // 2 + 1))
        new_img.paste(part4, (n // 2 + 1, m // 2 + 1))
        return new_img


class Inversion(Photo_filter):
    def __init__(self):
        super().__init__(
            "Разноцветная инверсия",
            "Инверсирует вашу картинку."
        )

    def filter(self, img: Image.Image) -> Image.Image:
        n, m = img.size
        new_img = Image.new("RGB", (n, m))
        new_img = new_img.convert("RGB")
        test = img.getpixel((0, 0))
        for i in range(n):
            for j in range(m):
                color = img.getpixel((i, j))
                new_color = (250 - color[0], 250 - color[1], 250 - color[2])
                new_img.putpixel((i, j), new_color)
        return new_img


class Black_and_White(Photo_filter):
    def __init__(self):
        super().__init__(
            "Чёрно-белый пуантилизм",
            "Переводит вашу картинку в изображение из двух цветов: чёрного и белого. \n"
            "Явный закос под стиль в искусстве 19 века.."
        )

    def filter(self, img: Image.Image) -> Image.Image:
        img = img.convert("1")
        return img

