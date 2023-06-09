import re

def creatSubject(id):
    
    # 유저파일 읽기
    usersFile = open('users.txt', 'r', encoding='UTF8')
    usersFIleLines = usersFile.readlines()
    usersFile.close()

    # 교수이름과 교번 불러오기
    for line in usersFIleLines:
        elementsOfLine = line.strip().split('    ')

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
        if(elementsOfLine[4] == userName + "(" + userNum + ")"):
            subList.append(line)

    # 과목구분별 번호 읽기
    aNum = 0    
    bNum = 0    

    for line in subFileLines:
        elementsOfLine = line.strip().split('    ')

        # 전공 과목번호
        if ('A' in elementsOfLine[0]):
            if (aNum < int(str(elementsOfLine[0]).replace("A", ""))):
                aNum = int(str(elementsOfLine[0]).replace("A", ""))

        # 교양 과목번호
        elif ('B' in elementsOfLine[0]):
            if (bNum < int(str(elementsOfLine[0]).replace("B", ""))):
                bNum = int(str(elementsOfLine[0]).replace("B", ""))

#==========================================================================================================================================================

# 과목 생성 
    # 1. 과목구분 입력
    subID, subClass = getSubClass(aNum, bNum)

    # 2. 과목명 입력
    subName = getSubName(wholeSubList)

    # 3. 강의시간 입력
        # 3.1 강의요일 입력
    subDay = getSubDay()

        # 3.2 강의교시 입력
    subTime, subCredit = getSubTime(subDay, subList)

    # 4. 강의장소 입력
    subPlace = getSubPlace(subTime, wholeSubList)

    # 5. 최대 수강인원 입력
    maxAvailable = getMaxAvailable(subPlace)

#==========================================================================================================================================================

# 파일 수정
    newSub = subID + "    " + subClass + "    " + subCredit + "    " + subName + "    " + userName+"("+userNum+")" + "    " + subTime + "    " + subPlace + "    " + "0" + "    " + maxAvailable + "\n" 

    #과목파일 수정
    subFile = open('subjects.txt', 'a', encoding='UTF8')
    subFile.write(newSub)
    subFile.close

    #유저파일 수정
    usersFile = open('users.txt', 'r', encoding='UTF8')
    usersFIleLines = usersFile.readlines()
    usersFile.close()

    index = 0

    for line in usersFIleLines:
        elementsOfLine = line.strip().split('    ')

        index += 1
        
        if(elementsOfLine[0] == id):
            usersFIleLines.insert(index, newSub)

    usersFile = open('users.txt', 'w', encoding='UTF8')
    
    for line in usersFIleLines:
        usersFile.write(line)

#==========================================================================================================================================================

#과목구분
def getSubClass(aNum, bNum):

    while True:

        print("과목구분 입력 > ", end = "")
        subClass = input()

        # 공백 제거
        subClass = subClass.replace(" ", "")

        # 과목구분 유효성 평가
        if(subClass == "전공" or subClass == "교양"):

            if(subClass == "전공"):
                if(aNum != 0):
                    aNum = aNum+1
                    subID = "A" + str(aNum)

                elif (aNum == 0):
                    subID = "A000"

                return subID, subClass
            
            elif(subClass == "교양"):
                
                if(bNum != 0):
                    bNum = bNum+1
                    subID = "B" + str(bNum)

                elif(bNum == 0):
                    subID = "B000"
                    
                return subID, subClass
        
        else:
            print("존재하지 않는 과목구분입니다. 다시 입력해주세요.")

#과목명
def getSubName(wholeSubList):

    while True: 
        
        isExist = False

        print("과목명 입력 > ", end = "")
        subName = input()

        # 공백 제거
        subName = subName.replace(" ", "")

        # 유효성 평가
        # 1. 문자열 길이 검사
        if (len(subName) < 3 or len(subName) > 10):
            print("과목명은 3~10글자로 구성되어야 합니다. 다시 입력해주세요.")
            continue

        # 2. 한글, 숫자, 알파벳 이외의 문자가 있는지 검사
        elif (not subName.isalnum()):
            print("한글, 숫자, 알파벳이외의 글자는 입력 불가능합니다. 다시 입력해주세요.")
            continue

        # 3. 숫자로만 구성되어 있는지 검사
        elif (subName.isnumeric()):
            print("과목명은 숫자만으로 구성될 수 없습니다. 다시 입력해주세요.")
            continue

        # 4. 중복 검사
        else:
            for subject in wholeSubList:
                elementOfSub = subject.strip().split('    ')

                if (elementOfSub[3] == subName):
                    print("이미 존재하는 과목명입니다. 다시 입력해주세요.")
                    isExist = True

        if (not isExist):
            return subName

# 강의요일
def getSubDay():

    while True:

        possibleDay = ["월", "화", "수", "목", "금", "토", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]

        print("강의요일 입력 > ", end = "")
        subDay = input()

        # 공백 제거
        subDay = subDay.replace(" ", "")

        # 유효성 평가
        for day in possibleDay:
            if(subDay == day):

                if(len(subDay) == 3):
                    subDay = subDay.replace("요일", "")
                    
                return subDay
        
        print("다시 입력해주세요.")

