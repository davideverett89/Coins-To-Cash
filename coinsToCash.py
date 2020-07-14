def calc_dollars(**coins):
    total = 0
    for coin, amount in coins.items():
        if coin == 'pennies':
            total += amount * .01
        elif coin == 'nickels':
            total += amount * .05
        elif coin == 'dimes':
            total += amount * .1
        elif coin == 'quarters':
            total += amount * .25
    print(f'${total}')

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)