import os


backups_dir='backups'

carpetas=sorted(os.listdir(backups_dir))

for i,c in enumerate(carpetas):
    fecha=c.split("data")[1].split(".db")[0]
    print(i,"fecha:", fecha)
 
decision=input('¿Qué backup quieres restaurar?: ')
print("De locos, restauremos el archivo ",carpetas[int(decision)] )
