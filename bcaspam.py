import requests


cookies = {
    'PHPSESSID': 'a6497aee85e7829c431672ab150f0bf9',
    'csrf': 'ecdd79e10a7b10f1df0f3287134f17a8',
    'fbcity': '4',
    'fre': '0',
    'rd': '1380000',
    'zl': 'en',
    'fbtrack': '9a60d21e3058a192b1d0570edc47fa6b',
    'ak_bmsc': '95C6AF609FF069211C7887EC620E069E~000000000000000000000000000000~YAAQfZYRYAciQvmMAQAA7MfXAhZ1kcgPonxsMeArE1s/BSgHbz3tr0TtR5yjvPtDI+wg04AA0ojX/kfZC+b96UYlxmFHd3ePmK5VopK75YnR2rss/lt/ZzfpBGgGKkE4cSIWcCcou5JKrIcTRObgKhinn/zR+l/F1+2aeZOhdQ3WKWb2eRzlAV3iAc+qDNo14V9nm/JfSsdRnTXMlliRA06KBOjIpZKl2pD7Fm+domW3mwCSmaNOigRHdNLIXcFt/fcW5i04U4Gxo3uHWmERSrhFNMUMBMliby7mdt+DC8Fae1sYRaSkl7S2BC8hk/P7dDap/Kd+SqybinQYSbpg1hp6FwnpNnt3pA4dMjrPF/GKwm2ZYL1v3hcwlwXYLRnodRRkxSJIgkzD5YvV',
    '_ga': 'GA1.1.464054626.1705149713',
    '_gid': 'GA1.2.2055188521.1705149713',
    '_gat_global': '1',
    '_gat_city': '1',
    '_gat_country': '1',
    '_gcl_au': '1.1.303690740.1705149713',
    '_ga_2XVFHLPTVP': 'GS1.1.1705149713.1.0.1705149713.60.0.0',
    '_ga_ZVRNMB4ZQ5': 'GS1.2.1705149714.1.0.1705149714.60.0.0',
    '_ga_X6B66E85ZJ': 'GS1.2.1705149714.1.0.1705149714.60.0.0',
    '_fbp': 'fb.1.1705149714304.1225299791',
    'cid': '2c4e3ed9-0308-4d16-a237-3a5c99f7e944',
    'oauth2_authentication_csrf': 'MTcwNTE0OTcxNnxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJREEwWVRkbE5ESXlaalU0TWpRMFpEUmhaRGhtWmpneFptVTJOekExTWpJeHzRPfkgFgvJ8okgXNUOuWce6C9TUDoMWy93u5s18cYliw==',
    'G_ENABLED_IDPS': 'google',
    'zxcv': '19b31100148597a81765f46aec0e56adc8c5f9dd7ab2952ca9ae0ccf',
    'cid': '2c4e3ed9-0308-4d16-a237-3a5c99f7e944',
    'purl': 'https://www.zomato.com',
    'callback': '',
}

headers = {
    'Host': 'accounts.zomato.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://accounts.zomato.com/zoauth/login?login_challenge=368829eab7ab43e2991c8a8b367417d0',
    'Content-Type': 'multipart/form-data; boundary=---------------------------24834847304053372771457526827',
    # 'Content-Length': '1717',
    'Origin': 'https://accounts.zomato.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'Te': 'trailers',
    # 'Cookie': 'PHPSESSID=a6497aee85e7829c431672ab150f0bf9; csrf=ecdd79e10a7b10f1df0f3287134f17a8; fbcity=4; fre=0; rd=1380000; zl=en; fbtrack=9a60d21e3058a192b1d0570edc47fa6b; ak_bmsc=95C6AF609FF069211C7887EC620E069E~000000000000000000000000000000~YAAQfZYRYAciQvmMAQAA7MfXAhZ1kcgPonxsMeArE1s/BSgHbz3tr0TtR5yjvPtDI+wg04AA0ojX/kfZC+b96UYlxmFHd3ePmK5VopK75YnR2rss/lt/ZzfpBGgGKkE4cSIWcCcou5JKrIcTRObgKhinn/zR+l/F1+2aeZOhdQ3WKWb2eRzlAV3iAc+qDNo14V9nm/JfSsdRnTXMlliRA06KBOjIpZKl2pD7Fm+domW3mwCSmaNOigRHdNLIXcFt/fcW5i04U4Gxo3uHWmERSrhFNMUMBMliby7mdt+DC8Fae1sYRaSkl7S2BC8hk/P7dDap/Kd+SqybinQYSbpg1hp6FwnpNnt3pA4dMjrPF/GKwm2ZYL1v3hcwlwXYLRnodRRkxSJIgkzD5YvV; _ga=GA1.1.464054626.1705149713; _gid=GA1.2.2055188521.1705149713; _gat_global=1; _gat_city=1; _gat_country=1; _gcl_au=1.1.303690740.1705149713; _ga_2XVFHLPTVP=GS1.1.1705149713.1.0.1705149713.60.0.0; _ga_ZVRNMB4ZQ5=GS1.2.1705149714.1.0.1705149714.60.0.0; _ga_X6B66E85ZJ=GS1.2.1705149714.1.0.1705149714.60.0.0; _fbp=fb.1.1705149714304.1225299791; cid=2c4e3ed9-0308-4d16-a237-3a5c99f7e944; oauth2_authentication_csrf=MTcwNTE0OTcxNnxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJREEwWVRkbE5ESXlaalU0TWpRMFpEUmhaRGhtWmpneFptVTJOekExTWpJeHzRPfkgFgvJ8okgXNUOuWce6C9TUDoMWy93u5s18cYliw==; G_ENABLED_IDPS=google; zxcv=19b31100148597a81765f46aec0e56adc8c5f9dd7ab2952ca9ae0ccf; cid=2c4e3ed9-0308-4d16-a237-3a5c99f7e944; purl=https://www.zomato.com; callback=',
}


#file = open("cakes.txt","w")
#while True:
#    number = input("Enter the number: ")
#    if number == "stop":
#        break
#    else:
#        file.write(number)

file = open("bcastudents.txt","r")
#proxyfile = open("httpproxies.txt","r")
for cake in file:
    data = f'-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="country_id"\r\n\r\n1\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="number"\r\n\r\n{cake}\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="type"\r\n\r\ninitiate\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="hash"\r\n\r\n\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="id_token"\r\n\r\n\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="fb_token"\r\n\r\n\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="email"\r\n\r\n\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="name"\r\n\r\n\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="otp"\r\n\r\n\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="csrf_token"\r\n\r\necdd79e10a7b10f1df0f3287134f17a8\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="lc"\r\n\r\n368829eab7ab43e2991c8a8b367417d0\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="verification_type"\r\n\r\ncall\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="message_uuid"\r\n\r\n\r\n-----------------------------24834847304053372771457526827\r\nContent-Disposition: form-data; name="theme"\r\n\r\n\r\n-----------------------------24834847304053372771457526827--\r\n'
    response = requests.post('https://accounts.zomato.com/login/phone', cookies=cookies, headers=headers, data=data, verify=False)