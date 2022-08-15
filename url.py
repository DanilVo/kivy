import requests


url = 'https://redirector.googlevideo.com/videoplayback?expire=1660515920&ei=8CH5YrL7G9ac8gOmsqXYDg&ip=49.12.104.180&id=o-AP1Dx6JrtgE5SYx3ezP6sbM2-eWm5uydjfSnF1RqpSG-&itag=17&source=youtube&requiressl=yes&mh=kr&mm=31%2C29&mn=sn-4g5e6nzl%2Csn-4g5ednz7&ms=au%2Crdu&mv=m&mvi=5&pl=26&initcwndbps=283750&vprv=1&mime=video%2F3gpp&gir=yes&clen=4614018&dur=468.996&lmt=1560317795409435&mt=1660493808&fvip=5&fexp=24001373%2C24007246&c=ANDROID&rbqsm=fr&txp=2211222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOgu4zA49vOeo_hjEZ6hml3KgRIYJHwMf9bIIt_pDEP5AiEA1I5dK4XLDXN2gLoWd3ZNlIp4DTZlH410vrZEJ8qNqps%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgCu4O0Gk9BMpkfKBJHTDShCZhkIlVi_sOA400zxjPE1ACIQDTi6-WnY3RqWjsKHjked9rY927qaCEwZU0_AUj0vbvng%3D%3D&ratebypass=yes&utmg=ytap1_ErDn9K7uStk'
r = requests.get(url, allow_redirects=True)

open('facebook.ico', 'wb').write(r.content)