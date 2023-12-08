#-------Internet SpeedTest App-------#
from speedtest import Speedtest

def get_speed(test_type):
    try:
        speed = test_type()
        return speed / 1024 / 1024
    except Exception as e:
        print(f"Error getting {test_type.__name__} speed: {e}")
        return None

def print_speed(test_type, speed,error_message = None):
    if speed is not None:
        print(f"{test_type} Speed Test in Your Wifi is: {speed:.2f} mbps")
    else:
        print(f"Failed to get {test_type} speed.")
        if error_message:
            print(f"Error Details: {error_message}")

if __name__ == "__main__":
    wifi = Speedtest()

    # Test Download Speed
    print("Getting Download Speed...")
    download_speed  = get_speed(wifi.download)
    print_speed("Download", download_speed)

    print("." * 50)

    # Test Upload Speed
    print("Getting Upload Speed...")
    upload_speed  = get_speed(wifi.upload)
    print_speed("Upload", upload_speed)

