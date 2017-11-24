import time

def render(toUser, fromUser, msgType, msg):

    if msgType == 'text':
        createTime = int(time.time())
        replyMsg = '''<xml>
            <ToUserName><![CDATA[{toUserName}]]></ToUserName>
            <FromUserName><![CDATA[{fromUserName}]]></FromUserName>
            <CreateTime>{createTime}</CreateTime>
            <MsgType><![CDATA[{msgType}]]></MsgType>
            <Content><![CDATA[{content}]]></Content>
            </xml>'''.format(toUserName=toUser, fromUserName=fromUser, createTime=createTime, msgType = msgType, content =msg)
        return replyMsg
    else:
        return None