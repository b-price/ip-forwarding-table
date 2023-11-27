def ip_decimal_to_binary(ip_address):
    return ' '.join([bin(int(x)+256)[3:] for x in ip_address.split('.')])


def longest_prefix_match(ip_address, forwarding_table):
    # Initialize longest_match as None
    longest_match = None
    matches = [0]*(len(forwarding_table)+1)
    bin_address = ip_decimal_to_binary(ip_address)
    print(bin_address)

    # Fill in start
    # Look up the forwarding table to find the longest prefix match record
    for x in forwarding_table:
        # print(len(x['prefix']))
        pos = 0
        current = x['prefix'][pos]
        # print(f"{current} {pos}")
        while pos < len(x['prefix']) - 1:
            if current == bin_address[pos]:
                matches[x['interface']] += 1
                pos += 1
                current = x['prefix'][pos]
                # print(f"{current} {pos}")
            elif current == '*' or current == ' ':
                pos += 1
                current = x['prefix'][pos]
                # print(f"{current} {pos}")
            else:
                matches[x['interface']] = 0
                break

    longest_match = matches.index(max(matches))
    if longest_match == 0:
        longest_match = None

    # Fill in end

    return longest_match


# Example forwarding table
forwarding_table = [
    {'prefix': '11111111 00000000 011010** ********', 'interface': 1},     # 255.0.104/22
    {'prefix': '11111111 00000000 0110101* ********', 'interface': 2},     # 255.0.106/23
    {'prefix': '11111111 00000000 011***** ********', 'interface': 3},     # 255.0.96/19
    {'prefix': '11111111 00000000 01101100 ********', 'interface': 4},     # 255.0.108/24
    {'prefix': '11111111 00000000 10101010 0*******', 'interface': 5},     # 255.0.170.0/25
]

while 1:
    # Get input IP address from user
    ip_address = input("Enter IP address: ")  # ip_address = 255.0.105.51
    
    longest_match = longest_prefix_match(ip_address, forwarding_table)
    
    if longest_match is not None:
        print(f"Longest match: Interface {longest_match}")
    else:
        print("No matching entry found\n")
    
