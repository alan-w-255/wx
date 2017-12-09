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

    if msgType == 'text':
        extract_data['textContent'] = data_xml.findtext('Content')
    elif msgType == 'image':
        extract_data['picUrl'] = data_xml.findtext('PicUrl')
        extract_data['mediaID'] = data_xml.findtext('MediaId')
    elif msgType == 'voice':
        extract_data['mediaID'] = data_xml.findtext('MediaId')
        extract_data['format'] = data_xml.findtext('Format')
        try:
            extract_data['recognition'] = data_xml.findtext('Recognition')
        except Exception:
            pass
    elif msgType == 'video':
        extract_data['thumbMediaID'] = data_xml.findtext('ThumbMediaId')
        extract_data['mediaID'] = data_xml.findtext('MediaId')
    elif msgType == 'shortvideo':
        extract_data['thumbMediaID'] = data_xml.findtext('ThumbMediaId')
        extract_data['mediaID'] = data_xml.findtext('MediaId')
    elif msgType == 'location':
        extract_data['location_X'] = data_xml.findtext('Location_X')
        extract_data['location_Y'] = data_xml.findtext('Location_Y')
        extract_data['scale'] = data_xml.findtext('Scale')
        extract_data['label'] = data_xml.findtext('Label')
        extract_data['mediaID'] = data_xml.findtext('MediaId')
    elif msgType == 'link':
        extract_data['mediaID'] = data_xml.findtext('MediaId')
        extract_data['description'] = data_xml.findtext('Description')
        extract_data['title'] = data_xml.findtext('Title')
        extract_data['url'] = data_xml.findtext('Url')
    elif msgType == 'event':
        extract_data['event'] = data_xml.findtext('Event')
        if extract_data['event'] == 'CLICK':
            extract_data['eventKey'] = data_xml.findtext('EventKey')
        elif extract_data['event'] == 'VIEW':
            extract_data['eventKey'] = data_xml.findtext('EventKey')
        elif extract_data['event'] == 'LOCATION':
            extract_data['latitude'] = data_xml.findtext('Latitude')
            extract_data['longitude'] = data_xml.findtext('Longitude')
            extract_data['precision'] = data_xml.findtext('Precision')
        elif extract_data['event'] == 'SCAN':
            extract_data['eventKey'] = data_xml.findtext('EventKey')
            extract_data['ticket'] = data_xml.findtext('Ticket')
        elif extract_data['event'] == 'subscribe':
            extract_data['eventKey'] = data_xml.findtext('EventKey')
            extract_data['ticket'] = data_xml.findtext('Ticket')
    
    else:
        raise TypeError('不能识别的消息类型 {}'.format(msgType))

    return extract_data