# 강의시간
def getSubTime(subDay, subList):

    korPattern = re.compile("[ㄱ-ㅎ가-힣]+")
    numPattern = re.compile("[0-9]+")

    while True:

        isPass = True

        print("강의 시작교시 입력> ", end = "")
        subStart = input()

        print("강의 종료교시 입력> ", end = "")
        subFinish = input()

        # 공백 제거
        subStart = subStart.replace(" ", "")
        subFinish = subFinish.replace(" ", "")

        # 1. 시작교시 유효성 평가
        # 1.1 숫자로만 구성되어 있는지 검사
        if (not subStart.isnumeric()):
            print("숫자 외의 다른문자는 입력할 수 없습니다. 다시 입력해주세요.")
            continue
        
        # 정수화
        subStart = int(subStart)

        # 1.2 강의가능 교시인지 검사
        if (subStart < 1 or subStart > 8):
            print("강의는 1교시부터 8교시까지만 가능합니다. 다시 입력해주세요.")
            continue

        # 2. 종료교시 유효성 평가
        # 2.1 숫자로만 구성되어 있는지 검사
        if (not subFinish.isnumeric()):
            print("숫자 외의 다른문자는 입력할 수 없습니다. 다시 입력해주세요.")
            continue

        # 정수화
        subFinish = int(subFinish)

        # 2.2 강의가능 교시인지 검사
        if (subFinish < 1 or subFinish >8):
            print("강의는 1교시부터 8교시까지만 가능합니다. 다시 입력해주세요.")
            continue

        # 2.3 시작교시 이후인지 검사
        if (subFinish < subStart):
            print("강의종료는 강의시작 후에 이루어져야 합니다. 다시 입력해주세요.")
            continue

        # 2.4 총 강의시간 검사
        if (subFinish - subStart > 3):
            print("강의시간은 3교시를 초과할 수 없습니다. 다시 입력해주세요.")
            continue

        # 3. 강의시간 중복 검사
        for existSub in subList:
            elementsOfSub = existSub.split('    ')

            existTime = elementsOfSub[5]

            existDay = re.sub(numPattern, "", existTime)
            existStartTime = int(int(re.sub(korPattern, "", existTime))/10)
            existFinishTime = int(int(re.sub(korPattern, "", existTime))%10)

            if (subDay == existDay):
                if (existStartTime <= subStart and subStart <= existFinishTime):
                    print("이미 개설하신 과목과 강의시간이 겹칩니다. 다시 입력해주세요.")
                    isPass = False
                    break
                    
                elif (existStartTime <= subFinish and subFinish <= existFinishTime):
                    print("이미 개설하신 과목과 강의시간이 겹칩니다. 다시 입력해주세요.")
                    isPass = False
                    break

        if (isPass):    
            subCredit = subFinish - subStart + 1
            subTime = subDay + str(subStart) + str(subFinish)

            return subTime, str(subCredit)

# 강의장소
def getSubPlace(subTime, wholeSubList):

    korPattern = re.compile("[ㄱ-ㅎ가-힣]+")
    numPattern = re.compile("[0-9]+")

    possiblePlace = re.compile("[새산공][1-9][0-9][1-9]")

    while True:

        isPass = True

        print("강의장소 입력 > ", end = "")
        subPlace = input()

        # 공백 제거
        subPlace = subPlace.replace(" ", "")

        # 유효성 평가
        # 1. 문자열 길이 검사
        if(len(subPlace) != 4):
            print("올바르지 못한 강의장소입니다. 다시 입력해주세요.")
            continue
        
        # 2. 문법 검사
        if(possiblePlace.match(subPlace) == None):
            print("올바르지 못한 강의장소입니다. 다시 입력해주세요.")
            continue

        # 3. 강의실 중복 검사
        for existSub in wholeSubList:
            elementsOfSub = existSub.split('    ')

            existPlace = elementsOfSub[6]
            existTime = elementsOfSub[5]

            existDay = re.sub(numPattern, "", existTime)
            existStartTime = int(int(re.sub(korPattern, "", existTime))/10)
            existFinishTime = int(int(re.sub(korPattern, "", existTime))%10)

            subDay = re.sub(numPattern, "", subTime)
            subStart = int(int(re.sub(korPattern, "", subTime))/10)
            subFinish = int(int(re.sub(korPattern, "", subTime))%10)

            if(existPlace == subPlace):
                if(existDay == subDay):
                    if (existStartTime <= subStart and subStart <= existFinishTime):
                        print("이미 개설된 과목과 강의시간 및 강의실이 겹칩니다. 다시 입력해주세요.")
                        isPass = False
                        break

                    elif (existStartTime <= subFinish and subFinish <= existFinishTime):
                        print("이미 개설된 과목과 강의시간 및 강의실이 겹칩니다. 다시 입력해주세요.")
                        isPass = False
                        break
                
        if(isPass):        
            return subPlace

# 최대 수강인원
def getMaxAvailable(subPlace):

    numPattern = re.compile("[0-9]+")

    # 새: 10~20, 산: 10~30, 공: 10~40
    while True:
        print("수강가능인원 입력 > ", end = "")
        maxAvailable = input()

        #공백 제거
        maxAvailable.replace(" ", "")

        #유효성 평가
        # 1. 숫자로만 구성되어 있는지 검사
        if (not maxAvailable.isnumeric()):
            print("숫자 외의 다른문자는 입력할 수 없습니다. 다시 입력해주세요.")
            continue

        # 정수화
        maxAvailable = int(maxAvailable)

        # 2. 강의실에 맞는 수강인원인지 검사
        subPlace = re.sub(numPattern, "", subPlace)
        
        if (subPlace == "새"):
            if (maxAvailable < 10 or maxAvailable > 20):
                print("강의실에 따른 수강가능 인원은 10~20명입니다. 다시 입력해주세요.")
                continue

        elif (subPlace == "산"):
            if (maxAvailable < 10 or maxAvailable > 30):
                print("강의실에 따른 수강가능 인원은 10~30명입니다. 다시 입력해주세요.")
                continue

        elif (subPlace == "공"):
            if (maxAvailable < 10 or maxAvailable > 40):
                print("강의실에 따른 수강가능 인원은 10~40명입니다. 다시 입력해주세요.")
                continue
        
        return str(maxAvailable)
    
            








        
    
