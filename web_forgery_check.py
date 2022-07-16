from urllib.request import urlopen
import urllib.request
import requests
import time
import sys

url = "http://" + sys.argv[1]
loop_cycle = int(sys.argv[2])
#print("webpage: ", url, " loop minutes: ", loop_cycle)
response = requests.get(url)

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
    



# original 웹사이트 title
title_index = html.find("<title>")
title_start_index = title_index + len("<title>")
title_end_index = html.find("</title>")
title = html[title_start_index:title_end_index]

#original 웹사이트 content
body_index = html.find("<body>")
body_start_index = body_index + len("<body>")
body_end_index= html.find("</body>")
body = html[body_start_index:body_end_index]
body_len = body_end_index - body_start_index
#print(body)

# original title, body_len
original_title = title
original_body_len = body_len
orignal_body = body



#while True:
while True:
    response = requests.get(url)
    status_code = response.status_code
    #print("response: ", response)
    #print("response status code ", response.status_code)


    if(status_code == 200):
        check_url = urllib.request.urlopen(url)
        resouce_check = check_url.status
        
        check_title_index = html.find("<title>")
        check_title_start_index = check_title_index + len("<title>")
        check_title_end_index = html.find("</title>")
        check_title = html[check_title_start_index:check_title_end_index]

        check_body_index = html.find("<body>")
        check_body_start_index = body_index + len("<body>")
        check_body_end_index= html.find("</body>")
        check_body = html[body_start_index:body_end_index]
        check_body_len = body_end_index - body_start_index


        '''print error check
            original_title = "try"
            check_title = "try"
            original_body_len = 1
            check_body_len = 2
            status_code = 200
            print("Noti: [Alert] www.example.com Title Change(\"",original_title, "\"", " to \"",check_title, "\"", ")" )
            print("Noti: [Alert] www.example.com Contents lengths change(", original_body_len, "to", check_body_len, ")")
            print("Noti: [Error] www.example.com ", status_code, " Error")
        '''
   


        if(check_title != original_title):
            print("Noti: [Alert] www.example.com Title Change(\"",original_title, "\"", " to \"",check_title, "\"", ")" )           
        if(check_body_len != original_body_len):
            print("Noti: [Alert] www.example.com Contents lengths change(", original_body_len, "to", check_body_len, ")")

    else:
       print("Noti: [Error] www.example.com ", status_code, " Error")
    
    
    time.sleep(60*loop_cycle)
    




