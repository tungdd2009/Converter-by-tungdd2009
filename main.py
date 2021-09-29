print('Welcome to Converter by tungdd2009\n Keybinds:\n 1 for C to F\n 2 for F to C\n 3 for kg to pounds\n 4 for pounds to kg\n 5 for exit application')
Flag = True
while Flag == True:
  function = int(input(': '))
  if function == 1:
    C = float(input('Enter degree C: '))
    F = C * 1.8000 + 32.00
    print(C, 'degree C =', F, 'degree F')
  elif function == 2:
    F = float(input('Enter degree F: '))
    C = (F - 32) / 1.8000
    print(F, 'degree F =', C, 'degree C')
  elif function == 3:
    kg = float(input('Enter kilograms: '))
    lbs = kg * 2.204623
    print(kg, 'kg =', lbs, 'pounds')
  elif function == 4:
    lbs = float(input('Enter pounds: '))
    kg = lbs / 2.204623
    print(lbs, 'pounds =', kg, 'kg')
  elif function == 5:
    Flag = False
    print('Thank you for using my creation')
    break