import json
from faker import Faker
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import init, Fore, Back, Style
import time, re, string, random, sys, colorama
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
######## This script is only for educational purpose ########
########           use it on your own RISK           ########
######## I'm not responsible for any loss or damage. ########
########       caused to you using this script       ########
########             Coded by Steven#2207            ########
init(autoreset=True)
fc = Fore.CYAN
fg = Fore.GREEN
fw = Fore.WHITE
fr = Fore.RED
fb = Fore.BLUE
flb = Fore.LIGHTBLUE_EX
flg = Fore.LIGHTGREEN_EX
fy = Fore.YELLOW
fly = Fore.LIGHTYELLOW_EX
flc = Fore.LIGHTCYAN_EX
fm = Fore.MAGENTA
bc = Back.CYAN
bg = Back.GREEN
bw = Back.WHITE
br = Back.RED
bb = Back.BLUE
by = Fore.YELLOW
bm = Fore.MAGENTA
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
start_url = 'https://www.opencccapply.net/gateway/apply?cccMisCode='
clg_ids = ['941', '311', '361', '233']
allColleges = ['MSJC College', 'Contra Costa College', 'City College', 'Sacramento College']
country_codes = ['855', '561', '800', '325', '330', '229']
fake = Faker('en_US')
ex = fake.name().split(' ')
firstName = ex[0]
LastName = ex[1]
studentAddress = fake.address()
randomMonth = random.randint(1, 12)
randomDay = random.randint(1, 27)
randomYear = random.randint(1996, 1999)
randomEduMonth = random.randint(1, 12)
randomEduDay = random.randint(1, 27)
eduYears = [2019, 2020]
randomEduYear = random.choice(eduYears)
banner = f'''\n{flg}===================================================================  \n{flc}{flg}||{flc}               _____  __              __              __       {flg}||{flc}\n{flg}||{flc}              / ___/ / /_ __  __ ____/ /___   ____   / /_      {flg}||{flc}\n{flg}||{flc}              \\__ \\ / __// / / // __  // _ \\ / __ \\ / __/      {flg}||{flc}\n{flg}||{flc}             ___/ // /_ / /_/ // /_/ //  __// / / // /_        {flg}||{flc}\n{flg}||{flc}            /____/ \\__/ \\__,_/ \\__,_/ \\___//_/ /_/ \\__/        {flg}||{flc}\n{flg}||{flc}    __  ___        _  __ ______            _    __ ___   ____  {flg}||{flc}\n{flg}||{flc}   /  |/  /____ _ (_)/ // ____/___   ____ | |  / /<  /  / __ \\ {flg}||{flc}\n{flg}||{flc}  / /|_/ // __ `// // // / __ / _ \\ / __ \\| | / / / /  / / / / {flg}||{flc}\n{flg}||{flc} / /  / // /_/ // // // /_/ //  __// / / /| |/ / / /_ / /_/ /  {flg}||{flc}\n{flg}||{flc}/_/  /_/ \\__,_//_//_/ \\____/ \\___//_/ /_/ |___/ /_/(_)\\____/   {flg}||{flc}\n{flg}===================================================================          \n{flg}   Github Repo - {flc}https://github.com/StevenHubbard/StudentMailGen{Fore.RESET}\n\n\n'''

def postFix(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
def random_phone_num_generator():
    first = str(random.choice(country_codes))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)
