# Список нажатых кнопок
selected_button = [None]

def select_button(index_button: int, color_select: str = "#000000", all_buttons: list = [], reset_color: str = "#e874af"):
    '''
    `Функция`, для `смены` цвета, при `нажатии` на кнопку, если `повторно` нажать на `любую` `другую`, то цвет `прошлой` кнопки `изменится` на указанный
    '''
    # Проверяем что список нажатых кнопок не пуст
    if selected_button[0] is not None:
        # Если есть, то меняем цвет кнопки, на которую был нажат ранее
        all_buttons[selected_button[0]].configure(fg_color = reset_color)

    # Из всех кнопок, берем необходимый нам индекс, и меняем на указанный параметр
    all_buttons[index_button].configure(fg_color = color_select)

    # Запоминаем индекс текущей нажатой кнопки
    selected_button[0] = index_button