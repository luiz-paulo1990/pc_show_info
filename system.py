import psutil
import wmi

def get_disk_info():
    try:
        disk = psutil.disk_usage('/')
        return f'{disk.percent}% usado de {disk.total / (1024**3):.2f} GB'
    except Exception as e:
        return f"Erro ao obter HD: {e}"


def get_cpu_name():
    # Cria um objeto wmi para interagir com a WMI
    c = wmi.WMI()

    # Obter informações sobre o processador
    processor_info = c.query("SELECT * FROM Win32_Processor")
    processor_name = processor_info[0].Name if processor_info else "Desconhecido"

    return processor_name


def get_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)  # interval=1 significa que será medido ao longo de 1 segundo
        return f'{cpu_usage}%'
    except Exception as e:
        return f'Erro ao obter CPU: {e}'
    
def get_cpu_phisical_cores():
    try:
        cpu_cores = psutil.cpu_count(logical=False)  # Para pegar os núcleos físicos
        return f'{cpu_cores} núcleos físicos'
    except Exception as e:
        return f'Erro ao obter núcleos: {e}'
    
def get_cpu_logical_cores():
    try:
        cpu_logical_cores = psutil.cpu_count(logical=True)  # Para pegar os núcleos lógicos (threads)
        return f'{cpu_logical_cores} núcleos lógicos'
    except Exception as e:
        return f'Erro ao obter núcleos lógicos: {e}'
    
def get_cpu_frequency():
    try:
        cpu_freq = psutil.cpu_freq()
        return f'{cpu_freq.max} MHz'
    except Exception as e:
        return f'Erro ao obter frequência da CPU: {e}'