def main():

    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    both_items = moscow & kazan
    msc_items = moscow - kazan
    kzn_items = kazan - moscow
    unique_items = moscow | kazan

    # Нужно найти:

    # что можно забрать в любом из двух городов

    print(both_items)

    # что есть только в Казани

    print(kzn_items)

    # что есть только в Москве

    print(msc_items)

    # сколько разных товаров на обоих складах вместе

    print(len(unique_items))


if __name__ == '__main__':
    main()
