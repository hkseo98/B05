import fileinput
import sys
from time import sleep


def manageSub(id):

    # 유저파일 읽기    
    usersubList = []

    usersFile = open('users.txt', 'r', encoding='UTF8')
    usersFIledata = usersFile.readl()
    usersFile.close()

    usersubList = usersFIledata.split("\n\n")

    for i in usersubList:
        line = i.split("\n")
        for j in line:
            data = line.split("    ")
            if data[0] == id:
                usersubList = i


    
#==========================================================================================================================================================

    while True:
        printSub(usersubList)
        print("수강신청 철회 원하는 경우 Y 메인 메뉴 복귀를 원하면 N > ", end = "")
        yn = input()
        
        # 공백 제거
        yn = yn.replace(" ", "")

        if (yn == "Y"):
           result = deleteSub(usersubList)

           if (result == 0):
               sleep(2)
               continue
           
           if (result == 1):
               print("잠시 후 메인 화면으로 돌아갑니다.")
               sleep(2)
               break

        elif (yn == "N"):
            print("잠시 후 메인 화면으로 돌아갑니다.")
            sleep(5)
            break

        else:
            print("다시 입력해주세요.")
            sleep(3)
        
#==========================================================================================================================================================

# 학생 수강신청내역 출력
def printSub(usersubList):
    print("수강신청 조회/철회")
    print("현재 수강신청 목록")    

    for subject in usersubList:

        print(subject)

# 수강 철회
def deleteSub(usersubList):
    
    while True:
        
        isExistID = False
        
        print("철회 희망 과목번호 입력(취소 요구 시 0) > ", end = "")
        inputSubID = input()

        # 공백 제거
        inputSubID = inputSubID.replace(" ", "")

        # 유효성 평가
        for subject in usersubList:
            elementsOfSubject = subject.strip().split('    ')

            if (inputSubID == elementsOfSubject[0]):
                isExistID = True

        # 과목이 존재하는 경우
        if (isExistID):
            while True:
                print("정말 철회하시겠습니까? (Y/N) ", end = "")
                yn = input()

                # 공백 제거
                yn = yn.replace(" ", "")

                if (yn == "Y"):

                    # 과목파일에서 인원수 빼기
                    subFile = open('subjects.txt', 'r', encoding='UTF8')
                    subFileLines = subFile.readlines()
                    subFile.close()
                    subList = []
                    wholeSubList = []

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
                    
                    cur_student = int(cur_student)
                    new_cur_student = cur_student - 1
                    new_cur_student = str(new_cur_student)

                    newSubInfo = subID + "    " + subClass + "    " + subCredit + "    " + subName + "    " + TeacherName + "    " + subTime + "    " + subPlace + "    " + new_cur_student + "    " + max_student + "\n"

                    with fileinput.FileInput('subjects.txt', inplace = True) as f:
                        for line in f:
                            if inputSubID in line:
                                line = line.replace(line, newSubInfo)
                            sys.stdout.write(line)


                    # 유저파일에서 과목 제거
                    for ListIndex in usersubList:
                        if (inputSubID in ListIndex):
                            usersubList.remove(ListIndex)

                    
                    # 유저파일 수정 (((((((((((((수정필요!!!!!!!)))))))))))))
                    userFile = open('users.txt', 'w', encoding='UTF8')

                    for line in usersubList:
                        userFile.write(line)

                    userFile.close()
                    return 1

                elif (yn == "N"):
                    print("철회를 취소합니다.")
                    sleep(3)
                    return 1

                else:
                    print("다시 입력하세요.")

        # 과목철회를 취소할 경우
        elif (inputSubID == "0"):
            print("철회를 취소합니다.")
            sleep(5)
            return 0
    
        # 과목이 존재하지 않는 경우
        else:
            print("존재하지 않는 과목번호! 다시 입력하세요.")
        