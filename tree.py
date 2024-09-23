input_file = open("input.txt", "r")
lines = input_file.readlines()
input_file.close()

print(int(lines[0].strip()) - len(lines))