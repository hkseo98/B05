# 로그인 상태를 나타내는 전역변수
def login():
    isLoggedIn = False
    isStudent = True
    print("\n<로그인>")
    failCount = 0
    # 5회 이상 틀리면 시작 페이지로
    while True:
        id = input("ID 입력 > ")
        pw = input("PW 입력 > ")
        # 파일 읽기
        usersFile = open('users.txt', 'r')
        usersFileLines = usersFile.readlines()
        usersFile.close()

        for line in usersFileLines:
            elementsOfLine = line.strip().split('    ')
            if len(elementsOfLine) == 4:
                lineId = elementsOfLine[0]
                linePw = elementsOfLine[1]
                # id 대분자로 둘 다 바꾼 뒤 동치비교, pw 동치비교
                if id.upper() == lineId.upper() and pw == linePw:
                    print("로그인 성공")
                    # 로그인 상태를 True로 변경 
                    isLoggedIn = True
                    # 학생인지 교수인지 여부 설정
                    # 학번이 5자리면 학생
                    isStudent = len(elementsOfLine[2]) == 5
                    return isLoggedIn, isStudent
        failCount = failCount + 1
        if failCount == 5:
            print("\n5회 틀렸습니다. 시작 화면으로 돌아갑니다.\n")
            return isLoggedIn, isStudent
        print("\n" + str(failCount) + "회 틀렸습니다.\n")
                    
       
            
 