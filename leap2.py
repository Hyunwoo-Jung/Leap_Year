# Q. 1950년에서 2050년 사이의 '윤년'을 출력하는 프로그램을 작성하세요.
# 1. 4로 나누어떨어지는 해는 윤년
# 2. 100으로 나누어떨어지고 400으로 나누어떨어지지 않는 해는 윤년이 아니다

def leap(n):
    if n % 4 == 0:
        if (n % 100 == 0) and (n % 400 != 0):
            return False
        else:
            return True
    else:
        return False
    
for i in range(1950,2051):
    if leap(i):
        print(i, end = "년 ")