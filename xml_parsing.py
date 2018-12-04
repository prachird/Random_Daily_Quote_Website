from xml.etree.ElementTree import parse
import random

def parsing():
    doc = parse('/home/dPrachi/mysite/input.xml')

    number = random.randint(0,11)
    #print(number)


    for item in doc.iterfind('name'):
        if(int((item.find('number').text)) == number):
            quote = item.findtext('quote')
            author = item.findtext('author')
            return str(quote), author


