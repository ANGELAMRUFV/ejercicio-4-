import requests

url = "https://api.exchangerate-api.com/v4/latest/EUR"
respuesta = requests.get(url)
datos = respuesta.json()

rates = datos["rates"]

moneda_economica = None
valor_maximo = 0

for moneda, valor in rates.items():
    print(moneda, valor)
    if valor > valor_maximo:
        valor_maximo = valor
        moneda_economica = moneda

print("----------------------")
print(f"La moneda más económica es {moneda_economica}")
print(f"1 EUR = {valor_maximo} {moneda_economica}")
print(f"1 {moneda_economica} = {1 / valor_maximo:.8f} EUR")