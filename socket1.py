if __name__=="__main__":
    input_bytes=b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'


    input_character=input_bytes.decode('utf-16')
    print(repr(input_character))

    output_charater="we copy you donw. Egale.\n"
    output_bytes=output_charater.encode('utf-8')
    with open('egale.txt','wb') as f:
        f.write(output_bytes)

        
