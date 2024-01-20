'''
Author: Logan Maupin
Date: 01/19/2024

The purpose of this module is to utilize the "ping" command in the shell
in combination with the system library, to ping all the devices within
the 255 length subnet on the local area network. It then prints a list of
all the active IPs on the network.
'''
import os
import socket


def get_gateway_ip(os_name: str) -> str:
    '''
    Gets the router's IP address for the LAN.

    Parameters:
    os: str - "windows" or "linux" or "mac"
    '''
    os_name = os_name.lower()
    if os_name not in ["windows", "linux", "mac", "nt"]:
        print("Please use a valid Operating System for this function call")
        raise ValueError
    
    # TODO: add support for other OS's lol
    if "nt" in os_name or "windows" in os_name:
        try:
            gateway_ip = socket.gethostbyname(socket.gethostname())
            return gateway_ip

        except Exception as e:
            print(f"Error: {e}")


def get_gateway_host_num(gateway_ip: str) -> str:
    return str(gateway_ip.split(".")[-1])


def get_active_ips_on_LAN() -> list[str]:

    active_ip_list = []
    gateway_address = get_gateway_ip(os.name)
    gateway_num = get_gateway_host_num(gateway_address)
    gateway_ip_without_host_num = gateway_address.replace(gateway_num, "")

    for i in range(1, 256):
        host_name = gateway_ip_without_host_num + str(i)
        if not i == gateway_num:
            response = str(os.system(f"ping -n 1 {host_name}"))
            if response == "1":
                active_ip_list.append(host_name)

    return active_ip_list


def print_ips(active_ip_list: list[str]) -> None:
    
    # clear the console so we can just see the output
    os.system("cls")

    if not active_ip_list:
        print("No active IPs found.")

    for ip in active_ip_list:
        print(ip)


def main():
    ip_list = get_active_ips_on_LAN()
    print_ips(ip_list)


if __name__ == "__main__":
    main()
