with open("met_no_Sandefjord_Torp_SN27470.csv", "r") as met:
    lines = met.readlines()

data = []
c = 0
skip = 1
for l in lines:
    if c >= skip:
        try:
            t, p, w = map(float, l.split(",")) # temp, trykk, vind
            data.append([t, p, w])
        except ValueError as err:
            print(err)
    c += 1

print(data)