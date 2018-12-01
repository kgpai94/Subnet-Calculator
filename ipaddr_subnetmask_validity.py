'''
Created on Nov 30, 2018

@author: KP
'''


import random
import sys


def subnetCal():
    try:
        print("\n")
        
        #code for checking the IP validity
        ip = input("Enter the IP address: ")
        ip = ip.rstrip("\n")
        ip_octets = ip.split('.')
        
        if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
            continue
             
        else:
            print('\n* There was an invalid IP address in the file: {} :(\n'.format(ip))
            sys.exit()

        
        masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]
        
        while True:
            subnet_mask = input("Enter the subnet mask: ")
            
            octets = subnet_mask.split('.')
            
            
            if (len(octets) == 4) and (int(octets[0]) == 255) and (int(octets[1]) in masks) and (int(octets[2]) in masks) and (int(octets[3]) in masks) and (int(octets[0]) >= int(octets[1]) >= int(octets[2]) >= int(octets[3])):
                break
                    
            else:
                print("\nThe IP address is invalid! Please retry with a correct IP address\n")
                continue
            
            
            octets_binary = []
            
            
            for i in octets:
                binary_i = bin(int(i)).lstrip('0b') 
                
                octets_binary.append(binary_i.zfill(8))
                
            bin_mask = "".join(octets_binary)
            
             
             
            no_of_zeroes = bin_mask.count("0")
            no_of_ones = 32 - no_of_zeroes
            no_of_hosts = abs(2 ** no_of_zeroes - 2)
            
            
            wildcard_octets = []
            
            
            for i in octets:
                temp = 255 - int(i)
                wildcard_octets.append(str(temp))
                
                
                wildcard_mask = ". ".join(wildcard_octets)
                
            ip_octets_binary = []
 
            for octet in ip_octets:
                binary_octet = bin(int(octet)).lstrip('0b')
                ip_octets_binary.append(binary_octet.zfill(8))
             
            binary_ip = "".join(ip_octets_binary)
             
            
             
            network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
            #print(network_address_binary)
             
            broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
            #print(broadcast_address_binary)
             
            
            net_ip_octets = []
             
            
            for bit in range(0, 32, 8):
                net_ip_octet = network_address_binary[bit: bit + 8]
                net_ip_octets.append(net_ip_octet)
             
            #print(net_ip_octets)
             
            net_ip_address = []
             
            for each_octet in net_ip_octets:
                net_ip_address.append(str(int(each_octet, 2)))
                
            #print(net_ip_address)
             
            network_address = ".".join(net_ip_address)
            #print(network_address)
             
            bst_ip_octets = []
            
            for bit in range(0, 32, 8):
                bst_ip_octet = broadcast_address_binary[bit: bit + 8]
                bst_ip_octets.append(bst_ip_octet)
             
            #print(bst_ip_octets)
             
            bst_ip_address = []
             
            for each_octet in bst_ip_octets:
                bst_ip_address.append(str(int(each_octet, 2)))
                
            #print(bst_ip_address)
             
            broadcast_address = ".".join(bst_ip_address)
            #print(broadcast_address)
             
            #Results for selected IP/mask
            print("\n")
            print("Network address is: %s" % network_address)
            print("Broadcast address is: %s" % broadcast_address)
            print("Number of valid hosts per subnet: %s" % no_of_hosts)
            print("Wildcard mask: %s" % wildcard_mask)
            print("Mask bits: %s" % no_of_ones)
            print("\n")
                
                
            
                
                 
                
            
            