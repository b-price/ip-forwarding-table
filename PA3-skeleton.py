def ip_decimal_to_binary(ip_address):
    return '.'.join([bin(int(x)+256)[3:] for x in ip_address.split('.')])


def longest_prefix_match(ip_address, forwarding_table):
    # Initialize longest_match as None
    longest_match = None

    # Fill in start
    # Look up the forwarding table to find the longest prefix match record


    # Fill in end

    return longest_match

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
    ip_address = input("Enter IP address: ") # ip_address = 255.0.105.51
    
    longest_match = longest_prefix_match(ip_address, forwarding_table)
    
    if longest_match is not None:
        print("Print out the result\n")
    else:
        print("No matching entry found\n")
    
