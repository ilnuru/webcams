import requests

from .models import Camera

def get_rtsp_link(link, email="spam@ilnu.ru"):
    add_url = "https://rtsp.me/add.php"
    rtsp_link = ''
    # link = "rtsp://185.147.82.220:554/G29_P1C1"
    # email = "spam@ilnu.ru"
    data = {'user_add': 'true', 'lang': 'en', 'rtspLink': link, 'rtspEmail': email, 'location': 'msk'}

    r = requests.post(add_url, data=data)

    answer = r.json()
    if answer.get('link'):
        # answer['link'] = '<a href="https://rtsp.me/embed/QF954S2a/" target="_blank">https://rtsp.me/embed/QF954S2a/</a>'
        rtsp_link = answer['link'][answer['link'].find(">")+1:answer['link'].rfind('</a>')]
    return rtsp_link

def get_camera_link(camera):
    ip_link = 'rtsp://%s:%s/' % (camera.house.ip_address.ip, camera.house.ip_address.port)
    mask = camera.mask
    if camera.mask == Camera.FRONT:
        mask = mask % (camera.house.number, camera.number)
    else:
        mask = mask % (camera.house.number, camera.entrance, camera.number)
    link = ip_link+mask
    return link