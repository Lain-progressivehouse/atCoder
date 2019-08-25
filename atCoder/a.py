S = input()
N = 29
dp = [0] * N
dp[0] = 1
mul = 1

for i in reversed(range(len(S))):
  nextDP = [0] * N
  c = S[i]
  if c == "?":
    for k in range(10):  # 数字[0-9]
      for j in range(N):
        nextDP[(k * mul + j) % N] += dp[j]
  else:
    k = int(c)
    for j in range(N):
      nextDP[(k * mul + j) % N] += dp[j]
  mul *= 10
  mul %= N
  dp = nextDP

print(int(dp[14]))
