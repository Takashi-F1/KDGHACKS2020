import requests


def postVideoText(url, seq, payload):

    url = url + "&lang=jp-JP"+"&seq="+str(seq)
    print(url)

    headers = {
        'Content-Type': 'text/plain'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload.encode("utf-8"))

    print(response.text.encode('utf8'))



# seq = 19
# payload = "test"

# print("please url : ")
# url = input()
# postVideoText(url, seq, payload)
# seq+=1

