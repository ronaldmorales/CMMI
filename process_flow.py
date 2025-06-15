# process_flow.py

def ciclo_vida_microservicio():
    """
    Define y muestra las fases estandarizadas del ciclo de vida del microservicio.
    """
    fases = [
        "Análisis de requisitos",
        "Diseño técnico",
        "Implementación",
        "Pruebas",
        "Integración",
        "Entrega"
    ] 

    print("Iniciando ciclo de vida del microservicio:")
    for fase in fases:
        print(f"Fase actual: {fase}") 

# Se llama a la función para ejecutar el flujo
ciclo_vida_microservicio()
