def get_map(center, file_name, api_key):
    import requests
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    center = str(center)
    zoom = 5

    r = requests.get(url + "center=" + center + "&zoom=" +
                    str(zoom) + "&size=640x640 &key=" +
                    api_key + "&maptype=satellite" +
                    f"&markers=icon:https://i.postimg.cc/26GXVNhj/spacex-marker.png|{center}")

    # wb mode is stand for write binary mode
    f = open(file_name, 'wb')

    # r.content gives content,
    # in this case gives image
    f.write(r.content)

    # close method of file object
    # save and close the file
    f.close()