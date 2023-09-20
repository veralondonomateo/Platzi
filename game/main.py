import random
option = ('piedra', 'papel' , 'tijera')
print('Bienvenido a guerra.py')
print('Elige tu ataque')
user_option = input('Piedra, Papel o Tijera => ') 
user_option = user_option.lower()
if not user_option in option:
  print('Esa opción no es valida')

computer_option = random.choice(option)
if user_option == computer_option:
  print('Empate') 
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('Ganaste, El pc eligio Tijera')
  elif computer_option == 'papel':
    print('Perdiste, El pc eligio Papel')
elif user_option == 'tijera':
  if computer_option == 'piedra':
    print('Perdiste, El pc eligio Piedra')
  elif computer_option == 'papel':
    print('Ganaste, El pc eligió papel')
elif user_option == 'papel':
  if computer_option == 'piedra':
    print('Ganaste, el pc eligio Piedra')
  elif computer_option == 'tijera':
    print('Perdiste, el pc eligió Tijera') 

