
list = []
with open('provinces.txt','rt') as provinces_file:
    for line in provinces_file:
        strip_line = line.strip
        list.append(strip_line)
    
