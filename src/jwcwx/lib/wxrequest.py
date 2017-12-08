import xml.etree.ElementTree as ET

def extract(request):
    extract_data = {}
    data = request.data
    assert len(data) > 0, "接受到post的数据应该大于零字节"
    data_xml = ET.fromstring(data)
    extract_data['openID'] = data_xml.findtext('FromUserName')
    extract_data['wxOfficeAccount'] = data_xml.findtext('ToUserName')
    extract_data['msgType'] = data_xml.findtext('MsgType')
    extract_data['createTime'] = data_xml.findtext('CreateTime')
    extract_data['msgID'] = data_xml.findtext('MsgId')
    msgType = extract_data['msgType']

    if msgType is 'text':
        extract_data['textContent'] = data_xml.findtext('Content')
    elif msgType is 'image':
        extract_data['picUrl'] = data_xml.findtext('PicUrl')
        extract_data['mediaID'] = data_xml.findtext('MediaId')
    elif msgType is 'voice':
        extract_data['mediaID'] = data_xml.findtext('MediaId')
        extract_data['format'] = data_xml.findtext('Format')
        try:
            extract_data['recognition'] = data_xml.findtext('Recognition')
        except Exception:
            pass
    elif msgType is 'video' or is 'shortvideo':
        extract_data['thumbMediaID'] = data_xml.findtext('ThumbMediaId')
        extract_data['mediaID'] = data_xml.findtext('MediaId')
    elif msgType is 'location':
        extract_data['location_X'] = data_xml.findtext('Location_X')
        extract_data['location_Y'] = data_xml.findtext('Location_Y')
        extract_data['scale'] = data_xml.findtext('Scale')
        extract_data['label'] = data_xml.findtext('Label')
        extract_data['mediaID'] = data_xml.findtext('MediaId')
    elif msgType is 'link':
        extract_data['mediaID'] = data_xml.findtext('MediaId')
        extract_data['description'] = data_xml.findtext('Description')
        extract_data['title'] = data_xml.findtext('Title')
        extract_data['url'] = data_xml.findtext('Url')
    else:
        raise TypeError('不能识别的消息类型 {}'.format(msgType))


