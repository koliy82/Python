print("Напишите количество чисел:")
count = int(input())+1
actualcount = 1
print("Введите первое число:")
res = int(input())
while(actualcount!=count):
    print(f"Введите Действие для числа №{actualcount} (+ - * /):")
    action = input()
    print("Введите число:")
    number = int(input())
    if(action=="+"):
        res+=number
    elif(action=="-"):
        res-=number
    elif(action=="*"):
        res*=number
    elif(action=="/" and number!=0):
        res/=number
    else:
        print("Неверное действие")
    actualcount+=1
    print("Первое число = ",res)
print("Конечный результат:",res)