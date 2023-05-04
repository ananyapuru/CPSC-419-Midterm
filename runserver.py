''' Importing the following modules in order for the code to work '''
from sys import exit, stderr
import argparse
from midterm import app

#-----------------------------------------------------------------------

def main(port):
    ''' Main Function '''
    try:
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(allow_abbrev=False,
                                     description='An object slideshow application.')
    parser.add_argument('p', metavar='port', type=int,
                    help='the port at which the server should listen')

    args = parser.parse_args()
    port = args.p if args.p else ""

    main(port)
