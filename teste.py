import wmi

def get_system_info():
    # Cria um objeto wmi para interagir com a WMI
    c = wmi.WMI()

    # Obter informações sobre o processador
    processor_info = c.query("SELECT * FROM Win32_Processor")
    processor_name = processor_info[0].Name if processor_info else "Desconhecido"

    # Obter informações sobre a memória RAM
    memory_info = c.query("SELECT * FROM Win32_ComputerSystem")
    total_memory = memory_info[0].TotalPhysicalMemory if memory_info else "Desconhecido"

    # Converte memória de bytes para GB
    total_memory_gb = int(total_memory) / (1024**3) if total_memory != "Desconhecido" else "Desconhecido"

    return processor_name, total_memory_gb

# Exibe as informações
processor, memory = get_system_info()
print(f"Processador: {processor}")
print(f"Memória Total: {memory:.2f} GB")