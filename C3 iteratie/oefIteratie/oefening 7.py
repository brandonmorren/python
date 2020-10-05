initial_limit = int(input("initial limit: "))
final_limit = int(input("final limit: "))

if initial_limit < final_limit:
    print("sum of numbers from " + str(initial_limit) + " till " + str(final_limit))
    sum = initial_limit
    for i in range(initial_limit + 1, final_limit + 1):
        sum += i
        print("+ " + str(i) + " --> " + str(sum))
else:
    print("the initial limit must be smaller than the final limit!")