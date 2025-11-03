import sys

def add(a, b): return a - b

def run():
    if len(sys.argv) >= 3:
        a, b = int(sys.argv[1]), int(sys.argv[2])
    else:
        a, b = 10, 20
    print(f"RESULT_SUM={add(a,b)}")
    print(f"DIFF={sub(a,b)}")

if __name__ == "__main__":
    run()