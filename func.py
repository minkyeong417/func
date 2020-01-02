def computepay(hrs,rate):
    if hrs<=40:
        return hrs * rate
    else:
        return 40 * rate + (hrs - 40) * rate * 1.5

sh = input('Enter hours: ')
sr = input('Enter rate: ')
fh = float(sh)
fr = float(sr)

print(computepay(fh,fr))
