import customtkinter as ctk

def update_animation_steps(step: int, steps: int, animated_obj: ctk.CTkButton, step_size: int, start_x: int):
    '''
    #### `Функция`, которая `выполняет` шаги анимации ####

    Параметры:
    - `step:` Текущий шаг анимации;
    - `steps:` Количество шагов анимации;
    - `animated_obj:` Объект, который будет выполнять анимацию (например, `Label`, `Button`);
    - `step_size:` Размер шага анимации;
    - `start_x:` Начальное положение X объекта
    '''
    # Проверяем что шаг больше чем шаги анимации (проще говоря что шаги анимации не отрицательные)
    if step < steps:
        # Получаем новый X 
        new_x = start_x + (step + 1) * step_size
        print(f'Шаг {step + 1}/{steps}: {new_x}')
        # Перемещаем объект на новую позицию
        animated_obj.place(x = new_x)  
        # Вызываем саму себя через 50 миллисекунд
        animated_obj.after(ms = 20, func = lambda: update_animation_steps(step = step + 1, steps = steps, animated_obj = animated_obj, step_size = step_size, start_x = start_x))            

def animation(shift_distance: int, animated_obj: object, steps: int = 10):
    '''
    #### `Функция`, которая `выполняет` анимацию сдвига ####

    Параметры:
    - `shift_distance:` Расстояние сдвига;
    - `steps:` Количество шагов анимации (по умолчанию 10 шагов)'
    - `animated_obj:` Объект, который будет выполнять анимацию (например, `Label`, `Button`)
    '''
    # Получаем изначальное значение X
    start_x = animated_obj.winfo_x()
    # Получаем размер шага анимации
    step_size = shift_distance // steps
    print(f'Это длина шага : {step_size}')
    # Выполняем анимацию с указанными шагами и расстоянием сдвига
    update_animation_steps(step = 0, steps = steps, animated_obj = animated_obj, step_size = step_size, start_x = start_x) 