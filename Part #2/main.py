import os
import requests
from bs4 import BeautifulSoup

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
os.system("clear")
url = "https://www.iban.com/currency-codes"


# iban.com 
# 국가 이름 & 통화 코드 배열 저장 
# ※ 일부 국가에는 통화가 없으므로 목록에 추가 x 
# 사용자 입력 ( 국가 목록에 있는 숫자만 허용 )
# try / for index

iban = requests.get(url)
iban_soup = BeautifulSoup(iban.text, "html.parser")
i_table = iban_soup.find("table", {"class": "table table-bordered downloads tablesorter"}) # iban_soup 의 결과를 i_table에 저장
               # 저장될때 리스트로 만들어지고 find_data에 저장  
find_data = i_table.find_all("td") # list

# 국가,코드,통화 저장
iban_data = []
iban_country = []
iban_code = []
iban_currency = []
# end 

for i in find_data:
  # 데이터 배열에 저장
    iban_data.append(i.string)
    try:
        if len(iban_data) > 0:
            for i in range(0,len(iban_data)//4): # for 문 데이터를 4를 나누기                                         데이터  = 1072개 확인
                iban_country.append(iban_data[i*4])  # [Country 0] 1 2 3
                iban_code.append(iban_data[2+(4*i)]) # 0 1 [Code 2] 3
                iban_currency.append(iban_data[1+(4*i)]) # 0 [Currency 1] 2 3
    except Exception as error:
        print("Error : ",error)
for i,  item in enumerate(iban_country):
    print("#",i,item)
    while True:
        try:

            print("Where are you from ? Choose a country by number\n")
            num= int(input("# :"))
            if num > len(iban_country):

                print("Choose a number from the list")
                continue
        except:
            
            print("That wasn't a number")
            retry = str(input("Retry ? y/n : "))
                
        if retry == "y":\

            continue

        elif retry == "n":
            print("Bye ~")
            break
        
print(f"{iban_country[num]}\n")
print(f"Now Choose another country\n")
second_num= int(input("# :"))
print(f"{iban_country[second_num]}")
print(f"How may {iban_code[num]} do you wnat to convert to {iban_code[second_num]} ?")


trans_input = str(input(""))
transferwise_url = f"https://transferwise.com/gb/currency-converter/{iban_code[num]}-to-{iban_code[second_num]}-rate?amount={trans_input}"

print(transferwise_url)
    
    
transferwise_request = requests.get(transferwise_url)
transfer_soup = BeautifulSoup(transferwise_request.text,"html.parser")
find_trans = transfer_soup.find("div", {"class": "row"})
print(find_trans)
    

print(int(trans_input), f"{iban_code[second_num]}", locale="ko_KR")

#   #-------------------------------------------------#
  

# https://transferwise.com/gb/currency-converter/gbp-to-usd-rate?amount=50
# How many {iban_code} do you want to convert to KRW?
# iban
