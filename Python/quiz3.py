site = "http://naver.com"
my_site=  site.replace("http://","")
x = my_site.index(".")
slice = my_site[:x]
password = slice[:3]+str(len(slice))+str(slice.count('e'))+"!"
print(password)