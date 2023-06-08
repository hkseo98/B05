import fileinput
import sys

def manageSub(id):

    usersubList = []

    usersFile = open('users.txt', 'r', encoding='UTF8')
    usersFIledata = usersFile.read()
    usersFile.close()

    usersubList = usersFIledata.split("\n\n")

    for i in usersubList:
        line = i.split("\n")
        data = line[0].split("    ")
        if data[0] == id:
            usersubList = i
            break

    usersubList = usersubList.split("\n")
    usersubList.remove(usersubList[0])
    # 수강신청한 과목들 정보

#==========================================================================================================================================================

    if(len(usersubList) == 0):
        print("\n수강신청한 과목이 없습니다. 학생메뉴로 돌아갑니다.")
        print("================================================================================\n")
        return
    
    printSub(usersubList)

    print("--------------------------------<수강신청 철회>---------------------------------")

    while True:
        print("수강신청 철회를 희망하시는 과목이 있으십니까? (Y/N) > ", end = "")
        yn = input()
        
        # 공백 제거
        yn = yn.replace(" ", "")

        if (yn == "Y"):
           result = deleteSub(usersubList, id)

           if (result == 0):
                continue
           
           if (result == 1):
                break

        elif (yn == "N"):
            print("\n학생메뉴로 돌아갑니다.")
            print("================================================================================\n")
            break

        else:
            print("다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")
        
#==========================================================================================================================================================

# 학생 수강신청내역 출력
def printSub(usersubList):

    print("\n--------------------------------<수강신청 목록>---------------------------------")

    for subject in usersubList:
        print(subject)
        print("")

# 수강 철회
def deleteSub(usersubList, id):
    
    while True:
        
        isExistID = False
        
        print("철회를 원하는 과목의 과목번호를 입력하시오 (0 입력 시 취소) > ", end = "")
        inputSubID = input()

        # 공백 제거
        inputSubID = inputSubID.replace(" ", "")

        # 유효성 평가
        for subject in usersubList:
            elementsOfSubject = subject.strip().split('    ')

            if (inputSubID == elementsOfSubject[0]):
                isExistID = True
                #과목파일 정보 불러오기
                subFile = open('subjects.txt', 'r', encoding='UTF8')
                subFileLines = subFile.readlines()
                subFile.close() 

                for line in subFileLines:
                    elementsOfLine = line.strip().split('    ')

                    if(elementsOfLine[0] == inputSubID):
                        print("과목 정보: " + elementsOfLine[0] + "    " + elementsOfLine[1] + "    " + elementsOfLine[2] + "    " + elementsOfLine[3] + "    " + elementsOfLine[4] + "    " + elementsOfLine[5] + "    " + elementsOfLine[6] + "    " + elementsOfLine[7] + "    " + elementsOfLine[8] + "    " + elementsOfLine[9] + "    " + elementsOfLine[10] + "\n")

        # 과목이 존재하는 경우
        if (isExistID):
            while True:
                print("정말로 철회하시겠습니까? (Y/N) > ", end = "")
                yn = input()

                # 공백 제거
                yn = yn.replace(" ", "")

                if (yn == "Y"):

                    # 과목파일에서 인원수 빼기
                    for line in subFileLines:
                        elementsOfLine = line.strip().split('    ')
                        
                        if(elementsOfLine[0] == inputSubID):
                            subID = elementsOfLine[0]
                            subClass = elementsOfLine[1]
                            subCredit = elementsOfLine[2]
                            subName = elementsOfLine[3]
                            TeacherName = elementsOfLine[4]
                            subTime = elementsOfLine[5]
                            subPlace = elementsOfLine[6]
                            cur_student = elementsOfLine[7]
                            max_student = elementsOfLine[8]
                            subNY = elementsOfLine[9]
                            subMajor = elementsOfLine[10]
                    
                            cur_student = int(cur_student)
                            new_cur_student = cur_student - 1
                            new_cur_student = str(new_cur_student)

                            newSubInfo = subID + "    " + subClass + "    " + subCredit + "    " + subName + "    " + TeacherName + "    " + subTime + "    " + subPlace + "    " + new_cur_student + "    " + max_student + "    " + subNY + "    " + subMajor + "\n"

                            with fileinput.FileInput('subjects.txt', inplace = True, encoding="UTF8") as f:
                                for line in f:
                                    if inputSubID in line:
                                        line = line.replace(line, newSubInfo)
                                    sys.stdout.write(line)

                            # 유저파일에서 과목 수정 
                            for line1 in usersubList:
                                data = line1.split("    ")

                                if data[0] == inputSubID:
                                    with fileinput.FileInput('users.txt', inplace = True, encoding="UTF8") as f:
                                        currentId = ""

                                        for line2 in f:
                                            if line2 != "" and line2.split("    ")[0][0] != "A" and line2.split("    ")[0][0] != "B":
                                                currentId = line2.split("    ")[0]
                                        
                                            if inputSubID in line2 and currentId == id:
                                                line2 = line2.replace(line2, "")

                                            sys.stdout.write(line2)
                                            
                                    print("\n철회가 완료되었습니다. 학생메뉴로 돌아갑니다.")
                                    print("================================================================================\n")
                                    return 1
                                
                elif (yn == "N"):
                    print("철회를 취소합니다. 학생메뉴 화면으로 이동합니다. ")
                    print("\n--------------------------------------------------------------------------------")
                    return 1
                
                elif (yn == "0"):
                    print("철회를 취소합니다. 수강신청 철회 화면으로 돌아갑니다.")
                    print("\n--------------------------------------------------------------------------------")
                    return 0

                else:
                    print("다시 입력해주세요.")
                    print("\n--------------------------------------------------------------------------------")

        # 과목철회를 취소할 경우
        elif (inputSubID == "0"):
            print("철회를 취소합니다.")
            print("\n--------------------------------------------------------------------------------")
            return 0
    
        # 과목이 존재하지 않는 경우
        else:
            print("존재하지 않는 과목번호입니다. 다시 입력해주세요.")
            print("\n--------------------------------------------------------------------------------")
        