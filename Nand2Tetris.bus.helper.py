def main():
# Program to write parts of Chip Or(16) bus in Nand2Tetris hardware simulator
# of pattern "Or(a=a[v],b=b[v],out=out[v]);"
    for k in range(0,16):
 #       print("Or(a=a[",k,"],b=b[",k,"],out=out[",k"]);");
        print("Or(a=a[{}],b=b[{}],out=out[{}]);".format(k, k, k))
#Obviously, this can be varied to produce busses for other chips
if __name__ == "__main__":
    main()def main():
