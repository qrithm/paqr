import logging
import subprocess

"""
Some helper methods for managing Docker containers underlying Paqs.

We may eventually rewrite this using the docker pypi project:
https://pypi.org/project/docker/
"""


def docker_build(image_name: str, paq_dir: str):
    args = ["docker", "build", "-t", image_name, paq_dir]
    logging.info("Building container {}".format(image_name))
    subprocess.run(args, check=True)


def docker_run(image_name: str, port: str = "8080:8080"):
    args = ["docker", "run", "-p", port, image_name]
    subprocess.run(args, check=True)


def docker_tag(image_name: str, tag: str = "latest") -> str:
    gcr_id = "gcr.io/qrithm/{}:{}".format(image_name, tag)
    args = ["docker", "tag", image_name, gcr_id]
    subprocess.run(args, check=True)
    return gcr_id


def docker_push(image_id: str):
    args = ["docker", "push", image_id]
    logging.info("Pushing container {}".format(image_id))
    subprocess.run(args, check=True)
