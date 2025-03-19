personas =["jorge","pepe","maria"]
for i in personas:
    print(f"hola {i} te invito a venir a mi casa") 
print(personas[0], "no pudo venir")
personas[0] = "felix"
for i in personas:
    print(f"hola {i} te invito a venir a mi casa") 
print("conseguimos mas lugar")
personas.insert(0,"pedro")
personas.insert(3,"mario")
personas.append("luis")
for i in personas:
    print(f"hola {i} te invito a venir a mi casa") 
print("solo puedo invitar a dos personas")
for i in range(len(personas)-2):
    persona_eliminada = personas.pop(i-1)
    print(f"{persona_eliminada} lamento informarte que se cancela la invitacion")
for i in personas:
    print(f"hola {i} te invito a venir a mi casa") 
del personas[0:2]
print (personas)