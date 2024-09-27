horaspt = int(input("Que horas sao: "))
minutos = int(input("Que minutos são:"))

if horaspt < 12:
    print(f"\nFormato americano: {horaspt}h{minutos}AM\n")
    
if horaspt > 12:
    horasusa = horaspt - 12
    print(f"\nFormato americano: {horasusa}h{minutos} PM\n")