pimport urllib.request
import re
import os


def fetch_pictures(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img class="j-pl-photoitem-img" style="(.*?)" data-width="172" data-height="129" data-bwidth="1440" data-bheight="1080" data-cpx="0" src="(.*?)" data-loaded="1" data-oriwidth="200"')
    picture_url_list = r.findall(html_content.decode('utf-8'))

    os.mkdir('liushishi')
    os.chdir(os.path.join(os.getcwd(), 'liushishi'))
    for i in range(len(picture_url_list)):
        picture_name = str(i) + '.jpg'
        try:
            urllib.request.urlretrieve(picture_url_list[i], picture_name)
            print("Success to download " + picture_url_list[i])
        except:
            print("Fail to download " + picture_url_list[i])

if __name__ == '__main__':
    fetch_pictures("https://user.qzone.qq.com/2219352323/4")
