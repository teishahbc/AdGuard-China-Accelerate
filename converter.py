import sys
import re

def convert_list(input_filepath, output_filepath):
    with open(input_filepath, 'r') as source_file, open(output_filepath, 'w') as target_file:
        pattern_server = r'server='
        pattern_bracket = r'['
        
        old_dns = r'/114.114.114.114'
        new_dns = r'/]tcp://223.6.6.6'
            
        for line in source_file:
            converted_line = re.sub(pattern_server, pattern_bracket, line)
            final_line = re.sub(old_dns, new_dns, converted_line)
            target_file.write(final_line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python domain_list_converter.py <gfw|china> <input_file>")
        sys.exit(1)
        
    source_type = sys.argv[1]
    input_filepath = sys.argv[2]
    input_filename = input_filepath.split('/')[-1]
    input_filename = input_filename.split('.')[0]
    output_filename = f'{input_filename}_AdGuard.txt'
    output_filepath = f'./{output_filename}'
    
    convert_list(input_filepath, output_filepath)
