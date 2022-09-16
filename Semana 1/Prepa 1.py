saldo_inicial=3480
fecha="2020/04/10"
print(f"Saldo actual a la fecha ({fecha}): ${saldo_inicial}\n")
saldo_actual=saldo_inicial-96
fecha="2020/04/11"
print("Se han retirado $96")
print(f"Saldo actual a la fecha ({fecha}): ${saldo_actual}\n")
saldo_actual+=1200
fecha="2020/04/17"
print("Se han recibido $1200")
print(f"Saldo actual a la fecha ({fecha}): ${saldo_actual}\n")
interes=round(saldo_actual*0.03, ndigits=2)
saldo_actual=saldo_actual+interes
fecha="2020/04/30"
print(f"Se han recibido ${interes}")
print(f"Saldo actual a la fecha ({fecha}): ${saldo_actual}\n")
fecha="2020/05/02"
saldo_actual-=51
print("Se han retirado $51")
print(f"Saldo actual a la fecha ({fecha}): ${saldo_actual}\n")