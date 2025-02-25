from win10toast import ToastNotifier
import customtkinter as ctk
toast_notify = ToastNotifier()

def notify_message(entry_frames: dict = ctk.CTkEntry):
    title = entry_frames["TITLE_NOTE"].get()
    text = entry_frames["TEXT_NOTE"].get()
    try:
        duration = int(entry_frames["DURATION_NOTE"].get())
    except Exception as e:
        toast_notify.show_toast(title="Ошибка", msg=str(e), duration=5, threaded=True)
    finally:
        toast_notify.show_toast(title = title, msg = text, duration = duration, threaded = True)
