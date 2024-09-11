import requests
import re

try:
    def get_status_description(status_code):
        """
        Повертає опис статусу на основі коду статусу.
        """
        status_descriptions = {
            -2: "Діє повітряна тривога",
            -1: "Діє повітряна тривога",
            1: "Світло є",
            2: "Світла нема",
            3: "Технічна перерва",
            4: "Технічна перерва"
        }
        return status_descriptions.get(status_code, "Невідомий статус")

    def analyze_data(data):
        """
        Аналізує дані та підраховує кількість кожного статусу.
        """
        status_counts = {
            "Світло є": 0,
            "Світла нема": 0,
            "Технічна перерва": 0,
            "Невідомий статус": 0,
            "Діє повітряна тривога": 0,
        }
        
        for line in data:
            fields = line.split(';&&&;')
            
            if len(fields) > 9:
                try:
                    status_code = int(fields[1])
                    description = get_status_description(status_code)
                    status_counts[description] += 1
                except ValueError:
                    status_counts["Невідомий статус"] += 1
        
        return status_counts

    def search_address(search_phrase, data):
        """
        Шукає адресу в даних та виводить інформацію про знайдені збіги.
        """
        search_phrase = search_phrase.strip().lower()  # Нормалізація пошукової фрази
        found = False
        
        for line in data:
            fields = line.split(';&&&;')
            
            if len(fields) > 9:
                address = fields[3].strip().lower()
                if search_phrase in address:
                    try:
                        status_code = int(fields[1])
                        description = get_status_description(status_code)
                        print(f"Адреса: {fields[3]}")
                        print(f"Телеграм канал: https://t.me/{fields[4]}")
                        print(f"Координати: {fields[6]}, {fields[7]}")
                        print(f"Група відключень: {fields[9]}")
                        print(f"Статус: {description}\n")
                        found = True
                    except ValueError:
                        print("Не вдалося конвертувати код статусу")
                        return
        if not found:
            print("Адресу не знайдено")

    def main():
        """
        Головна функція, яка керує роботою CLI.
        """
        print("""
 ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░       ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
 ░▒▓██████▓▒░ ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
       ░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
       ░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓███████▓▒░   ░▒▓██▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░  ░▒▓█▓▒░     
                                                                                                              
                                                                                                                                                                                                             
                                                                                                            
                                                                                                            
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ 
                                    
                                    
                                                                                    
    Made by @Romikan4ik\n\n""")

        while True:
            mode = input("\n\nВас вітає CLI клієнт API Світлобота!\nРежими:\n1. Статистика та інформація по адресі\n2. Зробити Ping каналу у Світлоботі\n3. Змінити розклад відключень\n4. Вийти\n\n\nВведіть режим: ")
            if mode == "1":
                # Отримання даних з API
                url = "https://api.svitlobot.in.ua/website/getChannelsForMap"
                response = requests.get(url)
                
                if response.status_code == 200:
                    data = response.text.split('\n')
                    status_counts = analyze_data(data)
                    print("\n\nСтатистика по статусах:")
                    total = sum(status_counts.values())
                    for status, count in status_counts.items():
                        print(f"{status}: {count}")
                    print(f'Всього: {total}\n')
                    
                    # Пошук адреси
                    while True:
                        user_address = input("Введіть адресу для пошуку (або 'exit' для виходу): ")
                        if user_address.lower() == "exit":
                            print('Виходжу...\n\n')
                            break
                        search_address(user_address, data)
                else:
                    print(f"Помилка запиту: {response.status_code}")

            elif mode == "2":
                # Ping каналу
                print('\nВведіть exit щоб вийти')
                while True:
                    channel_key = input("\nВведіть ключ каналу: ")
                    url = f"https://api.svitlobot.in.ua/channelPing?channel_key={channel_key}"
                    if channel_key.lower() == "exit":
                        break
                    response = requests.get(url)
                    if response.status_code == 200:
                        print('\n\nПінг пройшов успішно!\n')
                        break
                    else:
                        print(f'\n\nСталася помилка\nКод помилки:{response.status_code}\n\n')

            elif mode == "3":
                # Зміна розкладу відключень
                while True:
                    channel_key = input("\nВведіть ключ каналу (або 'exit' для виходу): ")
                    if channel_key.lower() == "exit":
                        break
                    
                    url = f"https://api.svitlobot.in.ua/website/getChannelTimetable?channel_key={channel_key}"
                    response = requests.get(url)
                    
                    if response.status_code == 200:
                        # Розбір відповіді
                        parts = response.text.split(';&&&;')
                        if len(parts) < 2:
                            print("Неочікуваний формат відповіді.")
                            continue

                        # Парсинг даних про групи
                        group_data = parts[0].strip().split('\n')
                        group_dict = {}
                        
                        for line in group_data:
                            if ';&;' in line:
                                group_info = line.split(';&;')
                                if len(group_info) >= 2:
                                    group_id = group_info[0].strip()
                                    group_parts = group_info[1].split('->')
                                    if len(group_parts) >= 2:
                                        city = group_parts[0].strip()
                                        group_name = group_parts[1].strip()
                                        status = group_info[2].strip() if len(group_info) > 2 else 'Невідомо'
                                        group_dict[group_name] = {'id': group_id, 'city': city, 'status': status}

                        if not group_dict:
                            print("Не знайдено дійсних даних про групи.")
                            continue
                        
                        # Виведення доступних груп
                        current_group_id = 0
                        print("\nДоступні групи:")
                        for group_name, group_info in group_dict.items():
                            if int(group_info['status']) == 1:
                                print(f"{group_info['city']} - {group_name} < Встановлена група ")
                                current_group_id = group_info['id']
                            else:
                                print(f"{group_info['city']} - {group_name}")

                        # Вибір нової групи
                        off_group = input("\nВведіть групу, яку ви хочете встановити (наприклад Група 1): ")

                        if off_group in group_dict:
                            group_info = group_dict[off_group]
                            if current_group_id != group_info['id']:
                                # Встановлення нової групи
                                url = f"https://api.svitlobot.in.ua/website/setChannelTimetable?channel_key={channel_key}&timetable_id={group_info['id']}"
                                response = requests.get(url)                        
                                if response.status_code == 200:
                                    print('\nГрупа успішно встановлена!')
                                else:
                                    # Повторна спроба у разі невдачі
                                    url = f"https://api.svitlobot.in.ua/website/setChannelTimetable?channel_key={channel_key}&timetable_id={group_info['id']}"
                                    response = requests.get(url)   
                                    if response.status_code == 200:
                                        print('\nГрупа успішно встановлена!')  
                                    else:
                                        print('\nСталася невідома помилка...')  
                            else:
                                print('Ця група вже встановлена!')  
                        else:
                            print(f"\nГрупу '{off_group}' не знайдено")
                            
                    else:
                        print(f'\nСталася помилка\nКод помилки: {response.status_code}\n')

            elif mode == "4":
                print('Дякуємо за використання нашого CLI Клієнта! До побачення!')
                break
            else:
                print("Неправильний вибір режиму. Спробуйте ще раз.\n")

    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print('\nДякуємо за використання нашого CLI Клієнта! До побачення!')
