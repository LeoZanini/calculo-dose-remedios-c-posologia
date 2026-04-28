from datetime import datetime as dt, timedelta

class remedio:
    def __init__(self,nome,posologia,dias):
        self.nome = nome
        self.posologia = posologia
        self.dias = dias

lista_remedios = [
    remedio("cetoprofeno",12,5),
    remedio("amoxicilina",8,7),
    remedio("dipirona",6,4)
]

hoje = dt.today()
data_inicial = "2026-04-27T16:00:00"
prim_dose = dt.fromisoformat(data_inicial)

def calc_num_total_doses(poso,dias):
    doses_p_dia = 24//poso
    return (doses_p_dia * dias) -1

def cal_doses(poso,dias):
    num_tot_doses = calc_num_total_doses(poso,dias)
    lista_doses = list(prim_dose + timedelta(hours=poso) * i for i in range(num_tot_doses))
    return num_tot_doses, lista_doses

dias_finais=[]
def calc_remedios(poso,dias,nome):
    num_tot_doses = calc_num_total_doses(poso,dias)
    fim = prim_dose + timedelta(hours=poso) * num_tot_doses
    dias_finais.append({'dose':fim,'remedio':nome})


prox_doses = []
def calc_prox_dose(doses,rem_nome):
    counter = 0
    for dose in doses:
        if dose >= hoje and counter <1:
            counter+=1
            prox_doses.append({'dose':dose,'remedio':rem_nome})

def main():
    for rem in lista_remedios:
        num_tot_doses, lista_doses = cal_doses(rem.posologia,rem.dias)
        calc_remedios(rem.posologia,rem.dias,rem.nome)
        calc_prox_dose(lista_doses,rem.nome)

    prox_doses.sort(key=lambda x:x['dose'])
    dias_finais.sort(key=lambda x:x['dose'])
    numeral = 1
    for rem in prox_doses:
        print(f'{numeral}. Próxima dose às: {rem["dose"].strftime("%H:%M")} de {rem["remedio"]}')
        numeral+=1
    for dia in dias_finais:
        print(f'Dose final do {dia["remedio"]} : {dia["dose"]}')
    return prox_doses,dias_finais

main()





