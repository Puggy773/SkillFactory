sum=0
i=1
number=input('Enter number of tickets:\t')
try:
    int_number=int(number)
except ValueError:
    print(f'You entered: {number}')
    print('Please,try later')
else:
    if int_number < 0:
        print('Number of tickets cannot be negative')
    while i<=int_number:
        try:
            int_age = int(input(f'Enter user {i} age:\t'))
        except ValueError:
            print('Please,try later')
        else:
            if int_age<0:
                print('Age cannot be negative')
                int_age=(-1)*int_age
            elif 18<=int_age<=25:
                sum+=990
            elif int_age>25:
                sum+=1250
        i+=1
    if int_number > 3:
        sum = 0.9 * sum
print(sum)


