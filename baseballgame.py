def minimum_days_to_reach_goal(a, b, n):
    def contains_seven(day):
        return '7' in str(day)
    
    total_points = 0
    days = 0
    
    while total_points < n:
        days += 1
        total_points += a
        if contains_seven(days):
            total_points += b
    
    return days

# Reading input from standard input
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    a = int(data[0])
    b = int(data[1])
    n = int(data[2])
    
    result = minimum_days_to_reach_goal(a, b, n)
    print(result)
