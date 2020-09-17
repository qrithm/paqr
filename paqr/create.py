import os
import argparse
import subprocess
import yaml
import shutil


""" 
Creates a new paq from the starter-paq template and configures it with the user-supplied paq_name
"""


def create_paq(base_dir: str, paq_name: str):
    os.chdir(base_dir)
    args = ["git", "clone", "https://github.com/qrithm/starter-paq.git", paq_name]
    subprocess.run(args, check=True)
    paq_root = os.path.join(base_dir, paq_name)
    os.chdir(paq_root)
    os.remove("LICENSE")
    shutil.rmtree(".git")
    paq_path = "paq.yaml"
    f = open(paq_path, 'r')
    paq = yaml.load(f, Loader=yaml.FullLoader)
    paq['name'] = paq_name
    f = open(paq_path, 'w')
    yaml.dump(paq, f)
    print("Initialized paq {} in base directory {}".format(paq_name, base_dir))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'base_dir', help="Directory where you want to initialize your paq dir")
    parser.add_argument(
        'paq_name', help="Name to be used for your paq")
    args = parser.parse_args()
    create_paq(args.base_dir, args.paq_name)
