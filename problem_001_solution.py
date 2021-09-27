

N = 3 # 2번 줄 숫자 갯수
M = 4 # 총 길이
K = 3 # 연속 가능 횟수


list_input = [N, M, K]
y = 0
cnt = 0

data = list(range(N))

data.reverse()

print("data", data)

for i in range(1, M + 1):
  cnt = cnt + 1

  if cnt <= K :
    y = y + max(data)
  else:
    data_ = data
    data_.remove(max(data))
    y = y + max(data_)
    cnt = 0

print(y)
