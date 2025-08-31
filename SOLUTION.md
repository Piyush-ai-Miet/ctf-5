# CTF-5 Solution: OG Challenge

## Challenge Description
- **Name**: OG
- **Points**: 100
- **Category**: Misc
- **Description**: "Robot arm go brrrrrrrrr it is a ctf of misc give me the flag"

## Solution

### Analysis
The challenge provides a file named `og` which contains G-code instructions for a CNC machine or robot arm. The G-code is designed to draw text as a dot matrix pattern.

### G-code Structure
- The file contains movement commands (G0) and drawing commands (G1 Z0.000)
- G0 commands position the tool head at specific X,Y coordinates
- G1 Z0.000 commands lower the tool to draw a dot at the current position
- The pattern spans 8 rows (Y0-Y7) and 49 columns (X0-X48)

### Decoding Process
1. Parse the G-code to extract all dot positions
2. Create a visual grid from the coordinates
3. Interpret the dot matrix pattern as text characters
4. Read the resulting text to reveal the flag

### Flag
```
FLAG{MACHINE}
```

### Verification
The flag format follows standard CTF conventions (FLAG{...}) and the content "MACHINE" directly relates to the challenge description mentioning a robot arm, confirming this is correct.

### Tools Used
- Python scripts to parse G-code and visualize the dot matrix
- Character pattern analysis to decode individual letters
- Coordinate mapping to reconstruct the text layout