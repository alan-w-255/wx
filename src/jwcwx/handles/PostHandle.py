import xml.etree.ElementTree as ET
from flask import redirect, url_for
from lib import MsgRender
import logging
import setting

def handle(request):
    # 处理用户发送的消息
    from lib import wxrequest
    assert request.method == 'POST', '应该传入post请求'

    try:
        msg_data = wxrequest.extract(request)
        assert len(DATA) > 0, "接受到post的数据应该大于零字节"
        openid = msg_data['openID']
        wxOfficeAccount = msg_data['wxOfficeAccount']
        msgType =  msg_data['msgType']

        logging.debug("接收到的POST请求的DATA类型为 {}".format(msgType))

        if msgType == 'text': # 处理用户发出的文本信息
            import re
            from lib.bindUser import bind_user_reply
            textContent =  msg_data['textContent']
            if re.match(r'^绑定', textContent) is not None:
                # 绑定用户
                stid = re.search(r'\d{13}', textContent).group()
                passwd = re.search(r':[^\s]*', textContent).group().replace(':', '')

                logging.debug("请求绑定用户 {} {}".format(stid, passwd))
                return bind_user_reply(stid, openid, passwd)

            else:
                print("接收到用户文本消息 {content}".format(content=textContent))
                assert isinstance(textContent, str), 'text content 应该为 str 类型'

                print("{}发回消息给{}: {}".format(openid, wxOfficeAccount, textContent))

                return MsgRender.render(openid, wxOfficeAccount, 'text', textContent)

        elif msgType == 'image': # 处理用户发出的图片信息
            pass
        elif msgType == 'voice': # 处理用户发出的语音信息
            recog_text = msg_data['recognition']


        elif msgType == 'event': # 处理用户发出的事件信息
            eventType = data_xml.findtext('Event')
            print('处理实践类型{}'.format(eventType))
            if eventType == 'CLICK':
                event_key = data_xml.findtext('EventKey')
                if event_key == 'GET_TODAY_CLASS_SCHEDULE':
                    print('{}请求今日课表'.format(openid))
                    from handles import get_today_course
                    # todo: 今日课表推送
                    return MsgRender.render(openid, wxOfficeAccount, 'text', get_today_course(openid))

                elif event_key == 'get_today_tasks':
                    # todo: 今日任务推送
                    pass
                elif event_key == 'get_teaching_time_table':
                    # todo: 获取教学时间表
                    pass
                else:
                    pass
            elif eventType == 'VIEW':
                from webpages import user_binding
                event_key = data_xml.findtext('EventKey')
                print("请求网页{}".format(event_key))
                if event_key == 'http://www.baidu.com':
                    # todo: 
                    return redirect('http://www.baidu.com')
                if event_key == setting.user_binding_page:
                    # todo: 需要先跳转到认证界面
                    return redirect(user_binding())
            else:
                pass

        else:
            pass
    except Exception as e:
        print("Exception: 处理用户post请求时出错")
        print(e)
        return MsgRender.render(openid, wxOfficeAccount, 'text', '对不起,服务器故障')
    
