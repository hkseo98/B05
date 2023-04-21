import os
import string
import login_function as m
import creat_subject
import re
from time import sleep
import fileinput
import sys
from student_sub_manage import manageSub



def Menu():

    print("--------------------------------------------------")
    print("1 -- 개설 과목 조회")
    print("2 -- 수강신청")   
    print("3 -- 수강신청 조회/철회")
    print("4 -- 로그아웃")
    print("--------------------------------------------------")

def logout():
    print("로그아웃 합니다.\n곧 로그인 화면으로 돌아갑니다.")
 

def studentmanager(id):
    while True:

        os.system('cls')
        Menu()
        print("선택하세요: ", end = "")
        student_select= input()

        if (student_select == "1"):

            print("전공/교양과목 (조회를 원하는 과목부분을 입력: 전공 or 교양)")
            while True:
                 print("조회 선택> ", end = "")
                 one_select = input()
                 if (one_select == "전공"):
                    f1 = open('subjects.txt', 'r', encoding='UTF8')
                    lines = f1.readlines()
                    for each_line in lines:
                         if each_line.find("전공") > 0:
                              print (each_line)
                         else:
                              pass
                    f1.close()
                    print("돌아가려면 아무 키 입력", end = "")
                    input()
                    break
            
                 elif (one_select == "교양"):
                    f2 = open('subjects.txt', 'r', encoding='UTF8')
                    lines = f2.readlines()
                    for each_line in lines:
                         if each_line.find("교양") > 0:
                              print (each_line)
                         else:
                              pass
                    f2.close()
                    print("돌아가려면 아무 키 입력", end = "")
                    input()
                    break
                 
                 else:
                     print("존재하지 않는 과목구분입니다. 다시 입력하세요.")

        elif (student_select == "2"):
            os.system('cls')
            print("수강신청 (메인메뉴 복귀 원하면 '0' 입력)")
            while True:
                if (return_num == 10):
                    break
                
                return_num = 5

                #과목번호 입력 
                print("과목번호 입력> ", end = "")
                student_select_sub = input()
                
                #공백제거
                student_select_sub = student_select_sub.replace(" ", "")

                if (student_select_sub == 0):
                    print("신청을 취소하였습니다.")
                    sleep(5)
                    break

                #유저 파일 확인
                usersFile = open('users.txt', 'r', encoding='UTF8')
                usersFIleLines = usersFile.readlines()
                usersFile.close()
                
                for line in usersFIleLines:
                    elementsOfLine = line.strip().split('    ')
                    
                    if (len(elementsOfLine) == 5):
                        if (elementsOfLine[0] == id):
                            userid = elementsOfLine[0]
                            userpw = elementsOfLine[1]
                            userNum = elementsOfLine[2]
                            userName = elementsOfLine[3]
                            usersub_amount = elementsOfLine[4]

                #현재 학점 정수화
                usersub_amount = int(usersub_amount)

                #과목 파일 확인 
                subFile = open('subjects.txt', 'r', encoding='UTF8')
                subFileLines = subFile.readlines()
                subFile.close()

                #맞는 과목 번호인지 확인
                checksub_num = []

                for line in subFileLines:
                    elementsOfLine = line.strip().split('    ')

                    checksub_num.append(line)

                if student_select_sub not in checksub_num:
                    print("존재하지 않는 과목번호! 다시 입력하세요.")
                    continue

                #인원 확인하기 
                for line in subFileLines:
                    elementsOfLine = line.strip().split('    ')

                    if (len(elementsOfLine) == 9):
                        if (elementsOfLine[0] == student_select_sub):
                            max_student = elementsOfLine[8]
                            cur_student = elementsOfLine[7]

                #정수화
                max_student = int(max_student)
                cur_student = int(cur_student)

                if ((max_student - cur_student) == 0):
                    print("수강인원이 꽉 차 있습니다. 다시 입력 해주세요. ")
                    continue

                #입력한 과목 추출
                input_sub = []

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


                #동일 시간 확인 

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
                             


                #여기 구현 아직 안됨 
                
                
                
                
                #유저파일에 과목 추가 
                subList = []

                for line in subFileLines:
                    elementsOfLine = line.strip().split('    ')

                    if(elementsOfLine[0] == student_select_sub):
                        subInfo = elementsOfLine

                #과목정보 출력
                print(subInfo)

                while True:

                    print("신청하시겠습니까?(Y/N) > ", end = "")
                    yn = input()

                    # 공백 제거
                    yn = yn.replace(" ", "")

                    if (yn == "Y"):
                        #유저정보에 과목추가
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
                            usersFile.close()

                        #유저 총학점 수정
                        subCredit = int(subCredit)
                        final_credit = usersub_amount + subCredit

                        #총 학점 문자화
                        final_credit = str(final_credit)

                        newUserInfo = userid + "    " + userpw + "    " + userNum + "    " + userName +  "    " + final_credit + "\n"

                        with fileinput.FileInput('users.txt', inplace = True) as f:
                            for line in f:
                                if id in line:
                                    line = line.replace(line, newUserInfo)
                                sys.stdout.write(line)

                        #과목파일 수강생 수 정정
                        new_cur_student = cur_student + 1
                        #정수를 문자화
                        new_cur_student = str(new_cur_student)

                        newSubInfo = subID + "    " + subClass + "    " + subCredit + "    " + subName + "    " + TeacherName + "    " + subTime + "    " + subPlace + "    " + new_cur_student + "    " + max_student + "\n"

                        with fileinput.FileInput('subjects.txt', inplace = True) as f:
                            for line in f:
                                if student_select_sub in line:
                                    line = line.replace(line, newSubInfo)
                                sys.stdout.write(line)


                        print("정상적으로 신청되었습니다.")
                        return_num = 10
                        break

                    elif (yn == "N"):
                        print("신청을 취소하였습니다.")
                        return_num = 10
                        break

                    else:
                        print("잘못된 입력! 다시 입력하세요.")



        elif (student_select == "3"):
            os.system('cls')
            manageSub(id)           


        elif (student_select == "4"):
            os.system('cls')
            logout()
            sleep(5)
            return
        
        else:
            print("존재하지 않는 선택지입니다. 다시 입력하세요.")
            sleep(3)


