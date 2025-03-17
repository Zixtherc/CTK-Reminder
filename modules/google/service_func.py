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
    creds = None
    token_path = abspath(join(__file__, '..', '..', '..', 'static', 'google_settings', 'token.json'))
    if path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            credentials_path = abspath(join(__file__, '..',  '..', '..', 'static', 'google_settings','credentials.json'))
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port = 0)

        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())
            
    try:
        service = build('calendar', 'v3', credentials = creds)
        return service
    
    except Exception as error:
        print(f'{red}Ошибка при создании service: {error} {reset}')
        return False

a = create_service()
print(f'Всё получилось, вот сервис: {a}')