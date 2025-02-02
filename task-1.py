# а) Отрефакторить программу с прошлой домашней работы на ООП стиль.

# Задача из прошлой домашки:
# а) Сделать набросок дизайна программы в figma / paint для программы,
# которая делает запрос на сайт jsonplaceholder с определённым id.
# б) Разработать эту программу на библиотеке tkinter.
# в) Реализовать сохранение полученного объекта в папку.

# Теперь нужно ее выполнить, используя классы
# Чтобы работать с GUI и tkinter в контексте ООП, необходимо использовать класс Frame, который предназначен 
# для организации виджетов внутри окна. Это своего рода контейнер, в который можно положить другие элементы
# интерфейса (например, кнопки, метки, текстовые поля). Он помогает организовывать и сгруппировать элементы, 
# чтобы было легче управлять их расположением и внешним видом.
from tkinter import Tk, Frame, Button, Label, TOP
import requests
import os
import json
# Создадим основной класс, который будет наследоваться от Frame, это позволит нам использовать этот класс как 
# контейнер для виджетов
class Main(Frame):
    # Создаем конструктор класса, который будет принимать окно, то есть объект класса Tk()
    def __init__(self, window):
        # далее вызываем конструктор Frame и указываем, что этот Frame должен быть дочерним элементом окна window.
        # Это означает, что все виджеты внутри этого Frame будут размещены внутри окна window
        super().__init__(window)
        # затем вызываем метод внутри конструктора
        self.init_main()
    # В этом методе будет настраиваться логика создания и размещения виджетов внутри Frame   
    def init_main(self):
        # Создадим бирку с текстом
        label = Label(window, text='Загрузка JSON', font=('Arial', 20))
        # здесь вместо grid воспользуемся более простым методом .pack(), который позволяет последовательно размещать 
        # элементы по какому-либо направлению, в данном случае ТОР означает сверху и, если ничего другого не указывать,
        # автоматически ставит элемент посередине 
        label.pack(side=TOP)
        # Далее создадим кнопку и привяжем к ней функцию
        btn = Button(window, text='Загрузить', command=self.json_download)
        btn.pack(side=TOP)
    # Функция как в прошлом домашке для создания папки с JSON-файлами
    def json_download(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        data = response.json()
        current_dir = os.getcwd()
        folder_name = 'JSON Folder'
        path = os.path.join(current_dir, folder_name)
        os.makedirs(path, exist_ok=True)
        for d in data:
            file_name = f'data_{d["id"]}.json'
            file_path = os.path.join(path, file_name)
            with open(file_path, 'w') as file:
                json.dump(d, file)

# Теперь запускаем наш код
if __name__ == '__main__':
    # Создадим окно - объект класса Tk
    window = Tk()
    # Создадим приложение - объект класса Main и передадим ей window
    app = Main(window)
    # Разместим это приложение 
    app.pack()
    # Зададим заголовок для этого окна
    window.title('JSON download')
    # Зададим размер для окна
    window.geometry('200x100')
    # Запустим открытие окна
    window.mainloop()