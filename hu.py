#Made BY @But_why_god(Anon-Bot) If u edit this the you will die in hell
import requests
import re
aui = 1
while aui <= 5779:
	au = requests.get('https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page='+str(aui)).text
	f = re.compile('https\:\/\/images(\d*)\.alphacoders\.com\/(\d{3})\/thumb\-350\-(\d{5,6})\.(\w+)\"')
	list_folder = f.findall(au)
	lenlisto = len(list_folder)
	ayy = 0
	while ayy < lenlisto-1:
		listnum = list_folder[ayy]
		imagesubname = listnum[0]
		imagefolder = listnum[1]
		imagename = listnum[2]
		extename = listnum[3]
		imageurl = "https://images{}.alphacoders.com/{}/{}.{}\n"
		fileho = open("imageurl.txt",'a')
		fileho.write(imageurl.format(imagesubname,imagefolder,imagename,extename))
		print('Added Successfully')
		ayy += 1
	fileho.close()
	list_folder = []
	aui += 1