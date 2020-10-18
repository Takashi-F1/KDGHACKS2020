import socket
import time
from postZoom import postVideoText
from Morph_W2V import Morphological_Analysis,W2V
from gensim.models import KeyedVectors

host = '127.0.0.1'   # IPアドレス
port = 10500         # Juliusとの通信用ポート番号
# Juliusにソケット通信で接続
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
data = ""
model_dir = './entity_vector/entity_vector.model.bin'
model = KeyedVectors.load_word2vec_format(model_dir, binary=True)

print("please url : ")
url = input()
seq = 15
try:
    data = ""
    base_time=time.time()
    text_list = list()
    recog_text = ""
    print("start")
    while True:
        
        if '</RECOGOUT>\n.' in data:
            # 出力結果から認識した単語を取り出す
            for line in data.split('\n'):
                index = line.find('WORD="')
                if index != -1:
                    line = line[index+6:line.find('"', index+6)]
                    recog_text = recog_text + line

            # text_list.append(recog_text) #text_listに認識した文を追加していく
            
            print("認識結果: "+recog_text)
            data =""
        else:
            data += str(client.recv(1024).decode('shift_jis'))
            # print('NotFound')
            
        if time.time()-base_time>=30: #elapsed time 15sごとにprint
            print("30秒経過: ")
            print(recog_text)
            word_count = Morphological_Analysis(recog_text, ['名詞'])
            result = W2V(word_count,model)
            print("result: "+result)
            payload="「{}」の話".format(result)
            postVideoText(url, seq, payload)
            seq+=1
            base_time=time.time()
            recog_text = ""




except KeyboardInterrupt:
    print('finished')
    client.send("DIE".encode('shift_jis'))
    client.close()
