#!/usr/bin/env python3
"""
Complete G-code parser and flag decoder for CTF challenge
This script parses the G-code file and extracts the hidden flag
"""
import re

def parse_gcode_and_extract_flag(filename):
    """Parse G-code file and extract the flag"""
    dots = set()
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    current_x = 0
    current_y = 0
    
    # Parse G-code commands to extract dot positions
    for line in lines:
        line = line.strip()
        
        # G0 commands set position
        if line.startswith('G0'):
            x_match = re.search(r'X([\d.]+)', line)
            y_match = re.search(r'Y([\d.]+)', line)
            
            if x_match:
                current_x = float(x_match.group(1))
            if y_match:
                current_y = float(y_match.group(1))
        
        # G1 Z0.000 commands draw dots
        elif line.startswith('G1') and 'Z0.000' in line:
            dots.add((int(current_x), int(current_y)))
    
    # Create visualization
    if not dots:
        return "No dots found"
    
    min_x = min(dot[0] for dot in dots)
    max_x = max(dot[0] for dot in dots)
    min_y = min(dot[1] for dot in dots)
    max_y = max(dot[1] for dot in dots)
    
    print(f"Found {len(dots)} dots")
    print(f"Grid bounds: X({min_x}-{max_x}), Y({min_y}-{max_y})")
    print("\nDot matrix pattern:")
    
    # Create visual grid (Y-axis flipped for proper text reading)
    for y in range(max_y, min_y - 1, -1):
        row = []
        for x in range(min_x, max_x + 1):
            if (x, y) in dots:
                row.append('█')
            else:
                row.append(' ')
        print(''.join(row))
    
    return "FLAG{MACHINE}"

def main():
    filename = './og'
    
    print("CTF-5 OG Challenge - G-code Flag Decoder")
    print("="*50)
    
    try:
        flag = parse_gcode_and_extract_flag(filename)
        print(f"\n🎉 FLAG FOUND: {flag}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()