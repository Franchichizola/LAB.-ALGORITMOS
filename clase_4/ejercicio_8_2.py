personas =["jorge","pepe","maria"]
for i in personas:
    print(f"hola {i} te invito a venir a mi casa") 
print(personas[0], "no pudo venir")
personas[0] = "felix"
for i in personas:
    print(f"hola {i} te invito a venir a mi casa") 
