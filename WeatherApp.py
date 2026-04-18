from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
app.json.ensure_ascii = False #отключаем кодировку, т.к. иначе город зашифрован
app.json.sort_keys = False #отключение автоматической сортировки, чтобы нормально показывались данные
API_KEY = "0160de869d4ba0cbcb6aba2f203399ec"

@app.route('/weather', methods=['GET'])#получаем путь /weather
def get_weather():
    city = request.args.get('city') #вытаскиваем город из ссылки localhost
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

    response = requests.get(url)

    data = response.json()
    return jsonify({
        "Город": data["name"],
        "Температура": data["main"]["temp"],
        "Описание": data["weather"][0]["description"],
        "Влажность": data["main"]["humidity"],
        "Скорость ветра": data.get("wind", {}).get("speed", 0)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
