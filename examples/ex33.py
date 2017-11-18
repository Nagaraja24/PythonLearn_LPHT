numbers = []

def increment(endValue, incrValue):
            i=0
            while i < endValue:
                print("At the top i is %d" %i)
                numbers.append(i)

                i = i + incrValue
                print("Numbers now: ", numbers)

                print("At the bottom i is %d" %i)

increment(8, 2)

print("The numbers : ")

for num in numbers:
    print(num)

