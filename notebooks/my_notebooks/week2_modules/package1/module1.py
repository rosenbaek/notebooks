import argparse
from urllib.request import urlopen

import webget

def scraper(url, destination):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    #Write to file 'w' creates file if not existing
    with open(destination, "w") as file:
        file.write(html)
    

if __name__ == '__main__':
    parser= argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='url to scrape')
    parser.add_argument('--destination', default='default_file.dat', help='The name of the file to store the url in')
    args = parser.parse_args()
    scraper(args.url, args.destination)
    print(args.url)

    webget.download(args.url);
