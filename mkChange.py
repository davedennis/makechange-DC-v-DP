import sys

cache = []
coins = []
calls = 0
reads = 0

# read coin values
def readCoins(fnm):
   global coins
   global cache
   f = open(fnm)
   for line in f:
      l = line.strip().split(" ")
      for c in l:
        coins.append(int(c))

   if db: print("coins:", coins)

def mkChangeDC(n, c):
   global calls
   memoized = {}
   temp = coins.copy()
   temp.sort()
   temp.reverse()

   def cp(i, n):
      global calls

      if (i, n) in memoized:

         return memoized[(i, n)]
      if i >= len(temp):

         return 0
      max_coin = temp[i]
      if n == 0:

         return 1
      if n < 0:

         return 0
      if i == len(temp) - 1:
         if n % max_coin == 0:

            return 1
         else:

            return 0
      else:

         val = cp(i + 1, n) + cp(i, n - max_coin)
         memoized[(i, n)] = val
         return val

   retval = cp(0, n)
   return retval

def mkChangeDP(n):
   global reads

   dptable = [[0 for x in range(len(coins))] for x in range(n + 1)]

   for i in range(len(coins)):

      dptable[0][i] = 1

   for i in range(1, n + 1):
      for j in range(len(coins)):

         x = dptable[i - coins[j]][j] if i - coins[j] >= 0 else 0

         y = dptable[i][j - 1] if j >= 1 else 0

         dptable[i][j] = x + y

   return dptable[n][len(coins) - 1]


if __name__ == "__main__":

   db = len(sys.argv)>3
   n = int(sys.argv[1])
   fnm = sys.argv[2]
   readCoins(fnm)
   c = len(coins)-1
   ways = mkChangeDC(n,c)
   print("mkChangeDC")
   print("amount:", n, "coins:", coins, "ways:", ways, "calls:", calls)
   ways = mkChangeDP(n+1)
   print("mkChangeDP")
   print("amount:", n, "coins:", coins, "ways:", ways, "reads:", reads)
