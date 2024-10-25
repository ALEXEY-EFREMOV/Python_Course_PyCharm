numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
i = 0
summa = 0
None_i = 0
while(i < len(numbers)):
   if numbers[i] !=None:
       summa+=numbers[i]
   else:
       None_i=i
   i+=1
Result = summa/len(numbers)
numbers[None_i] = Result
print("Измененный список:", numbers)
