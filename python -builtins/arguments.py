import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')

parser.add_argument("--a", default=1, type=int, help="This is the 'a' variable")
parser.add_argument("--name", required=True, type=str, help="Your name")

args = parser.parse_args()
a = args.a
name = args.name
print(str(a) + " " + name)