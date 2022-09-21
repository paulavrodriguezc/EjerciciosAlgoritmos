capital=float(input("How much do you wish to invest?"))
annual_interest_rate=float(input("What is the annual interest rate applied to your investment?"))
time=int(input("For how many years will you invest?"))
print("You will obtain "+str(round(capital*(annual_interest_rate/100 + 1)*time, 2))+"$.")