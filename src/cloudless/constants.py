import os

def determine_output_ending():
    """
    We add a unique ending to our output files so they can stack over time,
    such as output0001.log. This method determines an appropriate, unused
    ending, incrementing through those that are already present.
    """
    file_found = False
    idx = 1
    while not file_found:
        if not os.path.isfile(LOG_DIR + "/output%04d.png" % (idx)):
          return "%04d" % (idx)
        idx += 1

ROOT_DIR = "."
LOG_DIR = ROOT_DIR + "/logs"

# The number to append to output files, such as output0001.log.
OUTPUT_ENDING = determine_output_ending()

OUTPUT_LOG_PREFIX = LOG_DIR + "/output" + OUTPUT_ENDING

# Where to write out log files that aide in understanding how training went.
OUTPUT_LOG_PATH = OUTPUT_LOG_PREFIX + ".log"

# Where to write out training and validation result graphs.
OUTPUT_GRAPH_PATH = OUTPUT_LOG_PREFIX + ".png"

CAFFE_HOME = os.environ.get("CAFFE_HOME")

MODEL_ROOT = ROOT_DIR + "/src/caffe_model/bvlc_alexnet"
SOLVER_FILE = MODEL_ROOT + "/solver.prototxt"
# TODO(neuberg): Differentiate between the stock vanilla Caffe model zoo AlexNet and
# the one we've fine tuned via training and our data.
TRAINED_WEIGHTS = MODEL_ROOT + "/bvlc_alexnet.caffemodel"

TRAINING_FILE = ROOT_DIR + "/data/leveldb/train_leveldb"
VALIDATION_FILE = ROOT_DIR + "/data/leveldb/validation_leveldb"

# Path to ImageNet's mean file, which AlexNet is trained on and which must be used as a mask.
TRAINING_MEAN_FILE = ROOT_DIR + "/data/imagenet/imagenet_mean.binaryproto"

WIDTH = 256
HEIGHT = 256

LANDSAT_ROOT = ROOT_DIR + "/data/landsat"
LANDSAT_IMAGES = LANDSAT_ROOT + "/images"
LANDSAT_METADATA = LANDSAT_ROOT + "/metadata/training-validation-set.csv"

# Architecture string that will appear on graphs; good for relatively stable
# hyperparameter tuning.
ARCHITECTURE = "AlexNet fine tune; Landsat data"
