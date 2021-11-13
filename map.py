def get_map(center, file_name, api_key):
    import requests
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    center = str(center)
    zoom = 5

    r = requests.get(url + "center=" + center + "&zoom=" +
                    str(zoom) + "&size=800x800 &key=" +
                    api_key + "&maptype=satellite" +
                    f"&markers=|{center}")
                    #icon:http://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico

    # wb mode is stand for write binary mode
    f = open(file_name, 'wb')

    # r.content gives content,
    # in this case gives image
    f.write(r.content)

    # close method of file object
    # save and close the file
    f.close()