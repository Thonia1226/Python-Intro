# 1. Input and print personal details
name = input("Enter your name: ")
designation = input("Enter your designation: ")
email = input("Enter your email address: ")
phone = input("Enter your phone number: ")

print("Personal Details:")
print("name")
print("designation")
print("email")
print("phone")

# 2. Picking a yellow ball
balls = ["black"] * 3 + ["yellow"] * 4 + ["white"] * 5
picked_ball = "yellow"  # For picking a yellow ball

if picked_ball in balls:
    print=(picked_ball), "I picked a yellow ball"

# 3. Adding cassava and checking for carrot
items = ["cucumber", "kola", "groundnut", "pineapple", "carrot", "grape"]






# 5. Remove kola from the list
if "kola" in items:
    items.remove("kola")
    print("Kola has been removed from the list.")

# 6. Addition of the numbers below
list1 = [12, 154, 79, 134, 3, 10]
total_sum = sum(list1)
print=(total_sum), "This is the sum of the numbers in list1"

if total_sum > 50:
    total_sum = (total_sum / 20) + 19
else:
    total_sum += 500

print=(total_sum), "Final total after condition"

# 7. Collecting items and prices from market
market_items = {}
Yam = 200
Cassava = 300
Groundnutoil = 500
Meat = 1000
Maize = 300

total_price = sum(market_items)
print("Items bought and their prices:")
for item, price in market_items.items():
    print(f"{item}: {price}")

print=(total_price), "Total amount spent"