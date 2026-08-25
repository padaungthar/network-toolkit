import ipaddress

def calculate_subnet_info(ip_with_subnet):
    # Create an IP network object from the provided IP and subnet
    network = ipaddress.IPv4Network(ip_with_subnet, strict=False)
    
    # Calculate the network address
    network_address = network.network_address
    
    # Calculate the broadcast address
    broadcast_address = network.broadcast_address
    
    # Calculate the usable IP range
    usable_ips = list(network.hosts())
    
    # Determine the IP class
    first_octet = int(str(network.network_address).split('.')[0])
    
    if first_octet >= 1 and first_octet <= 126:
        ip_class = 'Class A'
    elif first_octet >= 128 and first_octet <= 191:
        ip_class = 'Class B'
    elif first_octet >= 192 and first_octet <= 223:
        ip_class = 'Class C'
    elif first_octet >= 224 and first_octet <= 239:
        ip_class = 'Class D (Multicast)'
    elif first_octet >= 240 and first_octet <= 255:
        ip_class = 'Class E (Experimental)'
    else:
        ip_class = 'Unknown Class'

    # Output results
    print(f"IP Address with Subnet: {ip_with_subnet}")
    print(f"Network Address: {network_address}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Usable IP Range: {usable_ips[0]} - {usable_ips[-1]}")
    print(f"Total Usable IPs: {len(usable_ips)}")
    print(f"IP Class: {ip_class}")

def calculate_ipv6_subnet_info(ip_with_subnet):
    # Create an IPv6 network object from the provided IP and prefix length
    network = ipaddress.IPv6Network(ip_with_subnet, strict=False)

    # Calculate the network address
    network_address = network.network_address

    # Calculate the first and last host addresses
    first_host = network.network_address + 1
    last_host = network.broadcast_address - 1

    # Total addresses in the subnet
    total_addresses = network.num_addresses

    # Determine the address type
    if network.is_multicast:
        address_type = 'Multicast'
    elif network.is_link_local:
        address_type = 'Link-Local'
    elif network.is_private:
        address_type = 'Unique Local (Private)'
    elif network.is_loopback:
        address_type = 'Loopback'
    elif network.is_reserved:
        address_type = 'Reserved'
    else:
        address_type = 'Global Unicast'

    # Output results
    print(f"IP Address with Prefix: {ip_with_subnet}")
    print(f"Network Address: {network_address}")
    print(f"Compressed Form: {network_address.compressed}")
    print(f"Expanded Form: {network_address.exploded}")
    print(f"Prefix Length: /{network.prefixlen}")
    print(f"Usable Host Range: {first_host.compressed} - {last_host.compressed}")
    print(f"Total Addresses: {total_addresses}")
    print(f"Total Usable Hosts: {total_addresses - 2 if network.prefixlen <= 126 else total_addresses}")
    print(f"Address Type: {address_type}")

def get_subnet_mask_info(ip_with_subnet):
    # Detect whether the input is IPv4 or IPv6
    if ':' in ip_with_subnet:
        calculate_ipv6_subnet_info(ip_with_subnet)
    else:
        calculate_subnet_info(ip_with_subnet)

# Main execution
if __name__ == "__main__":
    # User input for the IP address with subnet (CIDR notation)
    ip_with_subnet = input("Enter an IP address with subnet (e.g., 8.8.0.0/22 or 2001:db8::/32): ")

    # Calculate and display subnet information
    get_subnet_mask_info(ip_with_subnet)
