def main():
    N = int(input())
    result = climbingStB(N)
    print (result)
    
"""
recursive solution
def climbingStA(N):
        
        if N <= 2:
              return N
        return climbingStA(N - 1) + climbingStA(N - 2)
"""

#dynammic programming solution
def climbingStB(N):
    onePos, twoPos = 1, 1

    for i in range(N-1):
         tmp = onePos
         onePos = onePos + twoPos
         twoPos = tmp
    return onePos

if __name__ == "__main__":
    main()


