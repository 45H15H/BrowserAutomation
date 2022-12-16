# from bs4 import BeautifulSoup
# import lxml

# HTMLFileToBeOpened = open("source.html", encoding="utf8")


# # Reading the file and storing in a variable
# contents = HTMLFileToBeOpened.read()
  
# # Creating a BeautifulSoup object and
# # specifying the parser 
# soup = BeautifulSoup(contents, 'lxml')
  
  
# # Using the prettify method to modify the code
# #  Prettify() function in BeautifulSoup helps
# # to view about the tag nature and their nesting

# from lxml import etree
# dom = etree.HTML(str(soup))
# print(dom.xpath('/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[2]/div[3]/ul/li[2]/div/div[2]/div/a/div/span/span[1]/text()'))

from bs4 import BeautifulSoup
import lxml

from login import page_source_

soup = BeautifulSoup(page_source_, 'lxml')
print(soup.prettify())
views = soup.find("section", id = "ember585")
print(views)

# //*[@id="ember585"]/div[3]/ul/li[1]/div/div[2]
# for i in views:
#     print(i.text)
