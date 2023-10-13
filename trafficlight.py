import time

def traffic_signal():
    while True:
        # North-South Road
        print("North-South Road")
        print("Green Light - Go")
        time.sleep(5)
        print("Yellow Light - Prepare to Stop")
        time.sleep(2)
        print("Red Light - Stop")
        time.sleep(5)

        # East-West Road
        print("East-West Road")
        print("Red Light - Stop")
        time.sleep(5)
        print("Yellow Light - Prepare to Stop")
        time.sleep(2)
        print("Green Light - Go")
        time.sleep(5)

if __name__ == "__main__":
    traffic_signal()
