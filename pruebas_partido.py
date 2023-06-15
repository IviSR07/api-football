partido = {
    "local": 'RMA',
    "visitante": 'FCB',
    "local": { 
        "goles":0
    },
    "visitante": {
        "goles": 0
    }
}

def sumar_gol_local(partido):
    partido["local"]["goles"] = partido["local"]["goles"] + 1
    return partido

def sumar_gol_visitante(partido):
    partido["visitante"]["goles"] = partido["visitante"]["goles"] + 1
    return partido

# Parte 1 
partido = sumar_gol_visitante(partido)
# RMA 0 - FCB 1
print(f"Parte 1: {partido}")

# Parte 2
partido = sumar_gol_local(partido)
# RMA 1 - FCB 1
print(f"Parte 2: {partido}")

# Parte 3
# TODO: código que llama a la función de marcar el equipo local
# RMA 2 - FCB 1
print(partido)

# Parte 4
# TODO: código que llama a la función de marcar el equipo local
# RMA 3 - FCB 1
print(partido)