def start_bot(start_url, email, college, collegeID):
    studentPhone = random_phone_num_generator()
    ex_split = studentAddress.split("\n")
    streetAddress = ex_split[0]
    if(re.compile(',').search(ex_split[1]) != None):
        ex_split1 = ex_split[1].split(', ')
        cityAddress = ex_split1[0]
        ex_split2 = ex_split1[1].split(' ')
        stateAddress = ex_split2[0]
        postalCode = ex_split2[1]
    else:
        ex_split3 = ex_split[1].split(' ')
        cityAddress = ex_split3[0]
        stateAddress = ex_split3[1]
        postalCode = ex_split3[2]
    random.seed()
    letters = string.ascii_uppercase
    middleName = random.choice(letters)
    fp = open('prefBrowser.txt', 'r')
    typex = fp.read()
    try:
        # For Chrome
        if typex == 'chrome':
            driver = webdriver.Chrome(executable_path=r'./webdriver/chromedriver')
        # For Firefox
        elif typex == 'firefox':
            driver = webdriver.Firefox(executable_path=r'./webdriver/geckodriver')
        elif typex == '':
            print(fr + 'Error - Run setup.py first')
            exit()
    except Exception as e:
        time.sleep(float(random.randint(20, 400)/1000))
        print('\n'+fr + 'Error - '+ str(e))
        exit()
    driver.maximize_window()
    driver.get(start_url)
    time.sleep(float(random.randint(400, 1000)/1000))
    driver.find_element_by_xpath('//*[@id="portletContent_u16l1n18"]/div/div[2]/div/a[2]').click()
    time.sleep(float(random.randint(400, 1000)/1000))
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "accountFormSubmit"))
    ).click()
    print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Account Progress - 1/3', end='')
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "inputFirstName"))
    ).send_keys(firstName)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "inputMiddleName"))).send_keys(middleName)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "inputLastName"))).send_keys(LastName)
    time.sleep(float(random.randint(20, 700)/1000))
    driver.find_element_by_xpath('//*[@id="hasOtherNameNo"]').click()
    driver.find_element_by_xpath('//*[@id="hasPreferredNameNo"]').click()
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputBirthDateMonth option[value="' + str(randomMonth) + '"]'))).click()
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputBirthDateDay option[value="' + str(randomDay) + '"]'))).click()
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputBirthDateYear'))).send_keys(randomYear)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputBirthDateMonthConfirm option[value="' + str(randomMonth) + '"]'))).click()
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputBirthDateDayConfirm option[value="' + str(randomDay) + '"]'))).click()
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputBirthDateYearConfirm'))).send_keys(randomYear)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, '-have-ssn-no'))).click()
    time.sleep(float(random.randint(3000, 4000)/1000))
    element = driver.find_element_by_id('accountFormSubmit')
    desired_y = (element.size['height'] / 2) + element.location['y']
    window_h = driver.execute_script('return window.innerHeight')
    window_y = driver.execute_script('return window.pageYOffset')
    current_y = (window_h / 2) + window_y
    scroll_y_by = desired_y - current_y
    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
    time.sleep(float(random.randint(400, 1000)/1000))
    element.click()
    print(flg+' (Success)')
    print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Account Progress - 2/3', end='')
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputEmail'))).send_keys(email)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputEmailConfirm'))).send_keys(email)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputSmsPhone'))).send_keys(studentPhone)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputStreetAddress1'))).send_keys(streetAddress)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputCity'))).send_keys(cityAddress)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputState option[value="' + stateAddress + '"]'))).click()
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputPostalCode'))).send_keys(postalCode)
    time.sleep(float(random.randint(1000, 2000)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'accountFormSubmit'))).click()
    try:
        time.sleep(float(random.randint(400, 1000)/1000))
        driver.find_element_by_xpath('//*[@id="messageFooterLabel"]').click()
        opError = True
        while opError != False:
            chkInputPhone = driver.find_element_by_id('inputSmsPhone')
            chkError = chkInputPhone.get_attribute('class')
            if chkError == 'portlet-form-input-field error':
                print('\n'+fc+sd+'['+fm+sb+'*'+fc+sd+'] '+fr + 'Invalid Number, Retrying....')
                chkInputPhone.clear()
                studentPhone = random_phone_num_generator()
                chkInputPhone.send_keys(studentPhone)
                time.sleep(float(random.randint(20, 400)/1000))
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputAlternatePhone_auth_txt'))).click()
                try:
                    time.sleep(2)
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="messageFooterLabel"]'))).click()
                except:
                    opError = False
            else:
                opError = False
                break
    except Exception as e:
        print(e)
    time.sleep(4)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'accountFormSubmit'))).click()
    try:
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'messageFooterLabel'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputAddressValidationOverride'))).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'accountFormSubmit'))).click()
    except:
        pass
    print(flg+' (Success)')
    userName = firstName + str(postFix(7))
    pwd = LastName + str(postFix(5))
    pin = postFix(4)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputUserId'))).send_keys(userName)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputPasswd'))).send_keys(pwd)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputPasswdConfirm'))).send_keys(pwd)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputPin'))).send_keys(pin)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputPinConfirm'))).send_keys(pin)
    time.sleep(float(random.randint(20, 700)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputSecurityQuestion1 option[value="5"]'))).click()
    time.sleep(float(random.randint(400, 1000)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputSecurityAnswer1'))).send_keys("John")
    time.sleep(float(random.randint(400, 1000)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputSecurityQuestion2 option[value="6"]'))).click()
    time.sleep(float(random.randint(400, 1000)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputSecurityAnswer2'))).send_keys(LastName)
    time.sleep(float(random.randint(400, 1000)/1000))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputSecurityQuestion3 option[value="7"]'))).click()
    time.sleep(float(random.randint(400, 1000)/1000))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'inputSecurityAnswer3'))).send_keys("Doe")
    print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+fr + 'Please fill the captcha in webdriver to proceed further')
    for d in range(1, 200):
        xx = driver.find_element_by_name('captchaResponse')
        tdt = xx.get_attribute('value')
        if tdt != '':
            print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flc + 'Captcha Solved, Executing Further')
            solved = 1
            break
        else:
            time.sleep(2)
            solved = 0
    if solved == 1:
        time.sleep(2)
        element = driver.find_element_by_id('accountFormSubmit')
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "accountFormSubmit"))).click()
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Account Progress - 3/3' +flg+ ' (Success)')
        fp = open(f'{str(firstName).lower()}Acc.json', 'a')
        birthDay = str(randomMonth) + '/' + str(randomDay) + '/' + str(randomYear)
        obj = dict({
            "Email": email,
            "Password": pwd,
            "UserName": userName,
            "First Name": firstName,
            "Middle Name": middleName,
            "Last Name": LastName, 
            "Date of Birth": birthDay,
            "College": college,
            "Pin": str(pin)})
        fp.write(json.dumps(obj))
        fp.close()
        print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flc + 'Account Created Successfully, Details saved in myccAcc.txt, Filling Application Form Now')
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="registrationSuccess"]/main/div[2]/div/div/button'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Details Progress - 1/8', end='')
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'application.termId')))
        dropdown_menu = Select(driver.find_element_by_name('application.termId'))
        dropdown_menu.select_by_index(1)
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputEduGoal option[value="B"]'))).click()
        time.sleep(2)
        dropdown_menu = Select(driver.find_element_by_id('inputMajorId'))
        dropdown_menu.select_by_index(random.randint(1, 7))
        time.sleep(2.5)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, '_eventId_continue'))).click()
        print(flg+' (Success)')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputAddressSame'))).click()
        time.sleep(2.5)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column2"]/div[6]/ol/li[2]/button'))).click()
        # Page 2
        dropdown_menu = Select(driver.find_element_by_name('appEducation.enrollmentStatus'))
        dropdown_menu.select_by_index(1)
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputHsEduLevel option[value="4"]'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        rndPassYear = [3, 4]
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputHsCompMM option[value="' + str(random.choice(rndPassYear)) + '"]'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputHsCompDD option[value="' + str(randomEduDay) + '"]'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputHsCompYYYY'))).send_keys(randomEduYear)
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputCaHsGradYes'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputCaHs3yearNo'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputHsAttendance option[value="1"]'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        bad_states = ['AA', 'AE', 'AP']
        if stateAddress in bad_states:
            stateAddress = 'CA'
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#hs-input-sf-state option[value="' + stateAddress + '"]'))).click()
        search = driver.find_element_by_id('hs-school-name')
        search.clear()
        search.send_keys('high')
        auto_complete = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'hs-suggestions')))
        time.sleep(2)
        parentElement = driver.find_element_by_class_name('autocomplete-menu')
        it = parentElement.find_elements_by_tag_name("li")
        if len(it) < 5:
            print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+fr + 'Changing State....')
            Select(driver.find_element_by_id('hs-input-sf-state')).select_by_value('CA')
            search.clear()
            search.send_keys('high', Keys.ENTER)
            auto_complete = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'hs-suggestions')))
            time.sleep(2)
            parentElement = driver.find_element_by_class_name('autocomplete-menu')
            it = parentElement.find_elements_by_tag_name("li")
            if len(it) > 5:
                print('['+fm+sb+'*'+fc+sd+'] '+flc + 'State Changed, Resuming')
        try:
            time.sleep(float(random.randint(400, 1000)/1000))
            it[random.randint(4, 8)].click()
        except Exception as e:
            print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+fr + str(e), 'can\'t click')
        time.sleep(float(random.randint(20, 400)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputGPA'))).send_keys(Keys.BACKSPACE, '400')
        time.sleep(float(random.randint(20, 400)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputHighestEnglishCourse option[value="4"]'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputHighestEnglishGrade option[value="A"]'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputHighestMathCourseTaken option[value="7"]'))).click()
        time.sleep(float(random.randint(20, 700)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputHighestMathTakenGrade option[value="A"]'))).click()
        time.sleep(4)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column2"]/div[14]/ol/li[2]/button'))).click()
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Details Progress - 2/8' +flg+ ' (Success)')
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Details Progress - 3/8', end='')
        # Military
        time.sleep(4)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputCitizenshipStatus option[value="1"]'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputMilitaryStatus option[value="1"]'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column2"]/div[6]/ol/li[2]/button'))).click()
        print(flg+' (Success)')
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Details Progress - 4/8', end='')
        # Residency
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputCaRes2YearsYes'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputHomelessYouthNo'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputIsEverInFosterCareNo'))).click()
        time.sleep(4)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column2"]/div[7]/ol/li[2]/button'))).click()
        print(flg+' (Success)')
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Details Progress - 5/8', end='')
        # Intersts
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputEnglishYes'))).click()
        time.sleep(2)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputFinAidInfoNo'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputAssistanceNo'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputAthleticInterest1'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        parentElement = driver.find_elements_by_class_name('ccc-form-layout')[5]
        element = parentElement
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        allElements = parentElement.find_elements_by_tag_name('li')
        rndList = [2, 1, 2, 2]
        occurance = 0
        inputChecked = False
        while occurance < 2:
            for elementxx in allElements:
                myRandom = random.choice(rndList)
                time.sleep(float(random.randint(20, 400)/1000))
                xx = elementxx.find_element_by_class_name('portlet-form-input-checkbox')
                if xx.get_attribute('id') == 'inputOnlineClasses' and inputChecked == False:
                    myRandom = 1
                    inputChecked = True
                if myRandom == 1:
                    occurance += 1
                    element = xx
                    desired_y = (element.size['height'] / 2) + element.location['y']
                    window_h = driver.execute_script('return window.innerHeight')
                    window_y = driver.execute_script('return window.pageYOffset')
                    current_y = (window_h / 2) + window_y
                    scroll_y_by = desired_y - current_y
                    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
                    time.sleep(float(random.randint(20, 400)/1000))
                    xx.click()
        time.sleep(2)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column2"]/div[9]/ol/li[2]/button'))).click()
        print(flg+' (Success)')
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Details Progress - 6/8', end='')
        # Demographic 
        time.sleep(4)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputGender option[value="Male"]'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputTransgender option[value="No"]'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputOrientation option[value="StraightHetrosexual"]'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputParentGuardianEdu1 option[value="6"]'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#inputParentGuardianEdu2 option[value="2"]'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputHispanicNo'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputRaceEthnicity800'))).click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputRaceEthnicity' + str(random.randint(801, 809))))).click()
        time.sleep(4)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column2"]/div[7]/ol/li[2]/button'))).click()
        print(flg+' (Success)')
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Details Progress - 7/8', end='')
        # Supplemental
        if collegeID == 1:
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_supp_MENU_1 option[value="AAAS"]'))).click()
            time.sleep(float(random.randint(20, 700)/1000))
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_supp_MENU_2 option[value="HS"]'))).click()
            time.sleep(float(random.randint(20, 700)/1000))
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_supp_MENU_3 option[value="6"]'))).click()
            time.sleep(float(random.randint(20, 700)/1000))
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_supp_MENU_4 option[value="H"]'))).click()
            time.sleep(float(random.randint(20, 700)/1000))
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'YESNO_1_no'))).click()
            time.sleep(4)
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="applyForm"]/main/div[3]/div[5]/ol/li[2]/button'))).click()
        elif collegeID == 2:
            pass

        elif collegeID == 3:

            try:
                element = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.ID, "_supp_MENU_1"))
                )
            except:
                pass
            Select(driver.find_element_by_id("_supp_MENU_1")).select_by_value('ENG')
            time.sleep(2)
            Select(driver.find_element_by_id("_supp_MENU_5")).select_by_value('N')
            Select(driver.find_element_by_id("_supp_MENU_6")).select_by_value('N')
            Select(driver.find_element_by_id("_supp_MENU_4")).select_by_value('OPT2')
            driver.find_element_by_id("_supp_CHECK_5").click()
            time.sleep(2)
            driver.find_element_by_name("_eventId_continue").click()
        elif collegeID == 4:
            time.sleep(2)
            driver.find_element_by_id("YESNO_1_yes").click()
            driver.find_element_by_id("YESNO_2_yes").click()
            time.sleep(2)
            driver.find_element_by_id("_supp_TEXT_1").send_keys(studentPhone.replace('-', ''))
            time.sleep(2)
            GPA = Select(driver.find_element_by_id('_supp_MENU_2'))
            GPA.select_by_value('4')
            time.sleep(2)
            units = Select(driver.find_element_by_id('_supp_MENU_8'))
            units.select_by_value('4')
            time.sleep(2)
            money = Select(driver.find_element_by_id('_supp_MENU_3'))
            money.select_by_value('30')
            time.sleep(2)
            house = Select(driver.find_element_by_id('_supp_MENU_4'))
            house.select_by_value('1')
            time.sleep(2)
            house = Select(driver.find_element_by_id('_supp_MENU_5'))
            house.select_by_value('B')
            time.sleep(2)
            driver.find_element_by_id("YESNO_4_yes").click()
            driver.find_element_by_id("YESNO_5_yes").click()
            time.sleep(2)
            driver.find_element_by_id("YESNO_6_yes").click()
            driver.find_element_by_id("YESNO_7_no").click()
            time.sleep(2)
            driver.find_element_by_id("YESNO_8_yes").click()
            driver.find_element_by_id("YESNO_9_no").click()
            driver.find_element_by_id("YESNO_10_no").click()
            time.sleep(float(random.randint(400, 1000)/1000))
            driver.find_element_by_id("YESNO_11_yes").click()
            time.sleep(float(random.randint(400, 1000)/1000))
            driver.find_element_by_id("YESNO_12_no").click()
            time.sleep(2)
            driver.find_element_by_id("YESNO_13_no").click()
            driver.find_element_by_id("YESNO_14_yes").click()
            question = Select(driver.find_element_by_id('_supp_MENU_6'))
            question.select_by_value('What school did you attend for sixth grade?')
            time.sleep(2)
            question = Select(driver.find_element_by_id('_supp_MENU_7'))
            question.select_by_value(
                'What is the first name of your least favorite relative?')
            time.sleep(float(random.randint(400, 1000)/1000))
            driver.find_element_by_id("_supp_TEXT_3").send_keys("Nulled")
            driver.find_element_by_id("_supp_TEXT_4").send_keys("Nulled")
            time.sleep(2)
            driver.find_element_by_name("_eventId_continue").click()
        print(flg+' (Success)')
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Details Progress - 8/8', end='')
        # Submission
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputConsentYes'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputESignature'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'inputFinancialAidAck'))).click()
        time.sleep(float(random.randint(400, 1000)/1000))
        print(flg+' (Success)')
        print('['+fm+sb+'*'+fc+sd+'] '+flc + 'Sleeping for 30 seconds, HOLD ON !!')
        time.sleep(30)
        element = driver.find_element_by_xpath('//*[@id="submit-application-button"]')
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        time.sleep(float(random.randint(400, 1000)/1000))
        element.click()
        time.sleep(2)
        confirmedText = driver.find_element_by_class_name('mypath-confirmation-text').text
        print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flc + confirmedText)
        driver.close()
    else:
        print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+fr + 'Timeout while Checking for captcha')
