def working_income_info():
    while True:
        try:
            hours = float(input('Please enter the hours you work?'))

            if hours <= 0:
                print('Please enter a positive number')
                continue

            print(f'you total working hour is {hours:.2f} hours')

            break


        except ValueError:
            print('Please enter a number')



    while True:
        try:
            tips = float(input('Please enter the tips you work?'))

            if tips < 0:
                print('Tips cannot be negative')
                continue

            print(f'you total tips is {tips:.2f} dollars')

            break


        except ValueError:
            print('Please enter a number')




    while True:
        try:
            base_rate = float(input('Please enter the base rate?'))
            if base_rate < 0:
                print('Please enter the base rate')
                continue
            break


        except ValueError:
            print('Please enter a number')

    return hours, tips, base_rate

def working_income_cal(hours, tips, base_rate):
    total_income = base_rate * hours+tips
    hourly_income = total_income / hours

    print(f'you total income is {total_income:.2f} dollars')
    print(f"your hourly income is {hourly_income:.2f} dollars")


if __name__ == '__main__':
    hours, tips, base_rate = working_income_info()
    working_income_cal(hours, tips, base_rate)


