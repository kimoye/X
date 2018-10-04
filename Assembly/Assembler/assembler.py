# -*- coding: UTF-8 –*-
import struct
instruction_set = {
        'mov': 0b00100010

}


if __name__ == '__main__':
    try:
        input_code = open('./codetext.py', 'r')
        output_code = open('output.bin', 'ab')
        print('source code file has read:')
        for line in input_code.readlines():
            print('line' '----->>' 'instruction_set[line]')
            output_code.write(struct.pack('b', instruction_set[line]))
    finally:
        if input_code:
            input_code.close()
            print('file has closed')