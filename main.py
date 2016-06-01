#!/bin/python

from fractions import gcd
import requests

page = requests.get("http://www.quantbet.com/quiz")

firstNumber  = int(page.text.split('<strong>')[1].split('</strong>')[0])
secondNumber = int(page.text.split('<strong>')[2].split('</strong>')[0])

responce = requests.post("http://www.quantbet.com/submit" , data={'divisor':gcd(firstNumber , secondNumber)} ,  cookies=page.cookies)

print('%s' , responce.text)
