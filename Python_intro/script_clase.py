def division(numero, divisor):
    try:
        return(numero/divisor)
    except ZeroDivisionError:
        print("Ops!Hoy estoy quemada")

print(division(3,2))
print(division(2,0))