### Primeiro Warmup
import random

num = [random.randint(1, 1000) for i in range(250)]

print("Números antes: ")
print(num)

num_reversed = list(reversed(num))
print("Números depois: ")
print(num_reversed)

### Segundo WARMUP

animais = ["onça", "tucano", "cachorro", "gato", "galinha", "elefante", "leão", "tigre", "porco", "vaca", "macaco",
           "sagui", "arara", "jacaré", "tuiuiú", "lobo", "pinguim", "urso", "peixe", "jaguatirica"]
animais_ordenados = sorted(animais)

with open('animais.csv', mode='w', newline="") as arquivo:
    for animal in animais:
        arquivo.write(f"{animal} \n")


