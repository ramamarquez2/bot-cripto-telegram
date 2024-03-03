import json
import requests
from loguru import logger

base_url = "https://api.coinex.com/v1"

def last_price(cripto):
    endpoint = "/market/ticker"
    url = base_url + endpoint
    params = {"market": criptomoneda.lower() + "usdt"}
    headers = {"Content-Type": "application/json", "User-Agent": "Tu Agente de Usuario"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['ticker']['last']
    else:
        logger.debug("Error al obtener el precio. Código de estado:", response.status_code)
        return None

def main():
    cripto = "BTC"
    print("El precio de " + criptomoneda + ": " + obtener_precio(criptomoneda))


if __name__ == "__main__":
    main()
