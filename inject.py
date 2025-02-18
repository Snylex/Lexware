import tkinter as tk
from tkinter import messagebox
import requests
import os
import subprocess
import customtkinter as ctk

# Н
ctk.set_appearance_mode("dark")  # Т
ctk.set_default_color_theme("blue")  # Синяя цветовая схема

# U
BOTS = {
    "Bot 1": "https://raw.githubusercontent.com/Snylex/Lexware/refs/heads/master/inject.py",
    "Bot 2": "https://ваш-сайт/bot2.py",
}

def download_and_run(bot_name, bot_url):
    try:
        # Заа
        response = requests.get(bot_url)
        if response.status_code == 200:
            code = response.text

            # Сохраненл
            temp_file = "temp_bot.py"
            with open(temp_file, "w", encoding="utf-8") as file:
                file.write(code)

            
            subprocess.run(["python", temp_file], check=True)

            
            os.remove(temp_file)
            messagebox.showinfo("Успех", f"Бот {bot_name} успешно запущен!")
        else:
            messagebox.showerror("Ошибка", "Не удалось загрузить код.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

def create_gui():
    
    root = ctk.CTk()
    root.title("Bybit Style Loader")
    root.geometry("500x400")  # Размер окна

    # Заголовок
    title_label = ctk.CTkLabel(
        root,
        text="ZAPUSTI MENYUA",
        font=("Arial", 24, "bold"),
        text_color="#00aaff",  # Синий цвет, как у Bybit
    )
    title_label.pack(pady=20)

    # Фрейм для кнопок
    button_frame = ctk.CTkFrame(root, fg_color="transparent")
    button_frame.pack(pady=20)

    # Кнопки для выбора бота
    for bot_name, bot_url in BOTS.items():
        button = ctk.CTkButton(
            button_frame,
            text=bot_name,
            command=lambda name=bot_name, url=bot_url: download_and_run(name, url),
            font=("Arial", 16),
            width=200,
            height=40,
            corner_radius=10,
            fg_color="#00aaff",  # Синий цвет кнопок
            hover_color="#0088cc",  # Темно-синий при наведении
        )
        button.pack(pady=10)

    # Кнопка выхода
    exit_button = ctk.CTkButton(
        root,
        text="Выход",
        command=root.quit,
        font=("Arial", 14),
        width=100,
        height=30,
        corner_radius=10,
        fg_color="#ff5555",  # Красный цвет для кнопки выхода
        hover_color="#cc0000",  # Темно-красный при наведении
    )
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
