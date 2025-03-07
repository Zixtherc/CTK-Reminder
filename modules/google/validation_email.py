forbidden_chars = [' ', '(', ')', ',', ':', ';', '<', '>', '@', '[', '\\', ']']

def check_validation_email(user_text: str):
    '''
    `Функция`, который проверяет `валидность` введенного email-адреса

    Примечание:
        Эта функция `не будет` проверять `другие` почтовые `домены`. 
        Тобеж если вы ввели `urk.net` или другие `домены`.` То функция `запретит` вам вход
    '''
    if user_text.endswith('@gmail.com'):
        user_text = user_text[:-10]
    else:
        return False
    
    for char in forbidden_chars:
        if char in user_text:
            return False
    return True

