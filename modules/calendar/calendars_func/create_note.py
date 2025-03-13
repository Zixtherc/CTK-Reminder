import customtkinter as ctk

# Настройка темы
ctk.set_appearance_mode("dark")

# Окно
app = ctk.CTk()
app.geometry("300x200")
app.title("CTkSlider Demo")

# Функция для обновления текста
def update_label(value):
    label.configure(text=f"Value: {int(slider.get())}")

# Заголовок
label = ctk.CTkLabel(app, text="Value: 0", font=("Arial", 24))
label.pack(pady=10)

# Кастомный слайдер с progress_color
slider = ctk.CTkSlider(
    app, from_=0, to=100, command=update_label,
    progress_color="#00ffcc",  # Цвет активной части (неоновый бирюзовый)
    fg_color="#222222",        # Цвет неактивной части (тёмный фон)
    button_color="#00cc99",    # Цвет ползунка
    button_hover_color="#00ffaa",  # Цвет ползунка при наведении
    height=8
)
slider.pack(fill="x", padx=20, pady=10)

# Запуск
app.mainloop()
