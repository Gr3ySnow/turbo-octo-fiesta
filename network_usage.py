import psutil
import time

UPDATE_DELAY = 5 # in seconds

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

io = psutil.net_io_counters()

bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

def net_monitor():

    while True:

        time.sleep(UPDATE_DELAY)

        io_2 = psutil.net_io_counters()

        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - io_2.bytes_recv

        print (f"Upload: {get_size(io_2.bytes_sent)}   ")




if __name__ == "__main__":
    net_monitor()