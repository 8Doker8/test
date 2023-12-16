f = open("1.txt")
ints = []

try:
    for line in f:
        ints.append(int(line))
        print(ints)
except ValueError:
    print("Eto ne chislo")
except Exception as e:
    print("we got: ", e)
else:
    print("All good")
finally:
    f.close()
    print("File is closed")