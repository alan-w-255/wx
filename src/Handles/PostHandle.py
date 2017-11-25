import xml.etree.ElementTree as ET
from lib import MsgRender

def handle(request):
    # 处理用户发送的消息
    assert request.method == 'POST', '应该传入post请求'
    try:
        DATA = request.data
        assert len(DATA) > 0, "接受到post的数据应该大于零字节"
        data_xml = ET.fromstring(DATA)
        fromUserName = data_xml.findtext('FromUserName')
        toUserName = data_xml.findtext('ToUserName')
        msgType = data_xml.findtext('MsgType')
        print("接收到的POST请求的DATA类型为 {}".format(msgType))

        if msgType == 'text': # 处理用户发出的文本信息
            textContent = data_xml.findtext('Content')
            print("接收到用户文本消息 {content}".format(content=textContent))
            assert isinstance(textContent, str), 'text content 应该为 str 类型'

            print("{}发回消息给{}: {}".format(fromUserName, toUserName, textContent))

            return MsgRender.render(fromUserName, toUserName, 'text', textContent)
        elif msgType == 'image': # 处理用户发出的图片信息
            pass
        elif msgType == 'voice': # 处理用户发出的语音信息
            pass
        elif msgType == 'event': # 处理用户发出的事件信息

        else:
            pass
    except Exception as e:
        print("Exception: 处理用户post请求时出错")
        print(str(e))
        return MsgRender.render(fromUserName, toUserName, 'text', '对不起,服务器故障')
        
