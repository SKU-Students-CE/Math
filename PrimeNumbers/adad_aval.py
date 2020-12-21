from sys import stdout

def save(lister):

  prime = "".join(lister)
  
  file = open("prime_numbers.txt", "a")
  file.writelines(prime)
  file.close()


def find_primes(lower , upper):
  lister = []
  print("Prime numbers between {0} and {1}:\n".format(lower, upper))

  holder = 0
  for num in range(lower, upper + 1):
    holder += 1
    if holder > 10000:
      save(lister)
      holder = 0
      lister = []
      
    stdout.write('\r' + str("{}".format(num)))
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
          break
      else:
        lister.append(str(num) + ",")


find_primes(0,1000000000)

input("\nEnd")
