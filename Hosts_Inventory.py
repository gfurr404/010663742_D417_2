#Why are we here, just to suffer

#Nah jk, this script is mostly a 1-1 recreation of the Switch Inventory with some minor changes.

import configparser
import yaml
import io

file_content = """
[WindowsDesktop-1]
ram=4096MB
vcpus=2
qemu_binary=/bin/qemu-system-x86_64(v4.2.1)
boot_priority=hdd
on_close=send_the_shutdown_signal(ACPI)
console_type=vnc
adapters=1
base_mac=0c:4b:3c:0a:00:00
type=Intel Gigabit Ethernet (e1000)
replicate_network_connection_status=Y

[WindowsDesktop-2]
ram=4096MB
vcpus=2
qemu_binary=/bin/qemu-system-x86_64(v4.2.1)
boot_priority=hdd
on_close=send_the_shutdown_signal(ACPI)
console_type=vnc
adapters=1
base_mac=0c:59:fd:86:00:00
type=Intel Gigabit Ethernet (e1000)
replicate_network_connection_status=Y

[WindowsDesktop-3]
ram=4096MB
vcpus=2
qemu_binary=/bin/qemu-system-x86_64(v4.2.1)
boot_priority=hdd
on_close=send_the_shutdown_signal(ACPI)
console_type=vnc
adapters=1
base_mac=0c:e2:07:f3:00:00
type=Intel Gigabit Ethernet (e1000)
replicate_network_connection_status=Y

[WindowsDesktop-4]
ram=4096MB
vcpus=2
qemu_binary=/bin/qemu-system-x86_64(v4.2.1)
boot_priority=hdd
on_close=send_the_shutdown_signal(ACPI)
console_type=vnc
adapters=1
base_mac=0c:46:74:35:00:00
type=Intel Gigabit Ethernet (e1000)
replicate_network_connection_status=Y

[Test_Box_1]
ram=4096MB
vcpus=2
qemu_binary=/bin/qemu-system-x86_64(v4.2.1)
boot_priority=hdd
on_close=send_the_shutdown_signal(ACPI)
console_type=vnc
adapters=1
base_mac=0c:cb:a8:90:00:00
type=Intel Gigabit Ethernet (e1000)
replicate_network_connection_status=Y

[Test_Box_2]
ram=4096MB
vcpus=2
qemu_binary=/bin/qemu-system-x86_64(v4.2.1)
boot_priority=hdd
on_close=send_the_shutdown_signal(ACPI)
console_type=vnc
adapters=1
base_mac=0c:50:a2:90:00:00
type=Intel Gigabit Ethernet (e1000)
replicate_network_connection_status=Y


         # End of Inventory #
"""

#Lemme Cook

file_name = "Host_Inventory.yaml"

config = configparser.ConfigParser()

config.read_string(file_content)

data_dict = {section: dict(config.items(section)) for section in config.sections()}

#I went from txt to ini to yaml, so I changed a LOT of this using random things online.
try:
    with open(file_name, "w", encoding="utf-8") as f:
        yaml.dump(data_dict, f, default_flow_style=False, sort_keys=False)
    print(f"YAML inventory '{file_name}' has been created successfully. Nice!")

except Exception as e:
    print(f"Dawg idk what happened, JK here is: {e}")

