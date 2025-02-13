import tkinter as tk
from network import get_local_ip, get_public_ip
from memory import get_memory_info
from system import get_disk_info, get_cpu_phisical_cores, get_cpu_logical_cores, get_cpu_frequency, get_cpu_usage, get_cpu_name

# Pegando informações do sistema para exibir no IpShow
cpu_usage = get_cpu_usage()
cpu_phisical_cores = get_cpu_phisical_cores()
cpu_logical_cores = get_cpu_logical_cores()
cpu_frequency = get_cpu_frequency()
cpu_name = get_cpu_name()
print (cpu_name)

# Função para atualizar as informações na interface
def update_memory_label():
    memory_used, memory_total = get_memory_info()
    label_memory_used.config(text=f'Mem usada: {memory_used}')
    label_memory_total.config(text=f'Mem total: {memory_total}')
    
    root.after(1000, update_memory_label)

# Função para atualizar as informações na interface
def update_cpu_usage_label():
    cpu_usage = get_cpu_usage()
    label_cpu_usage.config(text=f'CPU uso: {cpu_usage}')
    
    
    root.after(1000, update_cpu_usage_label)

# Criar janela principal
root = tk.Tk()
root.title("Meus ip's")

# Definir tamanho e posição (exemplo: 300x100 pixels no canto superior direito)
largura = 300
altura = 200
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
label_local_ip = tk.Label(root, text=f'Ip local: {get_local_ip()}', font=("Arial", 8, "bold"), fg="black", pady=0) 
label_public_ip = tk.Label(root, text=f'Ip público: {get_public_ip()}', font=("Arial", 8, "bold"), fg="black", pady=0)
label_memory_used = tk.Label(root, text=f'Mem usada: 0%', font=("Arial", 8, "bold"), fg="black", pady=0) 
label_memory_total = tk.Label(root, text=f'Mem total: 0 GB', font=("Arial", 8, "bold"), fg="black", pady=0)
label_cpu_name = tk.Label(root, text=f'Processador: {cpu_name}', font=("Arial", 8, "bold"), fg="black", pady=0)
label_cpu_usage = tk.Label(root, text=f'CPU uso: {cpu_usage}', font=("Arial", 8, "bold"), fg="black", pady=0)
label_cpu_phisical_cores = tk.Label(root, text=f'Núcleos: {cpu_phisical_cores}', font=("Arial", 8, "bold"), fg="black", pady=0)
label_cpu_logical_cores = tk.Label(root, text=f'Núcleos: {cpu_logical_cores}', font=("Arial", 8, "bold"), fg="black", pady=0)
label_cpu_frequency = tk.Label(root, text=f'Frequência: {cpu_frequency}', font=("Arial", 8, "bold"), fg="black", pady=0)


# Usar place para posicionar os rótulos sem espaçamento extra
label_local_ip.place(x=5, y=5)
label_public_ip.place(x=5, y=20)
label_memory_used.place(x=5, y=45)
label_memory_total.place(x=5, y=60)
label_cpu_name.place(x=5, y=85)
label_cpu_phisical_cores.place(x=5, y=100)
label_cpu_logical_cores.place(x=5, y=115)
label_cpu_frequency.place(x=5, y=130)
label_cpu_usage.place(x=5, y=145)


# Iniciar o loop de atualização da memória/uso da CPU
update_memory_label()
update_cpu_usage_label()

# Iniciar loop da interface
root.mainloop()
