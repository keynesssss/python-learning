

def calculator():
    try:
        hours = float(input('how long your work today?'))
        if hours <= 0:
            print('、work hours must be greater than 0')
            return

        tips = float(input('How many tips did you make?'))
        if tips < 0:
            print('tips can not be negative')
            return

    except ValueError:
        print('Please enter a number')
        return

    hourly_tips = tips/hours

    print(f'your hourly tips rate is ${hourly_tips:.2f}')

    return hours,tips




def total_money(hours, tips):
    base_rate = 18
    total_income = base_rate * hours + tips
    hourly_income = total_income / hours

    print(f'Your total income is ${total_income:.2f}')
    print(f'Your hourly income is ${hourly_income:.2f}')


if __name__ == '__main__':
    result = calculator()
    if  result is not None:
        hours,tips = result

        total_money(hours,tips)

