c_tempt=float(input("Enter temperature in Celsius: "))
print("Enter F for Fahrenheit and K for Kelvin")
choice=input("Convert to Fahrenheit or Kelvin? : ")
if choice=='F' or choice=='f':
    f_tempt=(c_tempt*9/5)+32
    print(f"{c_tempt} degree Celsius is equal to {f_tempt} degree Fahrenheit")
elif choice=='K' or choice=='k':
    k_tempt=c_tempt+273.15
    print(f"{c_tempt} degree Celsius is equal to {k_tempt} degree Kelvin")