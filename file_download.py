import sys
import urllib.request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to the save the downloaded file", default='./file')
parser.add_argument("-u", "--url", help="URL to download the file from", default="https://1fhjlor.oloadcdn.net/dl/l/PdvQbiVUvWI1Slul/siDhfdOdRHI/Molly%27s.Game.2017.1080p.BluRay.x264-%5BYTS.AM%5D.mp4?mime=true")

def dlProgress(count, blockSize, totalSize):
      percent = float(count*blockSize*100.00/totalSize)
      sys.stdout.write("\rTotal Size: "+str(totalSize%1024)+"MB")
      sys.stdout.write("\tProgress: %d%%" % percent)
      sys.stdout.flush()

def download(url="https://1fhjlor.oloadcdn.net/dl/l/PdvQbiVUvWI1Slul/siDhfdOdRHI/Molly%27s.Game.2017.1080p.BluRay.x264-%5BYTS.AM%5D.mp4?mime=true",path="./file"):
    urllib.request.urlretrieve(url, path, reporthook=dlProgress)
    print("Done.")

if __name__ == '__main__':
    args = parser.parse_args()
    download(url = args.url, path = args.file)
