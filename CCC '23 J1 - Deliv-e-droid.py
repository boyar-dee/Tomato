P = int(input())
C = int(input())
Score = 50 * P - 10 * C
if P > C:
    Score += 500
print(Score)