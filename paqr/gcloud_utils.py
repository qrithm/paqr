import subprocess
import logging

"""
Utils to assist with deploying Paqs to gcloud

"""


def gcloud_deploy(container_id: str, config: dict, allow_unauthenticated: bool = True, region: str = "us-east1"):
    print("Deploying to gcloud with config", config)
    args = ["gcloud", "run", "deploy", config["name"], "--image",
            container_id, "--platform", "managed", "--memory", config['memory'], "--region", region, "--cpu", str(config['cpu'])]
    if "concurrency" in config.keys():
        args.append("--concurrency")
        args.append(config["concurrency"])
    if allow_unauthenticated:
        args.append("--allow-unauthenticated")
    logging.info("Deploying container {} to Cloud Run".format(container_id))
    subprocess.run(args, check=True)
