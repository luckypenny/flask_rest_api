"""
This script simulates a model that predicts a person's age from a URL to a photo.

To run pass an URL to a photo as a command line argument.
The predicted age will be printed to stdout.

Example:

    $ python model.py https://upload.wikimedia.org/wikipedia/commons/c/c0/Douglas_adams_portrait_cropped.jpg
    42
"""
import random
import sys
import time


def predict_age(input_url):
    # NOTE: real model will be here in the future...
    time.sleep(random.randint(0, 3))  # simulate computation taking some time
    return random.randint(0, 100)


if __name__ == "__main__":
    input_url = sys.argv[1]
    age = predict_age(input_url)
    print(age)