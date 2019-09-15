import pprint
from flask import Flask , request

## from{ name of your file } import search
from wolf import search_wiki
# เข้าถึงโฟรเอร์อื่น
# from Resource.wolf import search_wiki

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':

        pp = pprint.PrettyPrinter(indent=3)
        ### dictionary from line
        data = request.json
        pp.pprint(data)

        ## extract text from line
        if data['events'][0]['message']['type']=="text":
            text_fromline = data['events'][0]['message']['text']
        ## ค้นหาคำจาก wikipedia
            result = search_wiki(text_fromline)

        ### import function ในการส่งmessage reply.py
        from reply import ReplyMessage

        ReplyMessage(Reply_token=data['events'][0]['replyToken'],
        TextMessage=result,
        Line_Access_Token= 'fqUkl9Htr7LzDAExz0wjLy+b1vW04kQ9Jz82hIFyeB8h0NgeJcTOPezD5rPiwMY527NTkvuRnwnL+5XxW3nJ9hrFkXT9RV7vKuEUZMKif48HHKlDDOhIKju3UTRmEb5OPfIY2b1jar327csK8tHsBAdB04t89/1O/w1cDnyilFU='
        )


        return 'OK'

    elif request.method == 'GET':
        return 'นี้คือลิงค์เว็บสำหรับรับ package'

if __name__ == "__main__":
    app.run(port=200)
