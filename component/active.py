import os
from datetime import datetime
from component.pubDataManufacturer import pub_data_manufacturer

def active(client, ID, vendor):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    pub_data_manufacturer(client, ID, vendor, current_time)

def run_once(client, ID, vendor, current_dir):
    if not os.path.exists(f"{current_dir}/already_run.txt"):
        active(client, ID, vendor)
        with open(f"{current_dir}/already_run.txt", "w") as file:
            file.write("This program has already run once.")
