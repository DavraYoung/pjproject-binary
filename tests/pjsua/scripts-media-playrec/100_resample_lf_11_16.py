#
from inc_cfg import *

# simple test
test_param = TestParam(
    "Resample (large filter) 11 KHZ to 16 KHZ",
    [
        InstanceParam(
            "endpt",
            "--null-audio --quality 10 --clock-rate 16000 --play-file wavs/input.11.wav --rec-file wavs/tmp.16.wav",
        )
    ],
)
