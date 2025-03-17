# Необходимые импорты для дочерний работы с GoogleApiCalendar
from os.path import abspath, join
from os import path

# Необходимые импорты для работы с GoogleApiCalendar 
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Для красивого вывода
import colorama
red = colorama.Fore.RED
reset = colorama.Fore.RESET


# Если мы поменяли read.only, то удаляем token.json, если он создан
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def create_service(): 
    '''
    `Функция` для создания `service` для работы с Google Calendar. Service - это объект, который используется для создания запросов, 
    непосредственно к самой API
    '''
    # Создаём переменную
    creds = None
    # Строим путь к 
    token_path = abspath(join(__file__, '..', '..', '..', 'static', 'google_settings', 'token.json'))
    # Если у нас есть токен, то загружаем его в переменную creds
    if path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # Если у нас нет доступных (действительных) учетных данных, заставляем пользователя войти в систему
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        # Иначе
        else:
            # Строим путь к файлу с настройками клиента
            credentials_path = abspath(join(__file__, '..',  '..', '..', 'static', 'google_settings','credentials.json'))
            # Даём возможность войти в аккаунт
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)\
            # Запускаем локальный сервер, чтобы пользователь мог авторизоваться в системе
            creds = flow.run_local_server(port = 0)

        # Открываем наш TOKEN файл 
        with open(token_path, 'w') as token_file:
            # Записываем в него нужную нам информацию
            token_file.write(creds.to_json())
    
    # Создаём и возвращаем service для работы с Google Calendar
    try:
        # Создаём service для работы с Google Calendar
        service = build('calendar', 'v3', credentials = creds)
        # Возвращаем service
        return service
    
    # Обрабатываем ошибку, если она возникнет при запросе
    except Exception as error:
        print(f'{red}Ошибка при создании service: {error} {reset}')
        # Возвразаем False
        return False