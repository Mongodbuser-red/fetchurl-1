import random
import os
from datetime import datetime
import requests
import urllib
from urllib.request import urlopen, Request
from PIL import Image, ImageDraw, ImageFont
logoyu = """╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━╮╱╱╱╱╱╱╭╮╱
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╮┃╱╱╱╱╱╭╯╰╮
┃┃╱┃┃╭━━╮╭━━╮╭━━╮╱╱╱╱┃╰╯╰╮╭━━╮╰╮╭╯
┃╰━╯┃┃╭╮┃┃╭╮┃┃╭╮┃╭━━╮┃╭━╮┃┃╭╮┃╱┃┃╱
┃╭━╮┃┃┃┃┃┃╰╯┃┃┃┃┃╰━━╯┃╰━╯┃┃╰╯┃╱┃╰╮
╰╯╱╰╯╰╯╰╯╰━━╯╰╯╰╯╱╱╱╱╰━━━╯╰━━╯╱╰━╯\n\n"""
greencolor = '\033[92;1;1m'
startoftexdf = '\033[92;1;1m[\033[91;1;1m+\033[92;1;1m]'
print('\033[0m'+logoyu)
def file_len(filname):
	with open(filname) as f:
		for i, l in enumerate(f):
			pass
		return i + 1
while True:
	print(greencolor+f'{startoftexdf}Do You Have URL File? (y/n)\n{startoftexdf} ', end='')
	inlkih = input()
	if inlkih is 'n' or inlkih is 'N' or inlkih is 'y' or inlkih is 'Y':
		break
	else:
		continue
if inlkih is 'n' or inlkih is 'N':
	os.system('python fetch.py')
while True:
	image_url_file_name = input(greencolor+f'{startoftexdf}Enter URL File Name \n(with extension)\n{startoftexdf} ')
	if image_url_file_name is None:
		continue
	else:
		if not os.path.isfile(image_url_file_name):
			print(f'{startoftexdf}\033[31;1;1mFile is Not Exist in Current Directory')
			continue
		else:
			break
while True:
	image_file_name = input(greencolor+f'{startoftexdf}Enter Image File Name \n(Without extension)\n{startoftexdf} ')
	if image_file_name is None:
		continue
	else:
		break
def downimg(urlimageog):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	requestuo = Request(url=urlimageog, headers=headers)
	file_ext_image = urlimageog.split('.')
	global image_file_name_nooob
	loxpycfo = image_file_name+'.'+file_ext_image[3]
	image_file_name_nooob = loxpycfo.rstrip()
	
	with urlopen(requestuo) as imagedata:
		imagefileload = imagedata.read()
		hopa = open(image_file_name_nooob,'wb')
		hopa.write(imagefileload)
def getimage():
	if os.path.isfile(image_url_file_name):
		urlnuo = open(image_url_file_name,'r')
		ranho = random.randint(1,file_len(image_url_file_name)+1)
		holo = urlnuo.readlines()
		randomurl = holo[ranho]
		urlnuo.close()
		if os.path.isfile(image_file_name):
			os.system(f'rm {image_file_name}')
			downimg(randomurl)
		else:
			downimg(randomurl)
	else:
		if not os.path.isdir('resources'):
			os.system('mkdir resources')
		urllib.request.urlretrieve('https://raw.githubusercontent.com/NobArxtx/urkk/master/imageurl.txt','resources/imageurl.txt')
		urlnuo = open('resources/imageurl.txt','r')
		ranho = random.randint(1,file_len('resources/imageurl.txt')+1)
		holo = urlnuo.readlines()
		randomurl = holo[ranho]
		bolooh = randomurl
		urlnuo.close()
		if os.path.isfile(image_file_name_nooob):
			os.system(f'rm {image_file_name_nooob}')
			downimg(randomurl)
		else:
			downimg(randomurl)
getimage()
print(greencolor+f'{startoftexdf}Want to Edit image?[y/n]\n{startoftexdf}',end = '')
ioii = input()
if ioii == 'n' or ioii == 'N':
	exit()
loblo = input(greencolor+f'{startoftexdf}Enter String to Add in Image\n{startoftexdf} ')
print(greencolor+f"{startoftexdf}Enter Custom Font File Name For Water Mark\nDon't have Font File Press Enter\n{startoftexdf} ",end='')
add_string_font = input()
if not add_string_font:
	add_string_font = "Pacifico.ttf"
if loblo:
	currenuiy = loblo
else:
	currenuiy = datetime.now().strftime('%b %d %Y | Anon~Bot | %H:%M:%S')
while True:
	try:
		print(f'{startoftexdf}'+greencolor+f'Want to add Custom font and Custom Water Mark\n(y\n)\n{startoftexdf}',end='')
		ingigh = input()
		if ingigh == 'N' or ingigh == 'n' or ingigh == 'y' or ingigh == 'Y':
			break
		else:
			continue
	except ValueError:
		continue
if ingigh == 'N' or ingigh == 'n':
	watermarkb ='By @But_why_god'
	watermark_font = "Roboto-Bold.ttf"
else:
	print(f'{startoftexdf}'+greencolor+f'Enter Custom Water Mark\n{startoftexdf} ',end='')
	watermarkb = input()
	print(f"{startoftexdf}"+greencolor+f"Enter Custom Font File Name For Water Mark\nDon't have Font File Press Enter\n{startoftexdf} ",end='')
	watermark_font = input()
	if not watermark_font:
		watermark_font = "Roboto-Bold.ttf"
img = Image.open(image_file_name_nooob)
img = img.convert("RGB")
draw = ImageDraw.Draw(img)
current_time = datetime.now().strftime(watermarkb)
font = ImageFont.truetype(watermark_font, 56)
draw.text((8, 9),current_time,(120, 224, 143),font=font)
font = ImageFont.truetype(add_string_font, 80)
draw.text((8,60),currenuiy,(0, 210, 211),font=font)
img.save(image_file_name_nooob)
print('\nImage Downloaded And Edited Successfully')




















