import tkinter as tk
import socket
import requests
import psutil

# Pega o IP local da máquina e retorna ele na função
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_adress = s.getsockname()[0]
        s.close()
        return ip_adress
    except Exception as e:
        return f"Erro ao obter IP: {e}"
    
# Pega o IP público da máquina e retorna ele na função
def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=text")
        return response.text
    except Exception as e:
        return f'Erro ao obter IP Público'
    
# Pega as informações de memória da máquina
def get_memory_info():
    try:
       memory = psutil.virtual_memory()
       memory_used = f'{memory.percent}% usado'
       memory_total = f'{memory.total / (1024**3):.2f} GB total' 
       return memory_used, memory_total
    except Exception as e:
        return f'Erro ao obter memória: {e}'

# Para atualizar a informação de memória usada na interface
def update_memory_label():
    memory_used, memory_total = get_memory_info()
    label_memory_used.config(text=f'Mem usada: {memory_used}')

    # Agenda a próxima atualização da memória usada em 1 segundo:
    root.after(1000, update_memory_label)
    
# Pega as informações da memória
memory_used, memory_total = get_memory_info()

# Criar janela principal
root = tk.Tk()
root.title("Meus ip's")

# Definir tamanho e posição (exemplo: 300x100 pixels no canto superior direito)
largura = 200
altura = 100
pos_x = root.winfo_screenmmwidth() - largura - 20 # 20px de margem da borda direita
pos_y = 20

# Removendo barra de título
root.overrideredirect(True)

# Aplicar tamanho e posição
root.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

# Criar um botão "X" para fechar, usando place para fixá-lo no canto superior direito
close_button = tk.Button(root, text="❌", font=("Arial", 4, "bold"), fg="white", bg="red", 
                         border=0, command=root.destroy, cursor="hand2")
close_button.place(x=largura-18, y=3, width=15, height=15)  # Fixar no canto superior direito

# Deixa o fundo transparente
root.attributes('-alpha', 0.9) # 0.0 = 100% transparente, 1.0 = 100% opaco
root.attributes('-topmost', True) # Janela sempre no topo

# Criar rótulos com IP's e outras informações
label = tk.Label(root, text=f'Ip local: {get_local_ip()}', font=("Arial", 8, "bold"), fg="black", pady=0) 
label2 = tk.Label(root, text=f'Ip público: {get_public_ip()}', font=("Arial", 8, "bold"), fg="black", pady=0)
label_memory_used = tk.Label(root, text=f'Mem usada: {memory_used}', font=("Arial", 8, "bold"), fg="black", pady=0) 
label_memory_total = tk.Label(root, text=f'Mem total: {memory_total}', font=("Arial", 8, "bold"), fg="black", pady=0)

# Usar place para posicionar os rótulos sem espaçamento extra
label.place(x=5, y=5)  # Posição do rótulo 1 (IP local)
label2.place(x=5, y=20)  # Posição do rótulo 2 (IP público)
label_memory_used.place(x=5, y=45)  # Posição do rótulo 3 (Memória usada)
label_memory_total.place(x=5, y=60)  # Posição do rótulo 4 (Memória total)

# Iniciar o loop de atualização da memória
update_memory_label()

# Iniciar loop da interface
root.mainloop()