def prime_or_not():
    a = int(input('Enter a number to be checked whether prime or not: '))

    if a == 1:
        print('Number is neither prime nor composite')

    if a <= 0:
        print('Not defined')

    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                print('Number is composite')
                break

        else:
            print('Number is prime')
            # print(i)

    AskOkCancel = input('Do you want to continue? (y/n):')

    if AskOkCancel == 'y':
        prime_or_not()

    else:
        print('Thanks!')

prime_or_not()
input()

