import sys
from . import run

def main():
    if len(sys.argv) < 2:
        print("Usage: groovy <command>")
        sys.exit(1)
    
    command = " ".join(sys.argv[1:])
    result = run(command)
    print(result)

if __name__ == "__main__":
    main() 