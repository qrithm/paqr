# paqr

Helper library for packing ML apps to be published on Qrithm

## Installation

Add `git+https://github.com/qrithm/paqr@master` to the requirements.txt file of your paq.

In the future we may cut releases, but for now this is based off master.

Install your requirements file so that `paqr` can be run from the shell

## Usage

### Implement your predictor

Implement your Predictor as follow:

```
from paqr.predictor import PredictorInterface

Predictor(PredictorInterface):

    def predict(self,input):
    ... compute some output ...
    return output
```

### Implement your server

Implement a FastAPI server that serves predictions from your Predictor at specified API endpoints.

See https://github.com/qrithm/template/blob/master/server.py for an example

### Add config files

Add a `paq.yaml` file to your paq directory. You can copy the one in this directory and customize it to your needs

Add a Dockerfile to your paq directory. It should containerize your paq and run your server. See

https://github.com/qrithm/template/blob/master/Dockerfile for an example.

TODO: Remove Dockerfile requirement, and automatically add a standard Dockerfile if one has not been added

### (Optional) Run your paq

You can run your paq with `python -m paqr.run <path-to-your-paq>`. Specify your own port if needed with `--port <your-port>`

### Publish your paq

Publish your paq with `python -m paqr.publish <path-to-your-paq>`. If your name is not available you may need to select a new name.

If publishing is successful the host API URL should be printed out at the end of this process. You can check it out by visiting `<host-url>/docs`