def main():
    sys.stdout.write(banner)
    print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flc + 'Select a college from all available colleges to proceed....\n')
    time.sleep(float(random.randint(20, 400)/1000))
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    for index, college in enumerate(allColleges):
        print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flg+ str(index + 1) + ' - ' + flc + college)
    isIDError = True
    while isIDError != False:
        print('\n'+fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flc + 'Enter college id for ex - 1 or 2 or 3.... : ', end='')
        try:
            userInput = int(input())
            if userInput > len(allColleges) or userInput < 1:
                print(fc+sd+'['+fm+sb+'*'+fc+sd+'] '+fr + 'Wrong College id')
            else:
                userInput = userInput - 1
                isIDError = False
        except KeyboardInterrupt:
            pass
            exit()
            isIDError=False
        except:
            pass
            isIDError = True
    time.sleep(float(random.randint(20, 400)/1000))
    print('\n'+fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flc + 'Selected College: ' + flg + allColleges[userInput])
    time.sleep(float(random.randint(20, 400)/1000))
    print('\n'+fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flc + 'Enter Your Email: ', end='')
    userEmail = input()
    time.sleep(float(random.randint(20, 400)/1000))
    print('\n'+fc+sd+'['+fm+sb+'*'+fc+sd+'] '+flc + 'Hold on Starting now, Keep checking this terminal for instructions')
    time.sleep(float(random.randint(400, 1000)/1000))
    reg_url = start_url + clg_ids[userInput]
    start_bot(reg_url, userEmail, allColleges[userInput], userInput + 1)
if __name__ == '__main__':
    main()