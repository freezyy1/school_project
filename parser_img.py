# берем изображение с сайта
import requests
link = "https://www.school5-tmn.ru/images/Doc/rasp_zvon.JPG"
filename = link.split('/')[-1]
r = requests.get(link, allow_redirects=True)
open(filename, "wb").write(r.content)
