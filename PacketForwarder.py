# By Ben Price and Conor Boyle

def ip_decimal_to_binary(ip_address):  # function returns binary ip
    return ' '.join([bin(int(x)+256)[3:] for x in ip_address.split('.')])


def longest_prefix_match(ip_address, forwarding_table):
    # Initialize longest_match as None
    longest_match = None
    matches = [0]*(len(forwarding_table)+1)  # initialize # of matches array. Elements correspond to interfaces
    bin_address = ip_decimal_to_binary(ip_address)

    # Look up the forwarding table to find the longest prefix match record
    for x in forwarding_table:  # checks each address in forwarding table
        pos = 0  # resets position in ip address
        current = x['prefix'][pos]  # current entry in the forwarding table
        interface = int(x['interface'])
        while pos < len(x['prefix']) - 1:
            if current == '*' or current == ' ':  # if space or wildcard, only move forward
                pos += 1
                current = x['prefix'][pos]
            elif current == bin_address[pos]:  # in case of digit match
                matches[interface] += 1
                pos += 1
                current = x['prefix'][pos]

            else:  # a mismatch will make the matches element of forward address 0 to reflect a mismatch and exit loop
                matches[interface] = 0
                break

    longest_match = matches.index(max(matches))  # sets the longest match out of all forwarding address interfaces
    digits_matched = max(matches)
    if longest_match == 0:
        longest_match = None  # in case of no matches

    return longest_match, digits_matched


# Example forwarding table
forwarding_table = [
    {'prefix': '11111111 00000000 011010** ********', 'interface': '1'},     # 255.0.104/22
    {'prefix': '11111111 00000000 0110101* ********', 'interface': '2'},     # 255.0.106/23
    {'prefix': '11111111 00000000 011***** ********', 'interface': '3'},     # 255.0.96/19
    {'prefix': '11111111 00000000 01101100 ********', 'interface': '4'},     # 255.0.108/24
    {'prefix': '11111111 00000000 10101010 0*******', 'interface': '5'},     # 255.0.170.0/25
]

while 1:
    # Get input IP address from user
    ip_address = input("Enter IP address: ")  # ip_address = 255.0.105.51

    print("Forwarding Table:")
    for rule in forwarding_table:
        print(f"Prefix: {rule['prefix']} \t Interface: {rule['interface']}")
    longest_match = longest_prefix_match(ip_address, forwarding_table)

    print("\nPacket Forwarding:")
    print(f"Packet with binary IP address: {ip_decimal_to_binary(ip_address)}")

    if longest_match[0] is not None:
        print(f"Forwarded to interface {longest_match[0]} "
              f"(rule {longest_match[0]} matched: {longest_match[1]} digits)")
    else:
        print("No matching entry found\n")
    
