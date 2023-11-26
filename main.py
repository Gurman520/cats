from filters import BrightFillter, DarkFillter, InverseFillter
from PIL import Image
import os


def main():
    filter_names = ["Увеличить яркость", "Уменьшить яркость", "Инверсия"]
    filters = [BrightFillter(), DarkFillter(), InverseFillter()]

    print("Добро пожаловать в консольный фоторедактор.")
    is_finished = False
    while not is_finished:
        # спрашиваем путь к файлу
        path = input("Введите путь к файлу: ")

        # проверяем ввод
        while not os.path.exists(path):
            path = input("Файл не найден. Попробуйте еще раз: ")

        # открываем изображение и на всякий случай преобразуем его в L
        img = Image.open(path).convert("L")

        print("Какой фильтр вы хотите применить?")
        for i in range(len(filter_names)):
            print(f"{i} - {filter_names[i]}")

        # запрашиваем номер фильтра
        choice = input("Выберите фильр (введите номер): ")

        # проверяем ввод
        while not choice.isdigit() or int(choice) >= len(filters):
            choice = input("Неккоректный ввод. Попробуйте еще раз: ")

        # Применяем фильтр
        filter = filters[int(choice)]
        img = filter.apply_to_image(img)

        # спрашиваем куда сохранить результат
        save_path = input("Куда сохранить: ")

        # сохраняем
        img.save(save_path)

        # спрашиваем, хотим ли повторить
        answer = input("Еще раз? (да/нет): ").lower()

        # Проверяем ввод
        while answer != "да" and answer != "нет":
            answer = input("Некорректный ввод. Попробуйте еще раз: ").lower()

        is_finished = answer == "нет"


if __name__ == "__main__":
    main()
