input = open('input.txt', 'r').read().strip()

input_list = list(input.splitlines())

increases = 0

for i, depth in enumerate(input_list):
    if (i < len(input_list) - 1 and i > 1):
        if int(input_list[i-2]) + int(input_list[i-1]) + int(depth) < int(input_list[i-1]) + int(depth) + int(input_list[i+1]):
            increases += 1

print("Result: {}".format(increases))
