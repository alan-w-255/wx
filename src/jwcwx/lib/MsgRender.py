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
            print(replyMsg)
            return replyMsg

    else:
        return None
        # 返回其他类型消息

def image_render(toUser, fromUser, msgType, MediaId):
        createTime = int(time.time())
        replyMsg = '''<xml>
            <ToUserName><![CDATA[{toUserName}]]></ToUserName>
            <FromUserName><![CDATA[{fromUserName}]]></FromUserName>
            <CreateTime>{createTime}</CreateTime>
            <MsgType><![CDATA[{msgType}]]></MsgType>
            <Image>
                <MediaId><![CDATA[{media_id}]]></MediaId>
            </Image>
            </xml>'''.format(toUserName=toUser, fromUserName=fromUser, createTime=createTime, msgType = msgType, media_id=MediaId)
        print('return imageID: {}'.format(MediaId))
        return replyMsg