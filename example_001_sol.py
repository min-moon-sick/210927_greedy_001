N = 1500

money = [500, 100, 50 , 10]
y = 0

for i in range(len(money)):
  print("i", i)
  y += int(N / money[i])
  N = N % money[i]  
  print("N:{}, y:{}".format(N, y))
  
  if N == 0 :
    print(y)
    break
