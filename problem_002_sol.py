

N, M  = map(int, input().split())

data = list(map(int, input().split()))

y = max([min(data[i * M:(i + 1) * M]) for i in range(N)])

print("N : {}, M : {}, y : {}".format(N,M,y))
