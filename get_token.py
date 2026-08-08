from yoomoney import Client

# Данные твоего приложения на yoomoney.ru/myservices
client_id = "9B12AD7371E2F6E9D51ED0B11102DA66C638A7EA0E1D1224FCEFBD09B1180EB8"  # Скопируй из настроек приложения
redirect_uri = "https://yoomoney.ru/"  # Должен совпадать с тем, что указан в приложении

print("\n🔑 1. Перейдите по ссылке и разрешите доступ:")
print(f"https://yoomoney.ru/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}\n")

code = input("📋 2. Вставьте code из адресной строки (после ?code=): ").strip()

print("\n🔄 3. Получите токен. Скопируйте и выполните в терминале эту команду (без client_secret):")
print(f'curl -X POST https://yoomoney.ru/oauth/token -d "code={code}&client_id={client_id}&grant_type=authorization_code&redirect_uri={redirect_uri}"')