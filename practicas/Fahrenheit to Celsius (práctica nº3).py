

conversion_type = input("What kind of conversion do you wish to make?  (ºF > Cº / Cº > ºF): ").upper()
if conversion_type != "ºF > Cº' or 'Cº > Fº":
    print('Please select a valid conversion type')
initial_temp = input ("How many degrees do you wish to convert?: ")

if conversion_type == "ºF > Cº":
    end_temp = (int(initial_temp) -32)/1.8
    print("{} Fahrenheit degrees are {} Celsius degrees ".format(initial_temp, end_temp))

else:
    end_temp = int(initial_temp) * 1.8 +32
    print("{} Celsius degrees are {} Fahrenheit degrees ".format(initial_temp, end_temp))