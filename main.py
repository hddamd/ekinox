# -*- coding: utf-8 -*-
from utils.project_functions import *

dvds_market = {
    'saga': ['back to the future 1', 'back to the future 2', 'back to the future 3'],
    'others': ['the goat', 'matrix', 'titanic']
}
shopping_cart = []


def main():
    # Enter
    try:
        show_available_titles(dvds_market)
        while True:
            dvd_name = input('Please enter film name: ')
            dvd_name = dvd_name.strip().lower()
            if exist_dvd(dvd_name, dvds_market):
                shopping_cart.append(dvd_name)
            else:
                print('title not found!')

    except KeyboardInterrupt:  # press (ctrl+c) to end dvd shopping and calculate total price
        total_price = calculate_total_price(shopping_cart, dvds_market)
        print('')
        print('selected titles:')
        print(*shopping_cart, sep='\n')
        print('!!FINISH!!.. Total: {:.2f} euros'.format(total_price))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
