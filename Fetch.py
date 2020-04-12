#Made BY @But_why_god(Anon-Bot) If u edit this par then you will die in hell
import requests
import re
import time
import sys
import os
logoyu = """╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━╮╱╱╱╱╱╱╭╮╱
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╮┃╱╱╱╱╱╭╯╰╮
┃┃╱┃┃╭━━╮╭━━╮╭━━╮╱╱╱╱┃╰╯╰╮╭━━╮╰╮╭╯
┃╰━╯┃┃╭╮┃┃╭╮┃┃╭╮┃╭━━╮┃╭━╮┃┃╭╮┃╱┃┃╱
┃╭━╮┃┃┃┃┃┃╰╯┃┃┃┃┃╰━━╯┃╰━╯┃┃╰╯┃╱┃╰╮
╰╯╱╰╯╰╯╰╯╰━━╯╰╯╰╯╱╱╱╱╰━━━╯╰━━╯╱╰━╯\n\n"""
print('\033[0m'+logoyu)
startoftexdf = "\033[92;1;1m[\033[91;1;1m+\033[92;1;1m]"
bgcolor = '\033[106m'
redcolor = '\033[91;1;1m'
greencolor = '\033[92;1;1m'
def downimg(urlimageog):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	requestuo = Request(url=urlimageog, headers=headers) 
	with urlopen(requestuo) as imagedata:
		imagefileload = imagedata.read()
		hopa = open(imagenameudl,'wb')
		hopa.write(imagefileload)
def file_len(filname):
	with open(filname) as f:
		for i, l in enumerate(f):
			pass
		return i + 1
dgfgf = input(greencolor+f'{startoftexdf}Enter Search String \n{startoftexdf} ')
pagefindtr = 'placeholder\=\"Page\s\#\s\/\s(\d*)\"\>'
rucg = '\<title\>(\d*).*Wallpapers\s\|'
def animate():
	ho = 0
	while ho <= 5:
		sys.stdout.write('\rSearching.. |')
		time.sleep(0.1)
		sys.stdout.write('\rSearching.. /')
		time.sleep(0.1)
		sys.stdout.write('\rSearching.. -')
		time.sleep(0.1)
		sys.stdout.write('\rSearching.. \\')
		time.sleep(0.1)
		ho += 1
	sys.stdout.write('\rSearching Done!       \n')
animate()
urliu = requests.get(f'https://wall.alphacoders.com/search.php?search={dgfgf}')
if urliu.url == 'https://wall.alphacoders.com/finding_wallpapers.php':
	print(redcolor+'\n No Result Found')
	exit()
else:
	qwr = re.compile(pagefindtr)
	numpagey = qwr.findall(urliu.text)
	finfhf = re.compile(rucg)
	numberhgg = finfhf.findall(urliu.text)
	if bool(numberhgg) == False:
		print(redcolor+'No Result Found NO')
		exit()
	else:
		if 1 == 0:
			print(redcolor+'Something is Wrong')
			exit()
		else:
			if bool(numpagey) is False:
				numimagelolko = numberhgg[0]
				numpagere = 0
				print(greencolor+f'{startoftexdf}Total Images Found [{numimagelolko}]\n{startoftexdf}Total Pages Found [{numpagere}]\n')
			else:
				numpagere = numpagey[0]
				numimagelolko = numberhgg[0]
				print(greencolor+f'{startoftexdf}Total Images Found [{numimagelolko}]\n{startoftexdf}Total Pages Found [{numpagere}]\n')
			
aui = 1
pagefindtr = 'placeholder\=\"Page\s\#\s\/\s(\d*)\"\>'
	
while True:
	if numpagere == 0:
		numpfhg = 1
		break
	numpfhg =  int(input(f'{startoftexdf}Enter the Number of Pages (1-{numpagere})\n{startoftexdf}'))
	if numpfhg > int(numpagere):
		print(redcolor+f'Input out of range. Please Enter below {numpagere}\n{startoftexdf}')
		continue
	elif numpfhg < 0:
		print(redcolor + f'Please Enter More Than 0\n')
	else:
		break
filenamelol = input(greencolor+f'{startoftexdf}Name Of File to Add URL\n(Without Extension)\n{startoftexdf}')
newfilenum_txt = filenamelol+'.txt'
while aui <= int(numpfhg):
	pagenum_u = '&page={}'.format(str(aui))
	if '&page=1' in urliu.url:
		newstug = urliu.url.replace('&page=1',pagenum_u)
	else:
		newstug = '{}&page={}'.format(urliu.url,aui)
	au = requests.get(newstug)
	f = re.compile('https\:\/\/images(\d*)\.alphacoders\.com\/(\d{3})\/thumb\-350\-(\d{2,3}\d{3,4})\.(\w+)\"')
	list_folder = f.findall(au.text)
	lenlisto = len(list_folder)
	ayy = 0
	while ayy < lenlisto:
		listnum = list_folder[ayy]
		imagesubname = listnum[0]
		imagefolder = listnum[1]
		imagename = listnum[2]
		extename = listnum[3]
		imageurl = "https://images{}.alphacoders.com/{}/{}.{}\n"
		fileho = open(newfilenum_txt,'a')
		fileho.write(imageurl.format(imagesubname,imagefolder,imagename,extename))
		print(greencolor+f'{startoftexdf}{imageurl} \nAdded Successfully\n{aui}'.format(imagesubname,imagefolder,imagename,extename))
		ayy += 1
	fileho.close()
	list_folder = []
	aui += 1
def downloadfile_txt_lol():
	file_open_txt_lol = open(newfilenum_txt,'r')
	numlhkb = 1
	while numlhkb <= file_len(newfilenum_txt):
		ffygggvg_url = file_open_txt_lol.readlines[numlhkb]
		xitxtxtixixi = str(numlhkb)
		imagenameudl = 'image'+xitxtxtixixi
		downimg(ffygggvg_url)
while True:
	fine_pro_lol = input(greencolor+f'[1] To Download All Images.\n[2] To Download one random image From list.\nEnter:')
	if fine_pro_lol == '1' or fine_pro_lol == '2':
		if fine_pro_lol == '1':
			downloadfile_txt_lol(newfilenum_txt)
			break
		else:
			os.system('python Download.py')
			break
	else:
		continue
		