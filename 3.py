##Есть список заказов:
##- `status` -  статус заказа
##  - `delivered` доставлен покупателю
 ## - `returned` возврат
##- `amount` — сумма заказа.

orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

def main():
    returned_sum = 0
    for i in orders:
        if i["status"] == "returned":
            returned_sum += i["amount"]

    ##Нужно найти:

    ##- на какую сумму оформили возвраты

    print(returned_sum)
    clients_return = list()
    for i in orders:
        if i["status"] == "returned":
            clients_return.append(i["buyer"])

    ####- кто хотя бы раз вернул заказ

    print(clients_return)
    cnt_delivered = 0
    sum_delivered = 0
    for i in orders:
        if i["status"] == "delivered":
            cnt_delivered += 1
            sum_delivered += i["amount"]

    ##- сколько заказов доставлено покупателю

    print(cnt_delivered)

    ##- средний чек доставленных заказов

    print(sum_delivered/cnt_delivered)
if __name__ == '__main__':
    main()