# 로그인 상태를 나타내는 전역변수
def login():
    
    print("\n------------------------------------<로그인>------------------------------------")
    isLoggedIn = False
    isStudent = True

    # 5회 이상 틀리면 시작 페이지로
    failCount = 0

    while True:
        id = input("ID 입력 > ")
        pw = input("PW 입력 > ")

        # 파일 읽기
        usersFile = open('users.txt', 'r', encoding="UTF-8")
        usersFileLines = usersFile.readlines()
        usersFile.close()

        for line in usersFileLines:
            elementsOfLine = line.strip().split('    ')

            if len(elementsOfLine) == 5:
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

                    return isLoggedIn, isStudent, id
                
        failCount = failCount + 1

        if failCount == 5:
            print("\n5회 틀렸습니다. 시작화면으로 돌아갑니다.")
            print("================================================================================\n")

            return isLoggedIn, isStudent, id
        
        print("\n" + str(failCount) + "회 틀렸습니다.")
        print("--------------------------------------------------------------------------------")
                    
       
            
def removeID():

    print("\n-----------------------------------<계정탈퇴>-----------------------------------")
    isLoggedIn = False
    count = 0
    lineNumToDel = 0

    # 5회 이상 틀리면 시작 페이지로
    failCount = 0

    while True:

        isProfessor = False
        isStudent = False

        id = input("ID 입력 > ")
        pw = input("PW 입력 > ")

        # 파일 읽기
        usersFile = open('users.txt', 'r', encoding="UTF-8")
        usersFileLines = usersFile.readlines()
        usersFile.close()
        
        
        for line in usersFileLines:
            elementsOfLine = line.strip().split('    ')
            
            if isLoggedIn == True and count == 1:
                count += 1

                # 신청 과목이 있는 경우
                if len(elementsOfLine) > 5:
                    if (isProfessor):
                        print("\n개설한 과목이 있습니다. 개설한 과목을 모두 철회한 뒤 다시 시도해주세요.")
                        print("================================================================================\n")
                        return

                    elif (isStudent):
                        print("\n수강신청한 과목이 있습니다. 수강신청한 과목을 모두 철회한 뒤 다시 시도해주세요.")
                        print("================================================================================\n")
                        return
                
                if len(elementsOfLine) == 1:
                    # 삭제 진행
                    print("정말 탈퇴하시겠습니까? (Y/N) > ", end = "")
                    yn = input()

                    # 공백 제거
                    yn = yn.replace(" ", "")
                    if yn == "Y":
                        remove_line_from_file('users.txt', lineNumToDel)
                        print("\n계정탈퇴가 완료되었습니다. 시작화면으로 돌아갑니다.")
                        print("================================================================================\n")
                        return
                    
                    elif yn == "N":
                        print("\n계정탈퇴를 취소하셨습니다. 시작화면으로 돌아갑니다.")
                        print("================================================================================\n")
                        return

            if len(elementsOfLine) == 5:
                lineId = elementsOfLine[0]
                linePw = elementsOfLine[1]
                userId = elementsOfLine[2]

                # id 대분자로 둘 다 바꾼 뒤 동치비교, pw 동치비교
                if id.upper() == lineId.upper() and pw == linePw:
                    lineNumToDel += 1

                    # 로그인 상태를 True로 변경 
                    isLoggedIn = True
                    count += 1

                    # 교수사용자인지 혹은 학생사용자인지 구분
                    if(len(userId) == 4):
                        isProfessor = True

                    elif(len(userId) == 5):
                        isStudent = True
                    
        failCount = failCount + 1

        if failCount == 5:
            print("\n5회 틀렸습니다. 시작화면으로 돌아갑니다.")
            print("================================================================================\n")

            return isLoggedIn, id
        
        print("\n" + str(failCount) + "회 틀렸습니다.")
        print("--------------------------------------------------------------------------------")
                    
                    
                    
def remove_line_from_file(filename, line_number):
    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove the specified line
    if line_number < 1 or line_number > len(lines):
        print("Invalid line number.")
        return

    del lines[line_number - 1]
    del lines[line_number - 1]

    # Write the modified contents back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)

    print(f"Line {line_number} removed from {filename}.")