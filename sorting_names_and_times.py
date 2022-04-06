
names = ["jon","ben","kevin","chris"]
vals = [5,10,3,2]
sorted_names = []
sorted_vals = [5,10,3,2]

# Sorting the names by looking at the corresponding time
# grabbing the index of that time and then using that index
# we search for the name corresponding to the time
# then we simply add that name to an array for sorted names
# we do that until we run out of times to check
for i in range(len(vals)):
    sorted_names.append(names[vals.index(min(vals))])
    names.remove(names[vals.index(min(vals))])
    vals.remove(min(vals))

print(sorted_names)

# Sorting the times using the bubble sort algorithm
for i in range(len(sorted_vals)):
    for j in range(0, len(sorted_vals) - i - 1):
        if sorted_vals[j] > sorted_vals[j+1]:
            temp = sorted_vals[j]
            sorted_vals[j] = sorted_vals[j+1]
            sorted_vals[j+1] = temp

print(sorted_vals)