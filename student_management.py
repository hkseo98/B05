import os
import string
import msvcrt as ms
import login_function as m
import creat_subject
import re
from time import sleep

def wait():
     ms.getch()

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
                 print("조회 선택: ", end = "")
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
                    wait()
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
                    wait()
                    break
                 
                 else:
                     print("존재하지 않는 과목구분입니다. 다시 입력하세요.")

        elif (student_select == "2"):
            os.system('cls')
            print("수강신청 (메인메뉴 복귀 원하면 '0' 입력)")
            while True:

                #유저 파일 생성 and 확인
                usersFile = open('users.txt', 'r', encoding='UTF8')
                usersFIleLines = usersFile.readlines()
                usersFile.close()
                
                for line in usersFIleLines:
                    elementsOfLine = line.strip().split('    ')
                    
                    if (len(elementsOfLine) == 4):
                        if (elementsOfLine[0] == id):
                            userNum = elementsOfLine[2]
                            userName = elementsOfLine[3]



                #처음 과목 신청인지 검사 
                path = 'sugang'
                for filename in os.listdir(path):
                    if filename == userNum + ".txt":
                        # 과목파일 읽기
                        subFile = open('subjects.txt', 'r', encoding='UTF8')
                        subFileLines = subFile.readlines()
                        subFile.close()

                        # 유저과목 읽기
                        userfile = open('sugang'+ userNum + '.txt', 'r', encoding='UTF8')
                        userfilelines = userfile.readlines()
                        userfile.close()

                        # 과목리스트 생성
                        subList = []
                        wholeSubList = []
                
                        for line in subFileLines:
                            elementsOfLine = line.strip().split('    ')
                    
                            # 전체 과목리스트
                            wholeSubList.append(line)
                            
                            
                        for line in userfilelines:
                            eleofLine = line.strip().split('    ')
                            
                            
                            
                        checkfile = open('subjects.txt', 'r', encoding='UTF8')
                        lines = checkfile.readlines()
                        for each_line in lines:
                            if each_line.find(two_select) > 0:
                                subject = each_line

                        filepath = os.path.join('sugang', userNum + '.txt')
                        f3 = open(filepath, "w")
                        f3.write(subject)
                        f3.close()

                        break

                    else:
                        checkfile = open('subjects.txt', 'r', encoding='UTF8')
                        lines = checkfile.readlines()
                        for each_line in lines:
                            while True:
                                two_select = input()
                                if (two_select == "0"):
                                    break
                                 
                                elif each_line.find(two_select) > 0:
                                    subject = each_line
                                    filepath = os.path.join("sugang/"+userNum+".txt")
                                    f3 = open(filepath, "w")
                                    f3.write(subject)
                                    f3.close()
                                    break
                                else:
                                    print("존재하지 않는 과목번호! 다시 입력하세요")
                                    print("과목번호 입력", end = "")

                    break
                

                

                """f2 = open('subjects.txt', 'r', encoding='UTF8')
                lines = f2.readlines()
                for each_line in lines:
                    if each_line.find(two_select) > 0:
                        print(each_line)
                        while True: 
                            print("신청하시겠습니까?(Y/N)", end = "")
                            choose_input = input()
                            if (choose_input == 'Y'):
                                print("f")"""

                            #유저 개인 파일 필요 
                                
                

        elif (student_select == "3"):
            os.system('cls')            



        elif (student_select == "4"):
            os.system('cls')
            logout()
            sleep(5)
            return
        
        else:
            print("존재하지 않는 선택지입니다. 다시 입력하세요.")
            sleep(3)


