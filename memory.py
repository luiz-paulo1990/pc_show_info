import psutil

def get_memory_info():
    try:
        memory = psutil.virtual_memory()
        memory_used = f'{memory.percent}%'
        memory_total = f'{memory.total / (1024**3):.2f} GB total'
        return memory_used, memory_total
    except Exception as e:
        return f'Erro ao obter memória: {e}', ''
