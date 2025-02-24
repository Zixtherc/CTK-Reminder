from win10toast import ToastNotifier

toast_notify = ToastNotifier()

def notify_message(title: str = "Hello", text: str = "World", duration: int = 5):
    toast_notify.show_toast(title = title, msg = text, duration = duration, threaded = True)
