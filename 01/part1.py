input = open('input.txt', 'r').read().strip()

input_list = list(input.splitlines())

increases = 0

for i, depth in enumerate(input_list):
    if int(depth) > int(input_list[i-1]):
        increases += 1

print("Result: {}".format(increases))
