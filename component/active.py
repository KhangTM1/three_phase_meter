import os
from datetime import datetime
from component.pubDataManufacturer import pub_data_manufacturer

def active(client, ID, vendor):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    pub_data_manufacturer(client, ID, vendor, current_time)

def run_once(client, ID, vendor):
    if not os.path.exists("already_run.txt"):
        active(client, ID, vendor)
        with open("already_run.txt", "w") as file:
            file.write("This program has already run once.")

# Gọi hàm run_once để kiểm tra xem đã chạy chương trình lần đầu tiên chưa
# run_once()
