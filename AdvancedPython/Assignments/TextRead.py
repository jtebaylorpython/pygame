file = open("text.txt")

dictionary = {}

while 1:
    line = file.readline()
    kt = line.split(" ")

    if not line:
        break
    for i in kt:
        try:
            dictionary[i] = dictionary[i] + 1
        except KeyError:
            dictionary[i] = 1
for key in dictionary.keys():
    print(key, dictionary[key])
