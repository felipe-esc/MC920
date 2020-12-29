#!usr/bin/python3

import sys, getopt
import numpy as np
import cv2
import string

def code_steganography(image, message, bit_plan):
    # convert data to bin
    text_bits = ''.join([format(ord(i), '08b') for i in remove_non_ascii(message)])

    data_index = 0
    data_len = len(text_bits)

    # hide data
    mask = (1 << bit_plan)
    for values in image:
        if data_index >= data_len:
            break
        for pixel in values:
            if data_index >= data_len:
                break

            r_bit = int(text_bits[(data_index)]) << bit_plan
            pixel[0] = (pixel[0] & ~mask) | r_bit
            data_index += 1

            if data_index < data_len:
                g_bit = int(text_bits[(data_index)]) << bit_plan
                pixel[1] = (pixel[1] & ~mask) | g_bit
                data_index += 1

            if data_index < data_len:
                b_bit = int(text_bits[(data_index)]) << bit_plan
                pixel[2] = (pixel[2] & ~mask) | b_bit            
                data_index += 1

    return image

def decode_steganography(image, bit_plan):
    bin_data = ""

    # get data
    for values in image:
        for pixel in values:
            r = str(pixel[0] >> bit_plan & 1)  
            g = str(pixel[1] >> bit_plan & 1)
            b = str(pixel[2] >> bit_plan & 1)
            bin_data += (r + g + b) 

    # convert data
    text = ''.join(chr(int(bin_data[i: i+8], 2)) for i in range(0, len(bin_data) - (len(bin_data) % 8), 8))
    text = text[:text.find('\0')]
    
    return remove_non_ascii(text)

def extract_bit_plan(image, bit_plan):
    return ((image >> bit_plan) & 1) * 255

def remove_non_ascii(text):
    return ''.join(filter(lambda x: x in set(string.printable), text))

def main(argv):
    input_img = ''
    output_img = ''
    code = -1
    text = ''
    separate = False
    bits_plan = -1
    
    try:
        opts, args = getopt.getopt(
                                    argv,
                                    "scdi:o:t:b:",
                                    [
                                        "input-file=",
                                        "output-file=",
                                        "text=",
                                        "bit-plan=",
                                        "code",
                                        "decode",
                                        "separate"
                                    ]
                                )
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--input-file"):
            input_img = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        elif opt in ("-t", "--text"):
            text = arg
        elif opt in ("-c", "--code"):
            code = 1
        elif opt in ("-d", "--decode"):
            code = 0
        elif opt in ("-s", "--separate"):
            separate = True
        elif opt in ("-b", "--bit-plan"):
            bits_plan = int(arg)
    
    while input_img == '':
        input_img = str(input('Input image file path: '))
    if code:
        while output_img == '':
            output_img = input('Output image file name: ')
    while code == -1:
        code_option = str(input("Code or Decode (c/d): "))
        if code_option == 'c':
            code = 1
        elif code_option == 'd':
            code = 0
        else:
            print("Invalid option! Try again.")
    while bits_plan < 0 or bits_plan > 2:
        bits_plan = int("Select a bit plan (0, 1 or 2): ")
    

    image = cv2.imread(input_img)
    if image is None:
        print ('Error opening image: ' + input_img)
        return -1
    if code and text == '':
        text = str(input("Please enter message or textfile to hide: "))

    # code
    if code == 1:
        # read message from file
        if text.endswith(".txt"):
            file = open(text, "r")
            if file is None:
                print ('Error opening file: ' + input_img)
                return -1
            out = code_steganography(
                                        image, 
                                        ''.join(file.readlines()) + '\0', 
                                        bits_plan
                                    )
            file.close()

        # message from input
        else: 
            out = code_steganography(
                                        image,
                                        text + '\0',
                                        bits_plan
                                    )
        
        cv2.imwrite(output_img, np.int32(out))
        
        # extracts bit plans to example plan changes
        if separate:
            output_img = output_img.split('.')

            extracted_bit_plan_0 = extract_bit_plan(out, 0)
            cv2.imwrite(
                            output_img[0] + "_bp0." + output_img[1],
                            np.int32(extracted_bit_plan_0)
                        )

            extracted_bit_plan_1 = extract_bit_plan(out, 1)
            cv2.imwrite(
                            output_img[0] + "_bp1." + output_img[1],
                            np.int32(extracted_bit_plan_1)
                        )

            extracted_bit_plan_2 = extract_bit_plan(out, 2)
            cv2.imwrite(
                            output_img[0] + "_bp2." + output_img[1],
                            np.int32(extracted_bit_plan_2)
                        )

            extracted_bit_plan_7 = extract_bit_plan(out, 7)
            cv2.imwrite(
                            output_img[0] + "_bp7." + output_img[1],
                            np.int32(extracted_bit_plan_7)
                        )
    
    # decode
    else:
        out = decode_steganography(image, bits_plan)
        if text.endswith(".txt"):
            file = open(text, "w")
            file.write(out)
            file.close()      
        else:
            print("### MESSAGE ###\n\n")
            print(out)  

if __name__ == "__main__":
    main(sys.argv[1:])
