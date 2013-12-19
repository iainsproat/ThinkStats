import gzip
import urllib.request
from datetime import datetime
import os
import sys

def downloadAndDecompressFile(url, fileName, forceNewDownload):
    if forceNewDownload == 'False' and os.path.exists(fileName):
        print('File', fileName, 'already exist, so there is no need to download it again.  If you want to force a download use the forceNewDownload="True" parameter')
        return 0

    tempFileName = fileName + datetime.now().strftime("%Y-%m-%dT%H%M%SZ%f") + ".tmp"
    responseData = urllib.request.urlopen(url)
    output = open(tempFileName,'wb')
    output.write(responseData.read())
    output.close()

    f = gzip.open(tempFileName, 'rb')
    rawResponseData = open(fileName, 'wb')
    rawResponseData.write(f.read())
    rawResponseData.close()
    f.close()
    
    os.remove(tempFileName)

    
def main(name, forceNewDownload='False'):
    downloadAndDecompressFile('http://greenteapress.com/thinkstats/2002FemResp.dat.gz', '2002FemResp.dat', forceNewDownload)
    downloadAndDecompressFile('http://greenteapress.com/thinkstats/2002FemPreg.dat.gz', '2002FemPreg.dat', forceNewDownload)
    
if __name__ == '__main__':
    main(*sys.argv)