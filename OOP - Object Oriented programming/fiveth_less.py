import json

# https://www.w3schools.com/python/python_json.asp
# Json fayllar bilan ishlash

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)  # JSON-dan Python-ga aylantirish

print(y["age"])

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Sayt orqali tanishib chiqishingiz mumkin !
