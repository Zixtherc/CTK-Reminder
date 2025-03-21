import customtkinter as ctk

def update_animation_steps(step: int, steps: int, animated_obj: object, step_size: int, canvas = ctk.CTkCanvas):
    if step < steps:
        canvas.move(animated_obj, step_size, 0)

def animation(shift_distance: int, animated_obj: object, canvas: ctk.CTkCanvas, steps: int = 10):
    '''
    #### `Функция`, которая `выполняет` анимацию сдвига ####

    Параметры:
    - `shift_distance:` Расстояние сдвига текста;
    - `steps:` Количество шагов анимации (по умолчанию 10 шагов)'

    Пример использования:
    ```python 
    ПОКА НЕ ДОДЕЛАЛ 
    ''' 
    # Расчитываем сколько будет занимать один шаг анимации
    step_size = shift_distance // steps
    # Обнуляем общее количество шагов
    step = 0
    update_animation_steps(step = step, steps = steps, animated_obj = animated_obj, step_size = step_size, canvas = canvas) 