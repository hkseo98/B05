import re

def register():
    while True:
        print("\n<회원가입>")
        print("1. 학생 사용자")
        print("2. 교수 사용자")
        userType = input("선택하세요> ")
        # 학생 회원가입
        if userType == "1":
            # ID, PW 입력
            id, pw = getIdandPW()
            # 학과 입력
            major = getMajor()
            # 이름 입력 
            name = getName()
            # 회원가입 완료
            makeNewUser(id, pw, major, name, True)
            return
        # 교수 회원가입  
        elif userType == "2":
            # ID, PW 입력
            id, pw = getIdandPW()
            # 학과 입력
            major = getMajor()
            # 이름 입력 
            name = getName()
            # 회원가입 완료
            makeNewUser(id, pw, major, name, False)
            return
        else:
            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
            continue                   
                        
                        
                        
def getIdandPW():
    pattern = re.compile("[ㄱ-ㅎ가-힣]+")

    while True:
                isExistingId = False
                print("\nID 입력(알파벳+숫자길이6~12)\n(공백/개행 입력 불가)")
                id = input("> ")
                # id 유효성 평가
                # 길이 검사
                if len(id) < 6 or len(id) > 12 :
                    print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                    continue
                # 숫자 알파벳 이외의 문자가 있는지 검사
                elif id.isalnum() == False:
                    print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                    continue
                # 한글이 포함되어 있는지 검사
                elif pattern.search(id):
                    print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                    continue
                # 숫자로만, 혹은 알파벳으로만 구성되어 있는지 검사
                elif id.isalpha():
                    print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                    continue
                elif id.isnumeric():
                    print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                    continue
                else:
                    # id 중복 검사
                    
                    userFile = open("users.txt", 'r', encoding="UTF-8")
                    userFileLines = userFile.readlines()
                    userFile.close()
                    for line in userFileLines:
                        # 사용자 정보 첫 줄인 경우
                        if len(line.strip().split("    ")) == 4:
                            # ID 중복된 경우 오류 메시지 
                            if line.strip().split("    ")[0].upper() == id.upper():
                                print("중복된 ID입니다! 다시 입력해주세요.")
                                isExistingId = True
                                continue
                # 중복되지 않았을 경우 
                if isExistingId == False:
                    # id 입력 완료
                    # 비밀번호 입력 시작
                    while True:
                        print("\nPW 입력\n(알파벳 + 숫자 + 제한된 특수문자 길이 8~15)\n(제한된 특수문자: !,@,#,$,%,^,&,* 사용 가능)\n(공백/개행 입력 불가)")
                        pw = input("> ")
                        originPw = pw
                        # pw 유효성 평가
                        # 길이 검사
                        if len(pw) < 8 or len(pw) > 15:
                            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                            continue
                        # 한글이 포함되어 있는지 검사
                        if pattern.search(pw):
                            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                            continue
                        # 제한된 특수문자 있는지 확인 후 특수문자 삭제 -> 그리고 isalnum()으로 숫자, 알파벳으로만 구성되어 있는지 확인
                        specials = ['!','@','#','$','%','^','&','*']
                        isContainSpecials = False
                        for char in pw:
                            if char in specials:
                                isContainSpecials = True
                                pw = pw.replace(char, '')
                        # 제한된 특수문자 포함하지 않는 경우 오류문구 출력
                        if isContainSpecials == False:
                            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                            continue
                        # 제한된 특수문자를 삭제한 이후에도 숫자, 알파벳으로만 이루어지지 않은 경우 오류문구 출력
                        elif pw.isalnum() == False:
                            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                            continue
                        # 숫자로만, 혹은 알파벳으로만 구성되어 있는지 검사
                        elif pw.isalpha():
                            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                            continue
                        elif pw.isnumeric():
                            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
                            continue
                        
                        # 비밀번호 재확인
                        pwDoubleCheck = input("PW 확인 > ")
                        
                        if originPw == pwDoubleCheck: 
                            return id, originPw
                        else:
                            print("재입력하신 PW가 처음 입력하신 PW와 일치하지 않습니다. 다시 입력해주세요.")
                            continue
                            
def getName():
    while True:
        print("\n이름 입력(한글 문자 2~5)")
        name = input(">")
        if len(name) < 2 or len(name) > 5:
            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
            continue
        if isKorean(name) == False:
            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
            continue
        return name

majors = ['컴퓨터공학부', '국어국문학과', '철학과', '기술경영학과', '물리학과']
majors2 = ['컴', '국', '철', '기', '물']

def getMajor():
    while True:
        print("\n학과 입력(컴퓨터공학부, 국어국문학과, 철학과, 기술경영학과, 물리학과 중 하나의 학과 입력)")
        major = input("> ")
        # 학과 입력 유효성 검사
        if(major in majors) or (major in majors2):
            # 학과 입력이 유효한 경우 => 이름 입력
            return major
        else:
            print("올바르지 않는 형식입니다! 다시 입력해주세요.")
            continue
        
        
def makeNewUser(id:str, pw:str, major:str, name:str, isStudent:bool):
    # 학생이면 학번이 5자리 수, 교수면 교수번호가 4자리 수
    if isStudent:
        numLen2 = 10000
        userFile = open("student_number.txt", 'r', encoding="UTF-8")
        userFileLines = userFile.readlines()
        userFile.close()
    else:
        numLen2 = 1000
        userFile = open("professor_number.txt", 'r', encoding="UTF-8")
        userFileLines = userFile.readlines()
        userFile.close()
    # 학과 번호 설정
    majorNum = 1
    if len(major) == 1:
        majorNum = majors2.index(major) + 1
    else:
        majorNum = major.index(major) + 1
        
    
    # 학번 설정
    studentOrProfessorNum = 0
    for line in userFileLines:
        # 학과번호가 같은 학생 사용자가 있을 때마다 studentOrProfessorNum 1씩 늘림
        if line.strip()[0] == str(majorNum):
            studentOrProfessorNum = studentOrProfessorNum + 1
    studentOrProfessorNum = majorNum * numLen2 + studentOrProfessorNum + 1    
    # 유저 파일에 기록
    userFile = open("users.txt", 'a', encoding="UTF-8")
    userFile.write(id + "    " + pw + "    " + str(studentOrProfessorNum) + "    " + name + "\n\n")
    userFile.close()
    # 학번/교수번호 파일에 기록
    if isStudent:
        userFile = open("student_number.txt", 'a', encoding="UTF-8")
        userFile.write(str(studentOrProfessorNum)+"\n")
        userFile.close()
    else:
        userFile = open("professor_number.txt", 'a', encoding="UTF-8")
        userFile.write(str(studentOrProfessorNum)+"\n")
        userFile.close()
    print("회원가입이 완료되었습니다.")
    return
    

def isKorean(text):
    # 한글 정규 표현식
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('', text)
    return len(result) == len(text)