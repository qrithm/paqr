from paqr.paq import validate_paq
from paqr.docker_utils import *
import argparse


"""
Builds and runs the paq container on the specified port
"""


def main(args):
    config = validate_paq(args.paq_dir)
    if not args.skip_build:
        docker_build(config['name'], args.paq_dir)
    docker_run(config['name'], port=args.port)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'paq_dir', help="Path to the base of the paq. Directory must contain a paq.yml file")
    parser.add_argument(
        '--port', help="Port to run the container on", default="8080:8080")
    parser.add_argument(
        '--skip_build', help="""Will skip the docker build step and just try and run the container. 
        This will fail if the container has not been built before or if it is already running on the same port""", action='store_true')
    args = parser.parse_args()
    main(args)
