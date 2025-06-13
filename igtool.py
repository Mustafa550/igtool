import requests
import random
import string
import time
from cfonts import render

class LogoPrinter:
    @staticmethod
    def araf_logo():
        T = render('{INSTA  UNBAN }', colors=['white', 'red'], align='center')
        print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓

                      {T}
    ~ YAPIMCI @SPECTER(:AdMiN
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')

LogoPrinter.araf_logo()

araf_1 = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Emine", "Mustafa", "Zeynep", "Ali", "Elif", "Oğuz"]
araf_2 = ["Yılmaz", "Kara", "Demir", "Çelik", "Aydın", "Koç", "Polat", "Öztürk", "Arslan", "Yıldız"]

araf_3 = input("Instagram kullanıcı adınızı (@ ile birlikte girin): ")

while True:
    araf_4 = random.choice(araf_1)
    araf_5 = random.choice(araf_2)
    araf_6 = ''.join(random.choices(string.digits, k=3))
    araf_7 = f"{araf_4.lower()}.{araf_5.lower()}{araf_6}@gmail.com"

    araf_8 = f"Hello Dear Instagram Team. I have been with you since 2015 with my {araf_3} account. I was traveling like I do every day. I saw that my account was suspended and they said they would open it within 1 day. However, it's been 2 days and it still hasn't opened. I think this error needs to be corrected and that it is an Instagram error and I want what is necessary to be done. Best regards, Dear Instagram Team."

    araf_9 = {
        'csrf': 'bWz6Kn0K9VtAnDzCvFstPo',
        'datr': 'yD63Z26K_5CVLHQrCR9-hZ62',
        'locale': 'en_US',
    }

    araf_10 = {
        'accept': '*/*',
        'accept-language': 'tr',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.meta.com',
        'referer': 'https://www.meta.com/help/work/contact/599317765457601/',
        'sec-ch-ua': '"Opera GX";v="116", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0',
        'x-asbd-id': '359341',
        'x-fb-lsd': 'AVqg6XJgpG8',
    }

    araf_11 = f'jazoest=2925&lsd=AVqg6XJgpG8&name={araf_4}%20{araf_5}&email={araf_7}&description={araf_8}&access_before=Yes&support_form_id=599317765457601&support_form_locale_id=en_US&support_form_hidden_fields=%7B%7D&support_form_fact_false_fields=[]&__user=0&__a=1&__req=4&__hs=20141.BP%3ADEFAULT.2.0...0&dpr=1&__ccg=EXCELLENT&__rev=1020321434&__s=9wxzvd%3Aazoihk%3Au9053k&__hsi=7474304979465981918&__dyn=7xe6E5aQ1PyUbFp41twpUnwgU6C7UW7oowMxW0DUeU1nEhwem0nCq1ewcG0RU2Cwooa81VohwnU1e42C0sy0ny0RE2Jw8W1uw75w9O0h-0Lo6-0uS0ue1TwmU3yw&__csr=&__spin_r=1020321434&__spin_b=trunk&__spin_t=1740247239&__jssesw=1'

    araf_12 = araf_11.encode('utf-8')

    araf_13 = requests.post('https://www.meta.com/ajax/help/contact/submit/page', cookies=araf_9, headers=araf_10, data=araf_12)

    if "Form submitted successfully" in araf_13.text:
        print("Başarılı form")
    else:
        print("Başarısız form")

    time.sleep(4)
  
