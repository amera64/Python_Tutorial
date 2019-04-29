price = 1008000
good_credit = False

if good_credit:
    price = price*.10
    print(f"You will need to put down ${price}")
else:
    price = price * .20
    print(f"You will need to put down ${price}")

