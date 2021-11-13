
def get_ship_id_json(ship_id):
    import requests
    headers = {
        'authority': 'www.marinetraffic.com',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'vessel-image': '00c6342aa2d903525f37f8511277d420fd10',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.marinetraffic.com/en/ais/home/shipid:6876716/zoom:10',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'vTo=1; SERVERID=app9; com.marinetraffic.android-smartbanner-closed=true',
        'if-modified-since': 'Thu, 11 Nov 2021 02:33:08 GMT',
    }

    response = requests.get(f'https://www.marinetraffic.com/map/getvesseljson/shipid:{ship_id}', headers=headers)
    return response.text



def get_ship_id_window(ship_id):
    import requests
    headers = {
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Vessel-Image': '00c6342aa2d903525f37f8511277d420fd10',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.marinetraffic.com/en/ais/home/centerx:-77.2/centery:31.2/zoom:10',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = (
        ('asset_type', 'ship'),
        ('id', ship_id),
    )

    response = requests.get('https://www.marinetraffic.com/en/ais/get_info_window_json', headers=headers, params=params)
    return response.text

import time
asog_droneship_ship_id = "369987"
import json
status = None
destination = None
next_port_name = None
while True:
    ship_json = get_ship_id_json(asog_droneship_ship_id)
    ship_json = json.loads(ship_json)
    if "STATUS_NAME" in ship_json.keys():
        if status is None:
            status = ship_json["STATUS_NAME"]
        elif status != ship_json["STATUS_NAME"]:
            status = ship_json["STATUS_NAME"]
            text_update = f"Now {status}"
    if "DESTINATION" in ship_json.keys():
        if status is None:
            destination = ship_json["DESTINATION"]
        elif status != ship_json["DESTINATION"]:
            destination = ship_json["DESTINATION"]
            text_update = f"Destination is now {destination}"

    ship_window = json.loads(get_ship_id_window(asog_droneship_ship_id))
    ship_window_values = ship_window['values']
    if "next_port_name" in ship_window_values.keys():
        if next_port_name is None:
            next_port_name = ship_window_values["next_port_name"]
        elif status != ship_window_values["next_port_name"]:
            next_port_name = ship_window_values["next_port_name"]
            text_update = f"Ships next port is now {next_port_name}"

    time.sleep(1800)