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
