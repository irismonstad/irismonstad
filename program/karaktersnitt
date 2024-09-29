#Regner ut skolepoeng (det man søker universitet med i ordf) ved alle fordelinger av seksere og femmere
#Totalt 16 fag, 24 karakterer (regner med ingen eksamen i vg1)

seksere = 24
femmere = 0

snitt = {}

for i in range(24):
    poeng = ((seksere*6 + femmere*5)/24)*10 #Regner ut karakterpoeng
    snitt[femmere +1] = round(poeng, 2) +4 #Regner ut skolepoeng (gitt maks tilleggspoeng, ingen kjønnspoeng inkludert), og legger skolepoeng til i snitt
    seksere -= 1
    femmere += 1

for key, value in snitt.items():
    print(f"{key : >2}: {value : >4}")

