
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
options = parser.parse_args()
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
def main(test_data=None, max_run_count=None):
    import configparser
    from requests.api import get
    config = configparser.ConfigParser()
    config.read('./conf.ini')
    google_api_key = config.get('GOOGLE', 'API_KEY')
    asog_droneship_ship_id  = config.get('TRACKING', 'SHIP_ID')

    import tweepy
    auth = tweepy.OAuthHandler(config.get('TWITTER', 'CONSUMER_KEY'), config.get('TWITTER', 'CONSUMER_SECRET'))
    auth.set_access_token(config.get('TWITTER', 'ACCESS_TOKEN'), config.get('TWITTER', 'ACCESS_TOKEN_SECRET'))
    tweet_api = tweepy.API(auth, wait_on_rate_limit=True)
    import time
    import json
    status = None
    destination = None
    next_port_name = None

    from datetime import datetime
    def status_update(text_update, ship_json, ship_window):
        text_update = "A Shortfall of Gravitas " + text_update
        print(text_update)
        import os
        map_file_name = "map.png"
        #Create Static Map
        from map import get_map
        ship_location = ship_json["LAT"] + ", " + ship_json["LON"]
        get_map(ship_location, map_file_name, google_api_key)
        from overlay import info_overlay
        info_overlay(map_file_name, ship_json, ship_window)
        #Tweet
        twitter_media_map_obj = tweet_api.media_upload(map_file_name)
        alt_text = f"{ship_location} "
        tweet_api.create_media_metadata(media_id= twitter_media_map_obj.media_id, alt_text= alt_text)
        tweet_api.update_status(status = (text_update), media_ids=[twitter_media_map_obj.media_id]).id
        #os.remove("map.png")
    run_count = 0
    while max_run_count is None or run_count < max_run_count:
        if test_data is None:
            ship_json = get_ship_id_json(asog_droneship_ship_id)
            ship_json = json.loads(ship_json)
            ship_window = json.loads(get_ship_id_window(asog_droneship_ship_id))
            ship_window_values = ship_window['values']
        else:
            ship_json = test_data['json'][run_count]
            ship_window_values = test_data['window'][run_count]

        if "STATUS_NAME" in ship_json.keys():
            if status is None:
                status = ship_json["STATUS_NAME"]
            elif status != ship_json["STATUS_NAME"]:
                status = ship_json["STATUS_NAME"]
                text_update = f"now {status}"
                status_update(text_update, ship_json, ship_window_values)
        if "DESTINATION" in ship_json.keys():
            if destination is None:
                destination = ship_json["DESTINATION"]
            elif destination != ship_json["DESTINATION"]:
                destination = ship_json["DESTINATION"]
                text_update = f"destination is now {destination}"
                status_update(text_update, ship_json, ship_window_values)

        if "next_port_name" in ship_window_values.keys():
            if next_port_name is None:
                next_port_name = ship_window_values["next_port_name"]
            elif status != ship_window_values["next_port_name"]:
                next_port_name = ship_window_values["next_port_name"]
                text_update = f"next port is now {next_port_name}"
                status_update(text_update, ship_json, ship_window_values)
        run_count += 1
        now = datetime.now().time()
        print("Check complete at", now, "Sleeping 30min")
        if test_data is None:
            time.sleep(1800)
def run_test():
    run_count = 2
    test_data = {
    "json" : [
        {'DESTINATION': "Crew-3", 'STATUS_NAME': "Stopped", 'SHIP_ID': '369987', 'MMSI': '309374000', 'SHIPNAME': 'INDEPENDENCE OF THE SEAS', 'LAT': '25.82438', 'LON': '-77.93564', 'SPEED': '0.00', 'HEADING': '21', 'COURSE': '21', 'SHIPTYPE': '60', 'LENGTH': '338.72', 'WIDTH': '39.03', 'FLAG': 'BS', 'TIMESTAMP': '2021-11-13 15:40:30', 'AVGSPEED': '16.6'},
        {'DESTINATION': "Port Canveral", 'STATUS_NAME': "Underway using Engine", 'SHIP_ID': '369987', 'MMSI': '309374000', 'SHIPNAME': 'INDEPENDENCE OF THE SEAS', 'LAT': '25.82438', 'LON': '-77.93564', 'SPEED': '0.00', 'HEADING': '21', 'COURSE': '21', 'SHIPTYPE': '60', 'LENGTH': '338.72', 'WIDTH': '39.03', 'FLAG': 'BS', 'TIMESTAMP': '2021-11-13 15:40:30', 'AVGSPEED': '16.6'}
        ],
    "window" : [
        {'next_port_name' : "CW3", 'light_iw': False, 'vessel_history_limit': 1, 'country_code': 'BS', 'show_chartering_btn': False, 'has_voyage_forecast_snippet': True, 'reported_draught': 'Reported Draught: 9m...raught: 9m', 'no_data_available': False, 'dest_class': 'gotocoords', 'port_data_x': '-77.94545', 'port_data_y': '25.823', 'last_pos': 1636818023, 'last_pos_tooltip': 1636818023, 'elapsed': 1636818023, 'timezone_offset': -300},
        {'next_port_name' : "PCV", 'light_iw': False, 'vessel_history_limit': 1, 'country_code': 'BS', 'show_chartering_btn': False, 'has_voyage_forecast_snippet': True, 'reported_draught': 'Reported Draught: 9m...raught: 9m', 'no_data_available': False, 'dest_class': 'gotocoords', 'port_data_x': '-77.94545', 'port_data_y': '25.823', 'last_pos': 1636818023, 'last_pos_tooltip': 1636818023, 'elapsed': 1636818023, 'timezone_offset': -300}
    ]}
    main(test_data, run_count)
if __name__ == "__main__":
    #run_test()
    if options.t:
       run_test()
    else:
       main()