import fileinput
import sys
from student_sub_manage import manageSub

def Menu():

    print("\n-----------------------------------<학생메뉴>-----------------------------------")
    print("1 -- 개설과목 조회")
    print("2 -- 수강신청")   
    print("3 -- 수강신청 조회/철회")
    print("4 -- 로그아웃")
    print("--------------------------------------------------------------------------------")

def logout():
    print("\n로그아웃합니다. 시작 화면으로 돌아갑니다.")
    print("================================================================================\n")
 
def studentmanager(id):

    while True:

        Menu()
        
        print("메뉴를 입력하시오 > ", end = "")
        student_select= input()

        if (student_select == "1"):
            print("\n-----------------------------------<과목조회>-----------------------------------")

            while True:
                majorNum = 0
                electiveNum = 0

                f1 = open('subjects.txt', 'r', encoding='UTF8')
                lines = f1.readlines()

                for each_line in lines:
                        if each_line.find("전공") > 0:
                              majorNum = majorNum+1

                        elif each_line.find("교양") > 0:
                            electiveNum = electiveNum+1

                print("과목구분 입력 > ", end = "")
                one_select = input()

                if (one_select == "전공"):
                    if (majorNum > 0):
                        print("\n-----------------------------------<전공과목>-----------------------------------")

                        for each_line in lines:
                            if each_line.find("전공") > 0:
                                print (each_line)

                                majorNum = majorNum+1
                            else:
                                pass
                            
                        f1.close()
                        print("--------------------------------------------------------------------------------")
                        print("메뉴로 돌아가려면 아무 키나 입력하시오", end = "")
                        input()
                        print("\n조회가 완료되었습니다. 학생메뉴로 돌아갑니다.")
                        print("================================================================================\n")
                        break

                    else:
                        print("\n개설된 전공과목이 없습니다. 학생메뉴로 돌아갑니다.")
                        print("================================================================================\n")
                        break
            
                elif (one_select == "교양"):
                    if (electiveNum > 0):
                        print("\n-----------------------------------<교양과목>-----------------------------------")
                    
                        for each_line in lines:
                            if each_line.find("교양") > 0:
                                print (each_line)
                            else:
                                pass
                            
                        f1.close()
                        print("--------------------------------------------------------------------------------")
                        print("메뉴로 돌아가려면 아무 키나 입력하시오", end = "")
                        input()
                        print("\n조회가 완료되었습니다. 학생메뉴로 돌아갑니다.")
                        print("================================================================================\n")
                        break

                    else:
                        print("\n개설된 교양과목이 없습니다. 학생메뉴로 돌아갑니다.")
                        print("================================================================================\n")
                        break
                 
                else:
                    print("존재하지 않는 과목구분입니다. 다시 입력해주세요.")
                    print("\n--------------------------------------------------------------------------------")

        elif (student_select == "2"):
            print("\n-----------------------------------<수강신청>-----------------------------------")
            return_num = 5

            while True:
                if (return_num == 10):
                    break
                
                #과목번호 입력 
                print("과목번호 입력(0 입력 시 취소) > ", end = "")
                student_select_sub = input()
                
                #공백제거
                student_select_sub = student_select_sub.replace(" ", "")

                if (student_select_sub == "0"):
                    print("\n수강신청을 취소합니다. 학생메뉴로 돌아갑니다.")
                    print("================================================================================\n")
                    break

                # 존재하는 과목번호인지 확인
                subFile = open('subjects.txt', 'r', encoding='UTF8')
                subFileLines = subFile.readlines()
                subFile.close()

                isSubNumberEx, selectedSub = isSubNumberExists(student_select_sub, subFileLines)

                # 존재하는 과목 번호인지 확인
                if isSubNumberEx is False:
                    continue
                
                # 존재하는 과목인 경우 과목 정보 출력
                print("과목 정보: " + selectedSub[0] + "    " + selectedSub[1] + "    " + selectedSub[2] + "    " + selectedSub[3] + "    " + selectedSub[4] + "    " + selectedSub[5] + "    " + selectedSub[6] + "    " + selectedSub[7] + "    " + selectedSub[8] + "\n")

                # 동일 시간 확인 및 최대 학점 확인
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

                usersub_amount = 0

                for line in usersubList:
                    usersub_amount = usersub_amount + int(line.split("    ")[2])
                
                # 인원 확인하기 
                for line in subFileLines:
                    elementsOfLine = line.strip().split('    ')

                    if (len(elementsOfLine) == 9):
                        if (elementsOfLine[0] == student_select_sub):
                            max_student = elementsOfLine[8]
                            cur_student = elementsOfLine[7]

                # 정수화
                max_student = int(max_student)
                cur_student = int(cur_student)

                if ((max_student - cur_student) == 0):
                    print("수강인원이 꽉 차 있습니다. 다시 입력해주세요.")
                    print("\n--------------------------------------------------------------------------------")
                    continue

                # 입력한 과목 추출
                for line in subFileLines:
                    elementsOfLine = line.strip().split('    ')

                    if(elementsOfLine[0] == student_select_sub):
                        subID = elementsOfLine[0]
                        subClass = elementsOfLine[1]
                        subCredit = elementsOfLine[2]
                        subName = elementsOfLine[3]
                        TeacherName = elementsOfLine[4]
                        subTime = elementsOfLine[5]
                        subPlace = elementsOfLine[6]

                newSub = subID + "    " + subClass + "    " + subCredit + "    " + subName + "    " + TeacherName + "    " + subTime + "    " + subPlace + "\n"
                
                while True:
                    print("신청하시겠습니까? (Y/N) > ", end = "")
                    yn = input()

                    # 공백 제거
                    yn = yn.replace(" ", "")

                    if (yn == "Y"):
                        # 유저정보에 과목추가
                        usersFile = open('users.txt', 'r', encoding='UTF8')
                        usersFileLines = usersFile.readlines()
                        usersFile.close()

                        # 과목명이 같은 과목을 수강중인지
                        isNameSame = False

                        for line in usersFileLines:
                            elementsOfLine = line.strip().split('    ')

                            if(len(elementsOfLine) == 4):
                                userID = elementsOfLine[0]

                            if(userID == id and len(elementsOfLine) == 7):
                                if(subName == elementsOfLine[3]):
                                    isNameSame = True

                        if(isNameSame):
                            print("동일한 과목명을 가진 과목을 수강 중입니다. 다시 입력해주세요.")
                            print("\n--------------------------------------------------------------------------------")
                            break

                        # 수업을 들을만큼 학점이 있는지 
                        test_subCredit = subCredit
                        test_subCredit = int(test_subCredit)

                        if (usersub_amount + test_subCredit > 12):
                            print("신청 가능한 학점을 초과했습니다. 다시 입력해주세요.")
                            print("\n--------------------------------------------------------------------------------")
                            break
                        
                        isDuplicate = False
                        # 강의실 및 시간 중복

                        for line in usersubList:
                            elements = line.split("    ")

                            # 요일 겹치는 경우
                            existTime = elements[5]
                            timeToAdd = subTime

                            if existTime[0] == subTime[0]:
                                if int(existTime[1]) <= int(timeToAdd[1]) and int(existTime[2]) >= int(timeToAdd[1]):
                                    print("이미 수강신청한 수업과 수업시간이 겹칩니다. 다시 입력해주세요.")
                                    print("\n--------------------------------------------------------------------------------")
                                    isDuplicate = True
                                    break

                                elif int(existTime[1]) <= int(timeToAdd[2]) and int(existTime[2]) >= int(timeToAdd[2]):
                                    print("이미 수강신청한 수업과 수업시간이 겹칩니다. 다시 입력해주세요.")
                                    print("\n--------------------------------------------------------------------------------")
                                    isDuplicate = True
                                    break

                                elif int(existTime[1]) >= int(timeToAdd[1]) and int(existTime[2]) <= int(timeToAdd[2]):
                                    print("이미 수강신청한 수업과 수업시간이 겹칩니다. 다시 입력해주세요.")
                                    print("\n--------------------------------------------------------------------------------")
                                    isDuplicate = True
                                    break

                        if isDuplicate == True:
                            break

                        index = 0

                        for line in usersFileLines:
                            elementsOfLine = line.strip().split('    ')

                            index += 1
        
                            if(elementsOfLine[0] == id):
                                usersFileLines.insert(index, newSub)

                        usersFile = open('users.txt', 'w', encoding='UTF8')
    
                        for line in usersFileLines:
                            usersFile.write(line)
                        
                        usersFile.close()

                        # 과목파일 수강생 수 정정
                        new_cur_student = cur_student + 1

                        # 정수를 문자화
                        new_cur_student = str(new_cur_student)
                        max_student = str(max_student)

                        newSubInfo = subID + "    " + subClass + "    " + subCredit + "    " + subName + "    " + TeacherName + "    " + subTime + "    " + subPlace + "    " + new_cur_student + "    " + max_student + "\n"

                        with fileinput.FileInput('subjects.txt', inplace = True, encoding="UTF8") as f:
                            for line in f:
                                if student_select_sub in line:
                                    line = line.replace(line, newSubInfo)

                                sys.stdout.write(line)

                        print("\n수강신청이 완료되었습니다. 학생메뉴로 돌아갑니다.")
                        print("================================================================================\n")
                        return_num = 10
                        break

                    elif (yn == "N"):
                        print("\n수강신청을 취소합니다. 학생메뉴로 돌아갑니다.")
                        print("================================================================================\n")
                        return_num = 10
                        break

                    else:
                        print("다시 입력해주세요.")
                        print("\n--------------------------------------------------------------------------------")

        elif (student_select == "3"):
            manageSub(id)           

        elif (student_select == "4"):
            logout()
            return
        
        else:
            print("메뉴번호를 확인 후 다시 입력해 주세요.")


def isSubNumberExists(student_select_sub, subFileLines):
    
    for line in subFileLines:
        elementsOfLine = line.strip().split('    ')
        if student_select_sub == elementsOfLine[0]:
            return True, elementsOfLine
    
    
    print("존재하지 않는 과목번호입니다. 다시 입력해주세요.")
    print("\n--------------------------------------------------------------------------------")
    return False, []
