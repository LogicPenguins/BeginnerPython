#! python3
# imgur-downloader.py

import os
import requests
import bs4

def downloader(query, max_save, output_path):
    """
    Args:
        query (str): search query
        max_save (int): max number of images to save to results
    Returns:
        None
    """

    # create imgur search url
    search_url = 'https://imgur.com/search'
    query_url = f'{search_url}?q={query}'

    # set up output_path (on my computer this will be in downloads folder, but the path will typically be your current working dir)
    abs_output_path = os.path.abspath(output_path)
    os.makedirs(abs_output_path, exist_ok=True)

    # Make request to imgur with query
    page_info = requests.get(query_url)

    try:
        page_info.raise_for_status()

        # parse res.text with bs4 to images
        imugur_soup = bs4.BeautifulSoup(page_info.text, 'html.parser')
        images = imugur_soup.select('.image-list-link img')

        # extract number image urls
        num_to_save = min(max_save, len(images))
        download_links = [f"https:{img.get('src')}" for img in images[:num_to_save]]

        # make requests for extracted url
        for link in download_links:
            print(f'Downloading {link}...')
            # request image link from imgur
            res2 = requests.get(link)

            try:
                res2.raise_for_status()
                
                # save to file with url base name in folder results
                imgFile = open(os.path.join(abs_output_path, os.path.basename(link)), 'wb')
                for chunk in res2.iter_content(100000):
                    imgFile.write(chunk)
                imgFile.close()

            except Exception as exc:
                print(f'There was a problem: {exc}')

    except Exception as exc:
        print(f'There was a problem: {exc}')

if __name__ == '__main__':
    downloader('python programming', 10, 'results')