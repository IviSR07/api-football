print("Pruebas equipo")

######## DICCIONARIOS TEAM ############

rma = {
    "name": "Real Madrid", # Entry: Key: name, Value: "Real Madrid"
    "stadium": "Santiago Bernabéu",
    "division": 1,
    "champions": True
}

fcb = {
    "name": "FC Barcelona",
    "stadium": "Camp Nou",
    "division": 2,
    "champions": False
}

bad = {
    "name": "Bad team"
}

bad2 = {
    "division": 2,
}

rmac = {
    "name": "Real Madrid Castilla",
    "stadium": "Alfredo Di Stéfano",
    "division": 3,
    "champions": False
}

######## FIN DE DICCIONARIOS TEAM ############


######## FUNCIONES SOBRE DICCIONARIOS TEAM ############

def change_name(equipo, name):
    equipo["name"] = name

def change_stadium(equipo, stadium):
    equipo["stadium"]= stadium
    
def up_division(equipo):
    if not "division" in equipo.keys(): # Podemos quitar .keys() porque Python ya interpreta que es un diccionario y busca en las claves.
        equipo["division"] = 2
    equipo["division"] = equipo["division"] - 1
    if equipo["division"] < 1 :
        equipo["division"] = 1

def down_division(equipo):
    # TODO: Si el equipo no tiene una división asignada, le ponemos en tercera
    if not "division" in equipo.keys(): # Podemos quitar .keys() porque Python ya interpreta que es un diccionario y busca en las claves.
        equipo["division"] = 2
    
    equipo["division"] = equipo["division"] + 1
    # TODO: La mínima división en la que puede estar un equipo es la tercera división
    if equipo["division"] > 3:
        equipo["division"]= 3

    
def play_champions(equipo):
    # TODO: Un equipo puede jugar la Champions sólo si está en primera división
    # if equipo["division"] == 1
    equipo["champions"] = True

def not_play_champions(equipo):
    equipo["champions"] = False
    
######## FIN DE FUNCIONES SOBRE DICCIONARIOS TEAM ############

######## EJECUCIONES ########
print("Resultado")
# change_name(rma, "Barcelona")
# print(rma)
# up_division(rma)
# print(rma)

# up_division(rma)
# print(rma)
# print(fcb)
# play_champions(fcb)
# print(fcb)

# TESTS

# up_division(bad)
# up_division(fcb)
# up_division(rma)

# print(bad)
# print(fcb)
# print(rma)

# Test down_division:

# Escenario básico: Equipo en primera o segunda división:
down_division(rma)
down_division(fcb)
print(rma)
print(fcb)
assert rma["division"] == 2
assert fcb["division"] == 3
# Escenario alternativo: Equipo sin división:
down_division(bad)
assert bad["division"] == 3
print(bad)

# Escenario alternativo: Equipo en tercera división:
down_division(rmac)
assert rmac["division"] == 3
print(rmac)

# change_name(bad2, "Nuevo")
# print(bad2)


## Test play_champions
# Escenario básico: el equipo está en primera y no juega champions
play_champions(betis)
assert betis["champions"] == True

