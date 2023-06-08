import re

def reviseSubject(id):

   # 유저파일 읽기
    usersFile = open('users.txt', 'r', encoding='UTF8')
    usersFIleLines = usersFile.readlines()
    usersFile.close()

    # 교수이름과 교번 불러오기
    userList = []

    for line in usersFIleLines:
        elementsOfLine = line.strip().split('    ')

        userList.append(line)

        if (len(elementsOfLine) == 5):
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
        if (elementsOfLine[4] == userName + "(" + userNum + ")"):
            subList.append(line)

# ==========================================================================================================================================================

    if (len(subList) == 0):
        print("\n개설하신 과목이 없습니다. 교수메뉴로 돌아갑니다.")
        print("================================================================================\n")
        return

    printSub(subList)

    print("--------------------------------<과목정보 수정>---------------------------------")

    while True:

        print("정보 수정을 희망하시는 과목이 있으십니까? (Y/N) > ", end="")
        yn = input()

        if (yn == "Y"):
           result = revise(subList, wholeSubList, userList, userName, userNum)

           if (result == 0):
               break

        elif (yn == "N"):
            print("\n교수메뉴로 돌아갑니다.")
            print("================================================================================\n")
            break

        else:
            print("다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")


# 과목 출력
def printSub(subList):

    print("\n-----------------------------------<개설과목>-----------------------------------")
    for subject in subList:
        print(subject)

# 과목정보 수정
def revise(subList, wholeSubList, userList, userName, userNum):

    while True:

        isExistID = False

        print("정보 수정을 원하는 과목의 과목번호를 입력하시오(0 입력 시 취소) > ", end="")
        inputSubID = input()

        # 유효성 평가
        # 1. 과목이 존재하는지 검사
        for subject in subList:
            elementsOfSubject = subject.strip().split('    ')

            if (inputSubID == elementsOfSubject[0]):
                isExistID = True
                print("과목정보: " + subject)

                subID = elementsOfSubject[0]
                subClass = elementsOfSubject[1]
                oldCredit = elementsOfSubject[2]
                oldName = elementsOfSubject[3]
                oldTime = elementsOfSubject[5]
                oldPlace = elementsOfSubject[6]
                participantsNum = elementsOfSubject[7] 
                oldMaxAvb = elementsOfSubject[8]
                oldRestricted = elementsOfSubject[9]
                subMajor = elementsOfSubject[10]

        # 유효한 경우
        if (isExistID):
                subName = reSubName(oldName, wholeSubList)
                subTime, subCredit = reSubTime(oldTime, oldCredit, oldPlace,participantsNum, subList, wholeSubList)

                if(subTime == 0):
                    print("\n과목정보 수정이 취소되었습니다. 교수메뉴로 돌아갑니다.")
                    print("================================================================================\n")
                    return 0 
                
                subPlace = reSubPlace(subTime, oldPlace, participantsNum, oldMaxAvb, wholeSubList)
                maxAvailable = reMaxAvailable(oldMaxAvb, participantsNum, subPlace)

                if(subID[0] == "A"):
                    isRestricted = reIsRestricted(oldRestricted, participantsNum, subMajor)
                elif(subID[0] == "B"):
                    isRestricted = oldRestricted

                # 파일 수정
                newSubinSub = subID + "    " + subClass + "    " + subCredit + "    " + subName + "    " + userName+"("+userNum+")" + "    " + subTime + "    " + subPlace + "    " + participantsNum + "    " + maxAvailable + "    " + isRestricted + "    " + subMajor + "\n" 
                newSubinUser = subID + "    " + subClass + "    " + subCredit + "    " + subName + "    " + userName+"("+userNum+")" + "    " + subTime + "    " + subPlace + "    " + isRestricted + "    " + subMajor + "\n" 

                # 유저파일 수정
                for line in userList:
                    elementsOfLine = line.strip().split('    ')

                    if(elementsOfLine[0] == subID):
                        userList[userList.index(line)] = newSubinUser

                usersFile = open('users.txt', 'w', encoding='UTF8')
    
                for line in userList:
                    usersFile.write(line)
                
                usersFile.close()

                # 과목파일 수정
                for line in wholeSubList:
                    elementsOfLine = line.strip().split('    ')

                    if(elementsOfLine[0] == subID):
                        wholeSubList[wholeSubList.index(line)] = newSubinSub

                subFile = open('subjects.txt', 'w', encoding='UTF8')

                for line in wholeSubList:
                    subFile.write(line)

                subFile.close()

                print("\n과목정보 수정이 완료되었습니다. 교수메뉴로 돌아갑니다.")
                print("================================================================================\n")
                return 0
                    
        # 정보수정을 취소할 경우
        elif (inputSubID == "0"):
            print("\n과목정보 수정이 취소되었습니다. 교수메뉴로 돌아갑니다.")
            print("================================================================================\n")
            return 0
    
        # 과목이 존재하지 않는 경우
        elif (not isExistID):
            print("존재하지 않는 과목번호입니다. 다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")

