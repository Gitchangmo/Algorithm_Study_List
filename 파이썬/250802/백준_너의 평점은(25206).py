import sys
input = sys.stdin.readline

grade_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
               'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
               'F': 0.0}
sum = 0.0
total_score = 0.0
for i in range(20):
    name, score, grade = input().split()
    score = float(score)
    if grade == 'P':
        continue
    grade = grade_score.get(grade)
    total_score += score
    sum += score * grade
    
result = sum/total_score
print(f"{result:.6f}")
    