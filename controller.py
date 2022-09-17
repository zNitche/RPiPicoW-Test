import machine
import network
import time
from config import Config


class Controller:
    def __init__(self):
        self.wlan = self.init_wlan()

        self.onboard_led = machine.Pin("LED", machine.Pin.OUT)

        self.toggle_onboard_led(True)

    def toggle_onboard_led(self, state):
        self.onboard_led.on() if state else self.onboard_led.off()

    def init_wlan(self):
        print("WLAN init...")

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

        return wlan

    def activate_wlan_if_disabled(self):
        if not self.wlan.active():
            print("Enabling WLAN interface...")

            self.wlan.active(True)

    def connect_to_network(self, ssid, password):
        attempts = 0

        self.activate_wlan_if_disabled()

        print("Connecting to WIFI network...")

        while not self.wlan.isconnected() and attempts < Config.MAX_WIFI_RECONNECT_ATTEMPTS:
            print("Trying to establish WiFi connection...")

            self.wlan.connect(ssid, password)

            time.sleep(1)

            attempts += 1

        print(f"Connected to '{ssid}' network...") if self.wlan.isconnected() else print("Failed to connect...")

    def get_wlan_config(self):
        config = None

        if self.wlan.active() and self.wlan.isconnected():
            config = self.wlan.ifconfig()

        return config

    def get_wifi_networks(self):
        print("Getting wifi networks...")

        self.activate_wlan_if_disabled()

        networks = self.wlan.scan()

        return networks
