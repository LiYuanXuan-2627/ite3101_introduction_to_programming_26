def hotel_cost(nights: int) -> int:
    return 140 * nights


def plane_ride_cost(city: str) -> int:
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days: int) -> int:
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


def trip_cost(city: str, days: int) -> int:
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)

input_city = input("Enter the city you are traveling to: ")
input_days = int(input("Enter the number of days you will be staying: "))
input_nights = int(input("Enter the number of nights you will be staying: "))
spending_money = 0
spending_money += input_city + input_days + input_nights
print(spending_money)