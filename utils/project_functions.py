def exist_dvd(dvd_name, dvds_market):
    ''' check if a given film exist in the market

            input:
                dvd_name: strings
                dvds_market: dictionary {'key': 'value'}
            output:
                boolean
    '''

    if dvd_name in dvds_market['saga'] or dvd_name in dvds_market['others']:
        return True
    else:
        return False


def discounts(saga_dvds):
    ''' calculate discount ratio depends on selected films
        1: no discount
        .9: 10% discount
        .8: 20% discount

        input:
            saga_dvds: list
        output:
            discount: float
    '''
    discount = 1
    unique_dvds = []

    for dvd in saga_dvds:
        if dvd not in unique_dvds:
            unique_dvds.append(dvd)

    if len(unique_dvds) == 2:
        discount = .9
    elif len(unique_dvds) > 2:
        discount = .8

    return discount


def show_available_titles(dvds_market):
    ''' Show available dvd titles in the market
        input:
            dvds_market: dictionary {'key': 'value'}
        output:
            None
    '''
    for gender in dvds_market:
        print(f'gender: {gender}')
        for title in dvds_market[gender]:
            print(f'\t> {title}')

        print('')


def calculate_total_price(selected_dvds, dvds_market):
    ''' calculate total price of selected dvds

        input:
            selected_dvds: list of strings
            dvds_market: dictionary {'key': 'value'}
        output:
            float
    '''
    saga_list = []
    others_list = []

    print('Our available dvd titles:')
    for dvd in selected_dvds:
        if dvd in dvds_market['saga']:
            saga_list.append(dvd)
        else:
            others_list.append(dvd)

    return discounts(saga_list)*len(saga_list)*15 + len(others_list)*20
