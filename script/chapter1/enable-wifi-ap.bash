# How to create a Raspi-based WiFi AP

sudo apt install hostapd dnsmasq -y

sudo cp ./dnsmasq.conf /etc/dnsmasq.conf
sudo cp ./dhcpcd.conf /etc/dhcpcd.conf
sudo cp ./hostapd.conf /etc/hostapd/hostapd.conf
sudo cp ./wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf

sudo systemctl stop hostapd.service
sudo systemctl unmask hostapd.service
sudo systemctl enable hostapd.service
sudo systemctl start hostapd.service
# sudo systemctl restart hostapd.service

sudo rfkill unblock wifi