# ==========================================================================================================================================================

def reSubName(oldName, wholeSubList):

    subNamePattern = re.compile(r'^[a-zA-Z0-9가-힣]+$')

    while True: 

        isExist = False

        print("과목명을 수정하시겠습니까? (Y/N) > ", end = "")
        reivseDecision = input()

        if(reivseDecision == "Y"):

            print("과목명 입력 > ", end = "")
            subName = input()

            # 공백 제거
            subName = subName.replace(" ", "")

            # 유효성 평가
            # 1. 문자열 길이 검사
            if (len(subName) < 3 or len(subName) > 10):
                print("과목명은 3~10글자로 구성되어야 합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 2. 한글, 숫자, 알파벳 이외의 문자가 있는지 검사
            elif (not subNamePattern.match(subName)):
                print("한글, 숫자, 알파벳 외의 글자는 입력 불가능합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 3. 숫자로만 구성되어 있는지 검사
            elif (subName.isnumeric()):
                print("과목명은 숫자만으로 구성될 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue
            
            # 4. 현재 과목명과 동일한지 검사
            elif (oldName == subName):
                print("현재 과목명과 동일합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue
            
            # 5. 중복되는 과목명이 있는지 검사
            for subject in wholeSubList:
                elementsOfSubject = subject.strip().split('    ')

                if(elementsOfSubject[3] == subName):
                    isExist = True
                    break

            if (isExist):
                print("과목명 수정시에는 다른 과목과 중복되는 과목명을 사용할 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            return subName
        
        elif (reivseDecision == "N"):
            return oldName
        
        else:
            print("다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")

def reSubTime(oldTime, oldCredit, oldPlace,participantsNum, subList, wholeSubList):

    print("")

    while True: 
        
        isPass = True
        
        print("강의시간을 수정하시겠습니까? (Y/N) > ", end = "")
        reivseDecision = input()

        if(reivseDecision == "Y"):

            if(int(participantsNum) > 0):
                print("수강신청한 인원이 없는 경우에만 강의시간을 수정할 수 있습니다.")
                print("\n--------------------------------------------------------------------------------")
                continue
            
        # 강의요일 입력
            possibleDay = ["월", "화", "수", "목", "금"]

            print("강의요일 입력 > ", end = "")
            subDay = input()

            # 공백 제거
            subDay = subDay.replace(" ", "")

            # 유효성 평가
            if (subDay not in possibleDay):
                print("요일은 '월, 화, 수, 목, 금'만 입력가능합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue
                
        # 강의 시작교시 입력
            print("강의 시작교시 입력(0 입력 시 취소) > ", end = "")
            subStart = input()

            if(subStart == "0"):
                return 0, 0

        # 1. 시작교시 유효성 평가
            # 1.1 숫자로만 구성되어 있는지 검사
            if (not subStart.isnumeric()):
                print("숫자 외의 다른문자는 입력할 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue
        
            # 1.2 숫자 검사
            if (len(subStart) != 1):
                print("강의교시는 '1,2,3,4,5,6,7,8'만 입력가능합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 정수화
            subStart = int(subStart)

            # 1.3 강의가능 교시인지 검사
            if (subStart < 1 or subStart > 8):
                print("강의는 1교시부터 8교시까지만 가능합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue


            #강의 종료교시 입력
            print("강의 종료교시 입력(0 입력 시 취소) > ", end = "")
            subFinish = input()

            if(subFinish == "0"):
                return 0, 0

            # 2. 종료교시 유효성 평가
            # 2.1 숫자로만 구성되어 있는지 검사
            if (not subFinish.isnumeric()):
                print("숫자 외의 다른문자는 입력할 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 2.2 숫자 검사
            if (len(subFinish) != 1):
                    print("강의교시는 '1,2,3,4,5,6,7,8'만 입력가능합니다. 다시 입력해주세요.")
                    print("\n--------------------------------------------------------------------------------")
                    continue

            # 정수화
            subFinish = int(subFinish)

            # 2.3 강의가능 교시인지 검사
            if (subFinish < 1 or subFinish >8):
                print("강의는 1교시부터 8교시까지만 가능합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 2.4 시작교시 이후인지 검사
            if (subFinish < subStart):
                print("강의종료는 강의시작 후에 이루어져야 합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 2.5 총 강의시간 검사
            if (subFinish - subStart > 3):
                print("강의시간은 3시간을 초과할 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 2.6 기존 강의시간과 동일한지 검사
            if(oldTime == subDay+str(subStart)+str(subFinish)):
                print("현재 강의시간과 동일합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 2.7 강의시간 중복 검사
            for existSub in subList:
                elementsOfSub = existSub.split('    ')

                existTime = elementsOfSub[5]

                existDay = existTime[0]
                existStartTime = int(existTime[1])
                existFinishTime = int(existTime[2])

                if (subDay == existDay):
                    if (existStartTime <= subStart and subStart <= existFinishTime):
                        print("타 과목과 강의시간이 겹칩니다. 다시 입력해주세요.")
                        print("\n--------------------------------------------------------------------------------")
                        isPass = False
                        break
                        
                    elif (existStartTime <= subFinish and subFinish <= existFinishTime):
                        print("타 과목과 강의시간이 겹칩니다. 다시 입력해주세요.")
                        print("\n--------------------------------------------------------------------------------")
                        isPass = False
                        break
                    
                    elif (subStart <= existStartTime and existFinishTime <= subFinish):
                        print("타 과목과 강의시간이 겹칩니다. 다시 입력해주세요.")
                        print("\n--------------------------------------------------------------------------------")
                        isPass = False
                        break
                
                # 강의실 중복 검사
                for existSub in wholeSubList:
                    elementsOfSub = existSub.split('    ')

                    existPlace = elementsOfSub[6]
                    existTime = elementsOfSub[5]

                    existDay = existTime[0]
                    existStartTime = int(existTime[1])
                    existFinishTime = int(existTime[2])

                    if(existPlace == oldPlace):
                        if(existDay == subDay):
                            if (existStartTime <= subStart and subStart <= existFinishTime):
                                print("타 교수가 개설한 과목과 강의시간 및 강의실이 겹칩니다. 다시 입력해주세요.")
                                print("\n--------------------------------------------------------------------------------")
                                isPass = False
                                break

                            elif (existStartTime <= subFinish and subFinish <= existFinishTime):
                                print("타 교수가 개설한 과목과 강의시간 및 강의실이 겹칩니다. 다시 입력해주세요.")
                                print("\n--------------------------------------------------------------------------------")
                                isPass = False
                                break

                            elif (subStart <= existStartTime and existFinishTime <= subFinish):
                                print("타 교수가 개설한 과목과 강의시간 및 강의실이 겹칩니다. 다시 입력해주세요.")
                                print("\n--------------------------------------------------------------------------------")
                                isPass = False
                                break

                if (not isPass):
                    break

                elif (isPass):    
                    subCredit = subFinish - subStart + 1
                    subTime = subDay + str(subStart) + str(subFinish)

                    return subTime, str(subCredit)

        elif (reivseDecision == "N"):
            return oldTime, oldCredit
        
        else:
            print("다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")

def reSubPlace(subTime, oldPlace, participantsNum, oldMaxAvb, wholeSubList):

    print("")

    possiblePlace = re.compile("[새산공][1-9][0-9][0-9]")

    while True: 
        print("강의장소를 수정하시겠습니까? (Y/N) > ", end = "")
        reivseDecision = input()

        if(reivseDecision == "Y"):

            isPass = True

            print("강의장소 입력 > ", end = "")
            subPlace = input()

            # 공백 제거
            subPlace = subPlace.replace(" ", "")

            # 유효성 평가
            # 1. 문자열 길이 검사
            if(len(subPlace) != 4):
                print("강의장소는 건물이름 새,산,공 중 하나와 3자리의 강의실 번호로 구성됩니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue
            
            if(subPlace[1] == "0"):
                print("강의실 번호의 첫번째 자리 숫자가 0일 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 2. 문법 검사
            if(possiblePlace.match(subPlace) == None):
                print("강의장소는 건물이름 새,산,공 중 하나와 3자리의 강의실 번호로 구성됩니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue
            
            # 3.기존 강의장소와 동일한지 검사
            if(oldPlace == subPlace):
                print("현재 강의장소와 동일합니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue
            
            # 4. 수강신청 중인 인원이 강의실의 최대 수용인원수보다 많은지 검사
            if(subPlace[0] == "새" and int(participantsNum) > 20):
                print("강의실에 따른 최대 수강가능 인원보다 수강신청한 인원이 많습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            elif(subPlace[0] == "산" and int(participantsNum) > 30):
                print("강의실에 따른 최대 수강가능 인원보다 수강신청한 인원이 많습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            elif(subPlace[0] == "공" and int(participantsNum) > 40):
                print("강의실에 따른 최대 수강가능 인원보다 수강신청한 인원이 많습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 5. 현재 최대 수강가능 인원이 강의실의 최대 수용인원수보다 많은지 검사
            if(subPlace[0] == "새" and int(oldMaxAvb) > 20):
                print("강의실에 따른 최대 수강가능 인원이 과목의 수강가능 인원보다 작습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            elif(subPlace[0] == "산" and int(oldMaxAvb) > 30):
                print("강의실에 따른 최대 수강가능 인원이 과목의 수강가능 인원보다 작습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            elif(subPlace[0] == "공" and int(oldMaxAvb) > 40):
                print("강의실에 따른 최대 수강가능 인원이 과목의 수강가능 인원보다 작습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 6. 강의실 중복 검사
            for existSub in wholeSubList:
                elementsOfSub = existSub.split('    ')

                existPlace = elementsOfSub[6]
                existTime = elementsOfSub[5]

                existDay = existTime[0]
                existStartTime = existTime[1]
                existFinishTime = existTime[2]

                subDay = subTime[0]
                subStart = subTime[1]
                subFinish = subTime[2]

                if(existPlace == subPlace):
                    if(existDay == subDay):
                        if (existStartTime <= subStart and subStart <= existFinishTime):
                            print("이미 개설된 과목과 강의시간 및 강의실이 겹칩니다. 다시 입력해주세요.")
                            print("\n--------------------------------------------------------------------------------")
                            isPass = False
                            break

                        elif (existStartTime <= subFinish and subFinish <= existFinishTime):
                            print("이미 개설된 과목과 강의시간 및 강의실이 겹칩니다. 다시 입력해주세요.")
                            print("\n--------------------------------------------------------------------------------")
                            isPass = False
                            break

                        elif (subStart <= existStartTime and existFinishTime <= subFinish):
                            print("이미 개설된 과목과 강의시간 및 강의실이 겹칩니다. 다시 입력해주세요.")
                            print("\n--------------------------------------------------------------------------------")
                            isPass = False
                            break
                    
            if(isPass):        
                return subPlace
                
        elif (reivseDecision == "N"):
                return oldPlace
            
        else:
            print("다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")

def reMaxAvailable(oldMaxAvb, participantsNum, subPlace):
    
    print("")

    numPattern = re.compile("[0-9]+")

    # 새: 10~20, 산: 10~30, 공: 10~40
    while True:

        print("수강가능 인원을 수정하시겠습니까? (Y/N) > ", end = "")
        reivseDecision = input()

        if(reivseDecision == "Y"):
            print("수강가능 인원 입력 > ", end = "")
            maxAvailable = input()

            #유효성 평가
            # 1. 숫자로만 구성되어 있는지 검사
            if (not maxAvailable.isnumeric()):
                print("숫자 외의 다른문자는 입력할 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 2. 앞자리 숫자가 0인지 검사
            if (maxAvailable[0] == '0'):
                print("첫번째 숫자가 0일 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 정수화
            maxAvailable = int(maxAvailable)

            # 3. 수강신청인원 보다 적은지 검사
            if(maxAvailable < int(participantsNum)):
                print("수강신청한 인원보다 작게 설정할 수 없습니다. 다시 입력해주세요.")
                print("\n--------------------------------------------------------------------------------")
                continue

            # 4. 강의실에 맞는 수강인원인지 검사
            subPlace = re.sub(numPattern, "", subPlace)
            
            if (subPlace == "새"):
                if (maxAvailable < 10 or maxAvailable > 20):
                    print("강의실에 따른 수강가능 인원은 10~20명입니다. 다시 입력해주세요.")
                    print("\n--------------------------------------------------------------------------------")
                    continue

            elif (subPlace == "산"):
                if (maxAvailable < 10 or maxAvailable > 30):
                    print("강의실에 따른 수강가능 인원은 10~30명입니다. 다시 입력해주세요.")
                    print("\n--------------------------------------------------------------------------------")
                    continue

            elif (subPlace == "공"):
                if (maxAvailable < 10 or maxAvailable > 40):
                    print("강의실에 따른 수강가능 인원은 10~40명입니다. 다시 입력해주세요.")
                    print("\n--------------------------------------------------------------------------------")
                    continue
            
            return str(maxAvailable)
        
        elif (reivseDecision == "N"):
            return oldMaxAvb
        
        else:
            print("다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")

def reIsRestricted(oldRestricted, participantsNum, subMajor):

    print("")

    while True:

        print("수강신청 제한여부를 수정하시겠습니까? (Y/N) > ", end = "")
        reivseDecision = input()

        if (reivseDecision == "Y"):
            if (int(participantsNum) > 0):
                    print("수강신청한 인원이 없는 경우에만 수강신청 제한여부를 수정할 수 있습니다.")
                    print("\n--------------------------------------------------------------------------------")
                    continue
            
            else:
                if (oldRestricted == "Y"):
                    return "N"
                elif (oldRestricted == "N"):
                    return "Y"

        elif (reivseDecision == "N"):
            return oldRestricted
        
        else:
            print("다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")