from controller import Controller
from config import Config


def main():
    controller = Controller()

    print(controller.get_wifi_networks())

    controller.connect_to_network(Config.WIFI_SSID, Config.WIFI_PASSWORD)

    if controller.wlan.isconnected():
        print(controller.get_wlan_config())


if __name__ == "__main__":
    main()
