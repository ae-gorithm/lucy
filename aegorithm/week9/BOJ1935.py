# 후위표기식이란 루트노드를 제일 뒤에 표기하는 형태
# ABC*+DE/-
# => 이걸 중위표기식으로 나타내면?
# a + b * c - d / e = 6.20
# 1 + 2 * 3 - 4 / 5 = 1 + 6 - 0.8

# 변환 후 값 넣기
# 피연산자라면 리스트에 넣기
# 연산자를 만나면 리스트에서 빼기
def sum_postfix(n, postfix):
    operand = []
    
    for i in range(len(postfix)):
         entity = postfix[i]
            
         if entity in ["-", "+", "/", "*"]:
            operand2 = float(operand.pop())
            operand1 = float(operand.pop())
           
            if entity == "-":
                operand.append(operand1 - operand2)
            elif entity == "+":
                operand.append(operand1 + operand2)
            elif entity == "/":
                operand.append(operand1 / operand2)
            elif entity == "*":
                operand.append(operand1 * operand2)
            #print(operand)
         else:
            operand.append(float(entity))
            #print(operand)

    return operand[0]
            

# 입력
n = int(input())
tmp_postfix = list(map(str, input()))
numbers = []
for i in range(n):
    numbers.append(input())

for i in range(len(tmp_postfix)):
    if tmp_postfix[i] not in ["-", "+", "/", "*"]:
        target_alpha = ord(tmp_postfix[i]) - 65 # ord 사용 주의, 아스키 코드 넘버 65(대문자)
        tmp_postfix[i] = str(numbers[target_alpha])

result = sum_postfix(n, tmp_postfix)

# 출력
print(f"{result:.2f}")