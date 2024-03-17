numbers= input('Enter some numbers: ').split()
for x in range(0, len(numbers)):
    numbers[x]= int(numbers[x])
# i=0;
# for number in numbers:
#     sum=number+i
#     i+=number
# print(sum)
    
#or,
    
sum=0
for numb in numbers:
    sum+=numb
print(f'sum={sum}')

total_numbers=0
for numb in numbers:
    total_numbers+=1
avg=round(sum/total_numbers)
print(f'avg={avg}')