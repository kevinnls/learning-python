total_cars = 345
cars_damaged = {"the hulk":{"thrashed":50},"superman":{"destroyed":67},"batman":{"has blasted":150}}

print("Total Cars\t:",total_cars)
print("\nDamaged")
sum_damaged=0
for person in cars_damaged:
    for action in cars_damaged[person]:
        print(person.title(),action,"\t:",cars_damaged[person][action])
        sum_damaged+=cars_damaged[person][action]
print("\nCars remaining\t:",total_cars-sum_damaged)
