#koreapas uploader

#designed by YJ

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.chrome.options import Options

class koreapas_bot:
    def __init__(self):
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        # chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'`    

        self.driver = webdriver.Chrome(chrome_options=chrome_options)  


        # self.driver =  webdriver.Chrome();
        # self.driver.start()          
        self.driver.get("https://www.koreapas.com/bbs/main.php")

    def close(self):
        self.driver.close()

    def login(self,id,password):
        self.driver.get("https://www.koreapas.com/bbs/main.php")
        while True:
            try:
                self.driver.find_element_by_name('user_id').send_keys(id)
                break
            except:
                pass

        self.driver.find_element_by_name('password').send_keys(password,Keys.RETURN)

    def check(self):
        self.driver.get("https://www.koreapas.com/bbs/zboard.php?id=circle")
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        # print(soup)
        source = soup.select('span.list_title') 
        name_ex = re.compile('HandS')
        now = name_ex.findall(str(source))
        if not now:
            return 0
        else :
            return 1
    def delete(self):
        self.driver.get("https://www.koreapas.com/bbs/myboard.php?id=circle")
        while True:
            try:
                self.driver.find_element_by_class_name('list_title').click()
                break
            except:
                pass
        while True:
            try:
                j = self.driver.find_element_by_class_name('class7')
                break
            except:
                pass
        print(j)

    def new_advertisement(self):
        self.driver.get("https://www.koreapas.com/bbs/zboard.php?id=circle")

        while True:
            try:
                self.driver.find_element_by_class_name('reebtn').click()
                break
            except:
                pass
        while True:
            try:
                self.driver.find_element_by_name('subject').send_keys('[고려대학교 전기전자공학부 전공학회] HandS에 함께할 신입 회원을 모집합니다!') #subject
                break
            except:
                pass

        self.driver.find_element_by_id('filesinput').send_keys("/home/coldreason/Desktop/pic.png"); #pic
        self.driver.find_element_by_name('sitelink1').send_keys('https://youtu.be/m7hk4CzrL94')
        self.driver.find_element_by_name('tag').send_keys('#전공학회 #전기전자공학부 #HandS #Hardware #Software #자율주행 #드론 #CCP #3D프린터 ')
        self.driver.find_element_by_name('memo').send_keys('고려대학교 전기전자공학부 전공학회 HandS에서 신입회원을 모집합니다! \n\n\
        18학번 신입생을 포함하여 전공/나이/학년 상관없이 지원 가능합니다. (*단 3학기 이상 활동이 가능한 자)\n\n\
        \
        안녕하세요 HandS입니다.\n\n\
        \
        저희는 전기전자공학부 전공학술 학회로서 \n\
        Hardware와 Software에 관심이 있는 사람들이 모인 동아리입니다.\n\n\n\
        \
        \
        평소에 만들고 싶었던 것을 직접 현실로 만들 수 있는 동아리!\n\n\
        \
        바로 HandS입니다.\n\n\n\
        \
        \
        아직 잘 모르는 사람… 배울 곳이 없어 고민하던 사람…\n\n\
        \
        같이 프로젝트 할 사람이 없는 사람…\n\n\
        \
        열정과 끈기만 있다면 얼마든지 함께할 수 있습니다!\n\n\
        \
        #3D프린터 #자율주행차 #드론 #알고리즘 #프로그래밍\n\
        다양한 프로젝트를 진행하고 있으며 관심있는 사람은 언제나 환영입니다.\n\n\n\
        \
        \
        ◎ 모집대상\n\
        •        전공/나이/학년 무관. 신입생 여러분 환영합니다! (*단 3학기 이상 활동이 가능한 자)\n\n\
        \
        ◎ 가입신청\n\
        •        https://goo.gl/forms/MIKEBpLVCE2fBxHq1\n\
        •        가입신청서 작성에 구글 로그인이 필요합니다.\n\n\
        \
        ◎ 학회실\n\
        •        신공학관 109호 ( 1층 우측 엘리베이터 옆)\n\n\
        \
        ◎ 가입신청 했습니다!\n\
        •        HandS에 오신 것을 환영합니다! 언제든 편한 시간에 신공학관 109호로 놀러오세요~ \n\n\
        \
        ◎ 신입생 OT / 개강총회\n\
        •        신입생은 OT에 필수 참여입니다.\n\
        •        3/15(목) 7시에 OT가 예정되어 있습니다.\n\
        •.       궁금한 사람은 모두 환영입니다. OT에 와보세요~\n\n\
        \
        ◎ 문의\n\
        •        회장 : 엄민성 (010-8321-7134)\n\
        •        부회장 : 나영채 (010-5198-1389)\n')


        self.driver.find_element_by_id('submm').click()

bot = koreapas_bot()
if bot.check() == 0:
    bot.login("","")#id password
    bot.new_advertisement()
    # bot.delete()
bot.close()
