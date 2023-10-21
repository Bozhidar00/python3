puzzle = 2.60
puppet = 3
teddy = 4.10
minion = 8.20
truck = 2

trip = float(input())
puzzles = float(input())
puppets = float(input())
teddies = float(input())
minions = float(input())
trucks = float(input())

price = (puzzles * puzzle) + (puppets * puppet) + (teddies * teddy) + (minions * minion) + (trucks * truck)

delivery_quantity = puzzles + puppets + teddies + minions + trucks
if delivery_quantity >= 50:
    price -= price * 0.25
    rent = price * 0.10
else:
    rent = price * 0.10

final_price = price - rent

if final_price >= trip:
    lv_left = final_price - trip
    print(f"Yes! {lv_left:.2f} lv left")
else:
    lv_not_enough = trip - final_price
    print(f"Not enough money! {lv_not_enough:.2f} lv needed.")
