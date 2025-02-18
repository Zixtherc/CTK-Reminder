def swith_frame(root: object, frame_name: str, frame_color: str = '#00008b'):
    """
    Функция для переключения на другой фрейм.
    """
    # Перебираем все Frame которые мы получили 
    for frame in root.frames.values():
        # Скрываем каждый 
        frame.pack_forget()
        frame.place_forget()

    # Если указанный фрейм существует в словаре
    if frame_name in root.frames:
        # Переименовываем
        frame = root.frames[frame_name]
        # Задаём указанный цвет
        frame.configure(fg_color = frame_color)
        # Размещаем ( relwidth  это ширина нашего фрейма, который будет "замещать" основной HEADER, и его будет не видно)
        frame.place(x=0, y=0, relwidth=1, relheight=1)