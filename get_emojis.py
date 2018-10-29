import requests
from bs4 import BeautifulSoup
import argparse
import os



def same_image(title, pic_url):
    with open(title, 'wb') as handle:
        print("downloading {}...".format(title))
        response = requests.get(pic_url, stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)





def get_images_url(links_responses, source=1):
    for link in links_responses:
        if source == 1:
            pic_url = link.get('href')
            title = pic_url.replace("https://", "").split("/")[-1].split("?")[0]
        if source == 2:
            pic_url = link.get("src")
            extension = pic_url.replace("https://", "").split("/")[-1].split(".")[1]
            title = "{}.{}".format(link.findNext("div").text.replace(":", ""), extension)
        if os.path.isfile(title):
            print("{} already exists.".format(title))
            continue
        same_image(title, pic_url)
    





def main(base_url=None, source=1):
    r = requests.get(base_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    if source == 1:
        if not base_url:
            print("No base url")
            quit()
        links_responses = soup.find_all("a", "downloader")
        get_images_url(links_responses)
    if source == 2:
        imgs = soup.find_all("img")
        get_images_url(imgs, source)






if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="Source 1 'slackmojis.com', source 2 'emojipacks.com'. \n Default 1", type=int)
    parser.add_argument("-c", "--category", help="Enter any category from Emojipacks https://emojipacks.com/packs/${CATEGORY}. \nThis option only works with source 2.", type=str)
    args = parser.parse_args()

    base_url = "https://slackmojis.com"

    if not args.source:
        print("Please add a source.")
        parser.parse_args(["-h"])
        quit()
    
    if args.source:
        if args.source not in [1,2]:
            print("Source should be either 1 or 2")
            quit()
        if args.source == 2:
            base_url = "https://emojipacks.com"
            if args.category:
                base_url = "{}/packs/{}".format(base_url, args.category)
            else:
                print("Need a category for source 2")
                quit()
    main(base_url, args.source)