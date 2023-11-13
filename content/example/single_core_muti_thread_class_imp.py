import threading
import shutil
from pathlib import Path
import requests
import os

proxies = {
  'http': 'http://proxy-dmz.intel.com:911',
  'https': 'http://proxy-dmz.intel.com:912',
}

class DownloaderThread(threading.Thread):
    def __init__(self, url, target):
        super().__init__()
        self.url = url
        self.target = target

    def run(self):
        print(f"Starting {self.name}")

        fname = os.path.basename(self.url)
        path = self.target / fname


        with requests.get(self.url, stream=True, proxies=proxies) as r:
            print(f"Downloading {fname}...")
            with open(path, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
    
        print(f"Download complete for {fname}!")
        print(f"Completing {self.name}")

if __name__ == "__main__":
    itr_forms = [
        "https://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr1_english.pdf",
        "https://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr2_english.pdf",
        "https://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr3_english.pdf",
        "https://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr4_english.pdf",
        "https://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr5_english.pdf",
        "https://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr6_english.pdf",
        "https://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr7_english.pdf",
    ]

    target_path = Path("static") / "concurrency_example"
    shutil.rmtree(target_path, ignore_errors=True)
    target_path.mkdir()

    threads = []
    for itr_form in itr_forms:
        my_thread = DownloaderThread(itr_form, target_path)
        my_thread.start()
        threads.append(my_thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All downloads completed!")
