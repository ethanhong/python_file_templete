import sys
from project_name import app

def main(args = None):
    if args is None:
        args = sys.argv[1:]
    
    # do arguments parsing here (eg. with argparse)

    return app.run()

if __name__ == '__main__':
    sys.exit(main())
    