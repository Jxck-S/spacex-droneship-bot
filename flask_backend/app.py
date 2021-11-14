# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, send_file


#os.chdir(r"C:\Users\Gfg\Desktop\geeks")

import os

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, static_url_path ="/static")
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
@app.route("/asog.json")
def asog_json():
    import json
    ship_json = json.loads(get_ship_id_json(6876716))
    from flask import jsonify
    response = jsonify(ship_json)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
@app.route("/asog_window.json")
def asog_window_json():
    import json
    ship_json = json.loads(get_ship_id_window(6876716))
    from flask import jsonify
    response = jsonify(ship_json)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()