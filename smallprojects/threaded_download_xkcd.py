#! python3
# threaded_download_xkcd.py - Downloads XKCD comics using multple threads

import requests, os, bs4, threading 
from pathlib import Path

xkcd_folder_path = f'{Path.home()}\\small-projects-python\\smallprojects\\xkcd_files'

# store comics in ./xkcd
os.makedirs(xkcd_folder_path, exist_ok=True) 

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):

        # Download the page using requests module.
        print(f'Downloading page https://xkcd.com/{url_number}')
        res = requests.get(f'https://xkcd.com/{url_number}')
        res.raise_for_status()

        # Create a soup object to parse raw html in res variable
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image by parsing through the HTML to find a <div> element with an ID of 'comic'.
        # with an img link inside.
        comic_elem = soup.select('#comic img')

        # If there are no results from searching the html, an error message will be given.
        # Else, the src link is grabbed from the element with an ID 
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = comic_elem[0].get('src')
            # download the Image.
            print(f'Downloading image {comic_url}')
            res = requests.get(f'https:{comic_url}')
            res.raise_for_status()

            # Save the image to ./xkcd.
            image_file = open(f'{xkcd_folder_path}\\xkcd{os.path.basename(comic_url)}', 'wb')

            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

# Create and start the Thread objects
download_threads = []
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1 # There is no comic 0, so set it to 1.
    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end.
for download_thread in download_threads:
    download_thread.join()

print('Done.')
