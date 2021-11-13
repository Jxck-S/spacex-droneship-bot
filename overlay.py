def info_overlay(map_file_name, ship_json, ship_window):
	from PIL import Image, ImageDraw, ImageFont

	# create Image object with the input image
	image = Image.open(map_file_name)
	image = image.convert("RGB")
	# initialise the drawing context with
	# the image object as background
	draw = ImageDraw.Draw(image)

	#Setup fonts
	fontfile = "./Roboto-Regular.ttf"
	font = ImageFont.truetype(fontfile, 14)
	mini_font = ImageFont.truetype(fontfile, 12)
	head_font = ImageFont.truetype(fontfile, 16)

	#Setup Colors
	black = 'rgb(0, 0, 0)' # Black
	white = 'rgb(255, 255, 255)' # White
	navish = 'rgb(0, 63, 75)'
	whitish = 'rgb(248, 248, 248)'
	yellow = 'rgb(234, 199, 45)'
	#Info Box
	draw.rectangle(((40, 425), (600, 590)), fill= black, outline=yellow)
	text = "A Shortfall of Gravitas"
	draw.text((56, 436), text, fill=white, font=head_font)

	text = f"Status: {ship_json['STATUS_NAME']}"
	draw.text((56, 470), text, fill=white, font=font)

	text = f"Destination: {ship_json['DESTINATION']}"
	draw.text((56, 490), text, fill=white, font=font)

	text = f"Speed: {ship_json['SPEED']}"
	draw.text((56, 510), text, fill=white, font=font)

	text = f"Next Port: {ship_window['next_port_name']}"
	draw.text((56, 530), text, fill=white, font=font)

	text = f"Lat: {ship_json['LAT']}, Lon: {ship_json['LON']}"
	draw.text((380, 470), text, fill=white, font=font)

	text = f"Timestamp: {ship_json['TIMESTAMP']}"
	draw.text((380, 510), text, fill=white, font=font)

	text = f"Heading: {ship_json['HEADING']}"
	draw.text((380, 530), text, fill=white, font=font)




	image.show()
	# save the edited image
	image.save(map_file_name)