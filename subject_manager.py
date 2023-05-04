def manageSub(id):

    # 유저파일 읽기
    usersFile = open('users.txt', 'r', encoding='UTF8')
    usersFIleLines = usersFile.readlines()
    usersFile.close()

    # 교수이름과 교번 불러오기
    userList = []

    for line in usersFIleLines:
        elementsOfLine = line.strip().split('    ')
        
        userList.append(line)

        if (len(elementsOfLine) == 4):
            if (elementsOfLine[0] == id):
                userNum = elementsOfLine[2]
                userName = elementsOfLine[3]

    # 과목파일 읽기
    subFile = open('subjects.txt', 'r', encoding='UTF8')
    subFileLines = subFile.readlines()
    subFile.close()

    # 과목리스트 생성
    subList = []
    wholeSubList = []

    for line in subFileLines:
        elementsOfLine = line.strip().split('    ')

        # 전체 과목리스트
        wholeSubList.append(line)

        # 개인 과목리스트
        if(elementsOfLine[4] == userName + "(" + userNum + ")"):
            subList.append(line)
    
#==========================================================================================================================================================

    if(len(subList) == 0):
        print("\n개설하신 과목이 없습니다. 교수메뉴로 돌아갑니다.")
        print("================================================================================\n")
        return

    printSub(subList)

    print("-----------------------------------<개설철회>-----------------------------------")

    while True:
        print("개설 철회를 희망하시는 과목이 있으십니까? (Y/N) > ", end = "")
        yn = input()

        if (yn == "Y"):
           result = deleteSub(subList, wholeSubList, userList)

           if (result == 0):
               break
           
           if (result == 1):
               break

        elif (yn == "N"):
            print("\n교수메뉴로 돌아갑니다.")
            print("================================================================================\n")
            break

        else:
            print("다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")
        
#==========================================================================================================================================================

# 과목 출력
def printSub(subList):

    print("\n-----------------------------------<개설과목>-----------------------------------")
    for subject in subList:
        print(subject)

# 과목 개설 철회
def deleteSub(subList, wholeSubList, userList):
    
    while True:
        
        isExistID = False
        canDelete = False
        
        print("철회를 원하는 과목의 과목번호를 입력하시오(0 입력 시 취소) > ", end = "")
        inputSubID = input()

        # 유효성 평가
        # 1. 과목이 존재하는지 검사
        for subject in subList:
            elementsOfSubject = subject.strip().split('    ')
                
            if (inputSubID == elementsOfSubject[0]):
                isExistID = True
            
        # 2. 과목의 수강신청 학생수 검사
        if (isExistID):
            for subject in wholeSubList:
                elementsOfSubject = subject.strip().split('    ')

                if(inputSubID == elementsOfSubject[0] and elementsOfSubject[7] == "0"):
                    canDelete = True
                    print("과목정보: " + subject)

        # 유효한 경우
        if (canDelete):

            while True:
                print("정말로 철회하시겠습니까? (Y/N) > ", end = "")
                yn = input()

                if (yn == "Y"):
                    
                    # 과목파일에서 과목 제거
                    for ListIndex in wholeSubList:
                        if (inputSubID in ListIndex):
                            wholeSubList.remove(ListIndex)


                    # 유저파일에서 과목 제거
                    for ListIndex in userList:
                        if (inputSubID in ListIndex):
                            userList.remove(ListIndex)


                    # 과목파일 수정
                    subFile = open('subjects.txt', 'w', encoding='UTF8')

                    for line in wholeSubList:
                        subFile.write(line)

                    subFile.close()
                    
                    # 유저파일 수정
                    userFile = open('users.txt', 'w', encoding='UTF8')

                    for line in userList:
                        userFile.write(line)

                    userFile.close()

                    print("\n철회가 완료되었습니다. 교수메뉴로 돌아갑니다.")
                    print("================================================================================\n")
                    return 1

                elif (yn == "N"):
                    print("\n철회가 취소되었습니다. 교수메뉴로 돌아갑니다.")
                    print("================================================================================\n")
                    return 0

                else:
                    print("다시 입력해주세요.")
                    print("\n--------------------------------------------------------------------------------")

        # 과목철회를 취소할 경우
        elif (inputSubID == "0"):
            print("\n철회가 취소되었습니다. 교수메뉴로 돌아갑니다.")
            print("================================================================================\n")
            return 0
    
        # 과목이 존재하지 않는 경우
        elif (not isExistID):
            print("존재하지 않는 과목번호입니다. 다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")

        # 수강신청한 인원이 0명보다 많은 경우
        elif (isExistID and not canDelete):
            print("수강신청한 인원이 없는 경우에만 철회가 가능합니다. 다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")
        