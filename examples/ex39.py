#create a mapping of state to abbrevation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and soem cities in them

cities = {
    'CA' : 'San Fransisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

#add some more cities

cities['NY'] = 'Mew York'
cities['OR'] = 'Portland'

#print out cities

print('-'*10)
print("NY state has : ", cities['NY'])
print("OR state has: ", cities['OR'])

#print some states
print('-'*10)
print("Michihan's abbrevation is :", states['Michigan'])
print("Florida's abbrevation is :", states['Florida'])




