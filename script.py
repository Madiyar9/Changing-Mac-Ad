import subprocess
import random

def generate_random_mac():
    # Генерируем случайный MAC-адрес
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]

    return ':'.join(map(lambda x: "%02x" % x, mac))

def change_mac(interface, new_mac):
    print(f"Changing MAC address of {interface} to {new_mac}")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

# Замените "eth0" на имя вашего сетевого интерфейса
interface = "eth0"
new_mac = generate_random_mac()
change_mac(interface, new_mac)
