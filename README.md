![image](https://github.com/user-attachments/assets/0e028f62-69aa-4e21-b2ce-cc504fa594c1)

# Неофіційний CLI-клієнт Світлобота на Python

## Встановлення Python

### Для користувачів Windows:
1. Зайдіть на сайт python.org і завантажте встановлювач Python
2. Під час встановлення поставте галочку біля "Add Python to PATH"
3. Завершіть встановлення

### Для користувачів Linux:
Гарні новини! Python вже встановлено у вашій системі.

### Для користувачів MacOS:
1. Спочатку встановіть Homebrew (інструкції на https://brew.sh)
2. Відкрийте Термінал і введіть: `brew install python`

## Встановлення необхідних бібліотек

### Для Windows та MacOS:
Відкрийте Термінал (або Командний рядок на Windows) і введіть:
```
pip install requests
```

### Для Linux:

Відкрийте Термінал і введіть:

### Для Debian дистрибутивів
```
sudo apt install pipx
```
### Arch Linux
```
sudo pacman -S python-pipx
```
### Fedora
```
sudo dnf install python3-pip
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```
### OpenSuse
```
sudo zypper install python3-pip
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```
### Gentoo
```
sudo emerge --ask dev-python/pipx
```
### Alpine Linux
```
sudo apk add py3-pip
pip3 install pipx
pipx ensurepath
```
### Solus
```
sudo eopkg install python3-pip
pip3 install pipx
pipx ensurepath
```
### Встановлення бібліотеки

```
pipx install requests
```
## Запуск CLI Світлобота

1. Завантажте файл `svitlobot-cli.py` зі сторінки GitHub
2. Відкрийте Термінал (або Командний рядок)
3. Перейдіть до папки, де ви зберегли файл
4. Введіть одну з цих команд:
   ```
   python svitlobot-cli.py
   ```
   або
   ```
   python3 svitlobot-cli.py
   ```

Потрібна допомога? Напишіть @Romikan4ik у Telegram!
