import shutil
from pathlib import Path
import requests
import os


proxies = {
  'http': '',
  'https': '',
}

def download_file(url: str, target: Path):
    fname = os.path.basename(url)
    path = target / fname
    
    with requests.get(url, stream=True, proxies=proxies) as r:
        print(f"Downloading {fname}...")
        with open(path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    
    print(f"Download complete for {fname}!")
