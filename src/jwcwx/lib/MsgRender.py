import time

def render(toUser, fromUser, msgType, msg):

    if msgType == 'text':
        print('查询到的课表:')
        print(msg)
        if len(msg) is 0:
            msg = '今天没有课'
        elif isinstance(msg, list):
            temp = ''
            for x in msg:
                temp = temp + str(x)
                temp = temp + '\n\n'
            msg = temp
        

        createTime = int(time.time())
        replyMsg = '''<xml>
            <ToUserName><![CDATA[{toUserName}]]></ToUserName>
            <FromUserName><![CDATA[{fromUserName}]]></FromUserName>
            <CreateTime>{createTime}</CreateTime>
            <MsgType><![CDATA[{msgType}]]></MsgType>
            <Content><![CDATA[{content}]]></Content>
            </xml>'''.format(toUserName=toUser, fromUserName=fromUser, createTime=createTime, msgType = msgType, content =msg)
        print(replyMsg)

        return replyMsg
    else:
        return None