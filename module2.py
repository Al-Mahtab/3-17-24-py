# numbers=input('Give all the numbers: ').split()
# for number in range(0, len(numbers)):
#     numbers[number]=int(numbers[number])
# bigger_one=0
# for numb in numbers:
#     if numb>bigger_one:
#         bigger_one=numb
# print(f'The larger number is {bigger_one}')

# sum=0;
# for number in range(0,101,2):
#     sum=sum+number
# print(sum+1)

for x in range (0,100):
    if x%3==0 and x%5==0:
        print('Fizz buzz')

    elif x%3==0:
        print("Fizz")

    elif x%5==0:
        print('Buzzz')
        
    else:
        print(x)