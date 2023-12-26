# 등차수열 첫째항:1 공차: 2 an=1+(n-1)*2=2n-1
def print_tree(size):
    for i in range(1, size):
        print(" " * (size - i), end="") 
        print("*" * (i * 2 - 1)) 

    print(" " * (size-1) + "|")


def main():
    size = int(input("size : "))
    print_tree(size)

if __name__ == "__main__":
    main()