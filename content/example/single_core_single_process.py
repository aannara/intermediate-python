from downloader import download_file
from pathlib import Path
import shutil

if __name__ == "__main__":
    itr_forms = [
        "http://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr1_english.pdf",
        "http://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr2_english.pdf",
        "http://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr3_english.pdf",
        "http://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr4_english.pdf",
        "http://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr5_english.pdf",
        "http://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr6_english.pdf",
        "http://incometaxindia.gov.in/forms/income-tax%20rules/2023/itr7_english.pdf",
    ]

    target_path = Path("static") / "concurrency_example"
    shutil.rmtree(target_path, ignore_errors=True)
    target_path.mkdir(exist_ok=True, parents=True)

    for itr_form in itr_forms:
        download_file(itr_form, target_path)

    print("All downloads completed!")
