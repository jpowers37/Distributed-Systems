import sys
import getopt

def main():
    opt_o = None
    opt_t = None
    opt_h = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:t:h")
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-o':
            opt_o = arg
        elif opt == '-t':
            opt_t = arg
        elif opt == '-h':
            opt_h = True

    print("Standard Input:")
    for line in sys.stdin:
        print(line, end='')

    print("Command line arguments:")    
    if opt_o:
        print(f"-o: {opt_o}")
    if opt_t:
        print(f"-t: {opt_t}")
    if opt_h == True:
        print(f"-h:")

if __name__ == "__main__":
    main()
