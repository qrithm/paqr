# paqr

Helper library for packing ML apps to be published on Qrithm

## Installation

Add `git+https://github.com/qrithm/paqr@master` to the requirements.txt file of your paq.

In the future we may cut releases, but for now this is based off master.

## Usage

Implement your Predictor as follow:

```
from paqr.predictor import PredictorInterface

Predictor(PredictorInterface):

    def predict(self,input):
    ... compute some output ...
    return output
```

The paqr package includes a base set of requirements such as fastapi and uvicorn that are common to all apps, so you only need to include the requirements specific to your app in the requirements.txt file.
