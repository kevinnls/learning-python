total_cars = 345
cars_thrashed = {"the hulk":50,"superman":67,"batman":150}

print("Total Cars\t:",total_cars)
print("Thrashed")
for i in cars_thrashed:
    print("By",i.title()+"\t:",cars_thrashed[i])
sum_thrashed=0
for i in cars_thrashed.values():
    sum_thrashed+=int(i)
print("Cars remaining\t:",total_cars-sum_thrashed)
