import os
import requests
from time import time as timer
from multiprocessing.pool import ThreadPool
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--batch", help="Path to file containing a list of URLs to download from", default="a.txt")

def fetch_url(entry):
    uri, path = entry
    if not os.path.exists(path):
        r = requests.get(uri, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    return path

if __name__ == '__main__':
    args = parser.parse_args()
    f = open(args.batch,'r')
    urls=[]
    for entry in f:
        urls.append(entry.split(','))
    print(urls)
    results = ThreadPool(8).imap_unordered(fetch_url, urls)
    start = timer()
    for path in results:
        print("Downloaded to: "+path)

    print(f"Completed! Elapsed Time: {timer() - start}")
    f.close()
