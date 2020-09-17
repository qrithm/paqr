from paqr.paq import validate_paq
from paqr.docker_utils import *
from paqr.gcloud_utils import *
import argparse
from paqr import qpr


def main(args):
    config = validate_paq(args.paq_dir)
    docker_build(config['name'], args.paq_dir)
    gcr_id = docker_tag(config['name'])
    docker_push(gcr_id)
    gcloud_deploy(gcr_id, config)
    qpr.publish(config)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'paq_dir', help="Path to the base of the paq. Directory must contain a paq.yml file")
    args = parser.parse_args()
    main(args)
