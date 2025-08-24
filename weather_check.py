# weather_check.py
import requests

# ユーザーから都市名を入力
city = input("Enter your city: ")

# APIから天気情報を取得
response = requests.get(f"https://wttr.in/{city}?format=3")

# 結果を表示
print(f"Weather for {city}: {response.text}")
