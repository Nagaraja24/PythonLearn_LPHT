cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avg_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars Available")
print ("Theer are only", drivers, " drivers available")
print ("There will be ", cars_not_driven, " empty cars available")
print ("We can transport ", carpool_capacity, "peoples today")