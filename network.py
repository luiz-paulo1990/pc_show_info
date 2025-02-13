import socket
import requests

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_adress = s.getsockname()[0]
        s.close()
        return ip_adress
    except Exception as e:
        return f"Erro ao obter IP: {e}"
    
def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=text")
        return response.text
    except Exception as e:
        return f'Erro ao obter IP Público'
