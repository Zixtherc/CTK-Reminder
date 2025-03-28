import customtkinter as ctk

def update_animation_steps(step: int, steps: int, animated_obj: object, step_size: int):
    if step < steps:
        current_x = animated_obj.winfo_x()
        print(f'Это текущий х: {current_x}')
        print(f'Это длина шага: {step_size}')

        animated_obj.place(x = current_x + step_size)

        print(f'Это сумма: {current_x + step_size} ')
        animated_obj.after(13, update_animation_steps, step + 1 , steps, animated_obj, step_size)            
    

def animation(shift_distance: int, animated_obj: object, steps: int = 10):
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
    step_size = shift_distance / steps
    # Обнуляем общее количество шагов
    step = 0
    update_animation_steps(step = step, steps = steps, animated_obj = animated_obj, step_size = step_size) 

root = ctk.CTk()
root.geometry("400x300")

button = ctk.CTkButton(root, text="Нажми меня")
button.place(x=50, y=100)

button.after(1000, lambda: animation(3, button)) 
root.mainloop()