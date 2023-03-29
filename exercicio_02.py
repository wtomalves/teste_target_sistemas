print("Sequência de Fibonacci")

antecessor = 0
sucessor = 1
fibonacci = 0

numero = int(input("Informe um número: "))

print(antecessor,end=" - ")
print(sucessor, end=" - ")
while fibonacci < numero:
  fibonacci = antecessor + sucessor
  antecessor = sucessor
  sucessor = fibonacci
  print(fibonacci, end=" - ")

  if fibonacci == numero:
    print("\nO número", numero, "está na sequência de Fibonacci")
    break
  else:
        if fibonacci > numero:
            print("\nO número", numero, "não está na sequência de Fibonacci")



