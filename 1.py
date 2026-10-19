
moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

def main():
    both_items = []
    msc_items = []
    kzn_items = []
    unic_items = 0

    for j in kazan:
        if j in moscow:
            both_items.append(j)
        elif j not in moscow:
            kzn_items.append(j)

    for j in moscow:
        if j not in kazan:
            msc_items.append(j)
            
    ##Нужно найти:

    ##- что можно забрать в любом из двух городов

    print(both_items)

    ##- что есть только в Казани

    print(kzn_items)

    ##- что есть только в Москве

    print(msc_items)

    ##- сколько разных товаров на обоих складах вместе

    unic_items = len(both_items)+ len(kzn_items)+ len(msc_items)
    print(unic_items)

if __name__ == '__main__':
    main()