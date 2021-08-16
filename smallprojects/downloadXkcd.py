#! python3
# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4, logging, time


logging.basicConfig(filename='', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# initializes URL for website
url = 'https://xkcd.com'

# stores comics in ./xkcd
os.makedirs('xkcd', exist_ok=True)


while not url.endswith('#'):
    # Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    logging.debug(f'Res:{res.text}')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    logging.debug(comic_elem)
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = f"https:{comic_elem[0].get('src')}"
    # Download the image.
    print(f'Downloading image {comic_url}')
    res = requests.get(comic_url)
    res.raise_for_status()

    # Save the image to ./xkcd.
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()
    # Get the previous button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = f"https://xkcd.com{prev_link.get('href')}"

print('Done.')