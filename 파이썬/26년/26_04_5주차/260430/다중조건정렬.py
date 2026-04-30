scores = [
    (80, 100),
    (100, 50),
    (70, 100),
    (80, 90)
]


''' 람다식을 통한 내림차순 정렬 '''
''' scores[0]을 기준으로 - 부호를 붙여 내림차순으로 정렬하고, 
[0] 점수가 같은 경우 [1]의 점수로 다시 내림차순 정렬 '''
scores.sort(key=lambda x: (-x[0], -x[1]))


for s in scores:
    print(f"english={s[0]}, math={s[1]}")


''' 딕셔너리 자료구조를 이용한 다중 조건 정렬 '''
scores = [
    {'english' : 80, 'math' : 100},
    {'english' : 100, 'math' : 50},
    {'english' : 70, 'math' : 100},
    {'english' : 80, 'math' : 90}
]

''' 동일하게 람다식 활용한 정렬 '''
''' math 점수를 기준으로 내림차순, 동일 시 english로 내림차순 '''
scores.sort(key=lambda x: (-x['math'], -x['english']))

for s in scores:
    print(s)