#! /usr/bin/env python

import sys

def main(f_orig, f_new):
    print("Porting {} as {}".format(f_orig, f_new))
    with open(f_new, 'w') as f_out:
        start = False
        f_out.write("---\nlayout: site\n---\n")
        with open(f_orig, 'r') as f_in:
            for line in f_in:
                line = line.strip()
                if line.startswith("<body style=\"background: #f1f1f1;\">"):
                    start = True
                elif line.startswith("<div id=\"footerlinks\">"):
                    start = False
                elif start:
                    line = line.replace(".php", ".html")
                    f_out.write(line)
                    f_out.write("\n")



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
