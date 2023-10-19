from typing import Any

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

percent_off = {}
price = (puzzles * puzzle) * (puppets * puppet) * (teddies * teddy) * (minions * minion) * (trucks * truck)

delivery_quantity = puzzles + puppets + teddies + minions + trucks
if delivery_quantity >= 50:
    percent_off = (price * 25 / 100)

final_price = (price + percent_off)

if final_price >= trip:
    lv_left = final_price - trip
    print(f"Yes! {lv_left} lv left ")
else:
    lv_not_enough = trip - final_price
    f"not enough money! {lv_not_enough}lv needed."
