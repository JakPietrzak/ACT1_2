res1 = requests.get("http://127.0.0.1:5000/hello")
print(res1.content)  # Powinno zwrócić "Hello!"

res2 = requests.get("http://127.0.0.1:5000/hello?name=Sebastian")
print(res2.content)  # Powinno zwrócić "Hello Sebastian!"

res3 = requests.get("http://127.0.0.1:5000/mojastrona")
print(res3.content)  # Powinno zwrócić "To jest moja strona!"


res4 = requests.get("http://127.0.0.1:5000/")
print(res4.content)  # Powinno zwrócić "Witaj W Moim API!"

res5 = requests.get("http://127.0.0.1:5000/api/v1.0/predict?num1=3&num2=4")
print(res5.json())  # Powinno zwrócić {"prediction": 1, "features": {"num1": 3.0, "num2": 4.0}}

