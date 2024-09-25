import threading
import time

def simulate_download(file_url, duration=2):
    """Simulate a file download by sleeping for some time."""
    print(f"Downloading {file_url}...")
    time.sleep(duration)
    print(f"Finished downloading {file_url}")

def download_files_with_threads(file_urls):
    """Download multiple files concurrently using threading."""
    threads = []
    for file_url in file_urls:
        thread = threading.Thread(target=simulate_download, args=(file_url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
