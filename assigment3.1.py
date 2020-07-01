hour= input("enter the time:")
rate= input("enter the rate:")
hour= float(hour)
rate= float(rate)
if hour<=40:
    pay=rate*hour
    pass
else:
    pay=40*rate+(rate*1.5*(hour-40))

print(pay)
    
