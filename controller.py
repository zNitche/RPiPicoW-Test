import machine
import network


class Controller:
    def __init__(self):
        self.wlan = self.init_wlan()

        self.toggle_onboard_led(True)

    def toggle_onboard_led(self, state):
        led = machine.Pin("LED", machine.Pin.OUT)

        led.on() if state else led.off()

    def init_wlan(self):
        print("Wlan init...")

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

        return wlan

    def get_wifi_networks(self):
        print("Getting wifi networks...")

        if not self.wlan.active():
            self.wlan.active(True)

        networks = self.wlan.scan()

        return networks
