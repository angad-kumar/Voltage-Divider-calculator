Vin = float(input("Source Voltage(V): "))
Vout = float(input("Output Voltage(V):"))
A = float(input("Output Current(mA): "))

R_total = (Vin-Vout)/A
print("Total Resistor(KOhm): ", R_total)

R2 = (Vout*R_total)/Vin
print("Value of R2(KOhm): ", R2)
R1 = R_total - R2
print("Value of R1(Kohm): ", R1)
