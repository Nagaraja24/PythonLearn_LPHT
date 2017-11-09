people = 30
cars = 40
buses = 15

if cars > people:
    print("we should take cars")

elif cars < people:
    print("We should not take cars")

else:
    print("We cant decide")



if buses > cars:
    print("Thats too many buses")

elif buses < cars:
    print("May be we could take the buses")
else:
    print("We still cant decide")


if people > buses:
    print("Alright, lets take the buses")
else:
    print("Fine, lets stay home then")
