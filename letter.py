char = input("Digite uma letra:")
vogais = {"a","e","i","o","u"}
VOGAIS = {"A","E","I","O","U"}

if char in vogais or char in VOGAIS:
  print(f"{char} é uma vogal.")
else:
  print(f"{char} é uma consoante.")
