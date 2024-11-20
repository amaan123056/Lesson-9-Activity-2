units=int(input("Enter the units comsumed"))
if units<50:
    Amount=units*2.6
    Tax=25
elif units<=100:
    Amount=130+((units-50)*3.25)
    Tax=35
elif units<=200:
    Amount=130+162.5+((units-100)*50.25)
    Tax=45
else :
    Amount= 130+162.5+526((units-200*8.45))
    Tax=75
total_Amount=Amount+Tax
print("Electricity bill is equal to",total_Amount)




