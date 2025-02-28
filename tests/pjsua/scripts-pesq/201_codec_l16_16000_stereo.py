#
from inc_cfg import *

# Call with L16/16000/2 codec
test_param = TestParam(
    "PESQ defaults pjsua settings",
    [
        InstanceParam(
            "UA1",
            "--stereo --max-calls=1 --clock-rate 16000 --add-codec L16/16000/2 --play-file wavs/input.2.16.wav --null-audio",
        ),
        InstanceParam(
            "UA2",
            "--stereo --max-calls=1 --clock-rate 16000 --add-codec L16/16000/2 --rec-file  wavs/tmp.2.16.wav   --auto-answer 200",
        ),
    ],
)

if HAS_SND_DEV == 0:
    test_param.skip = True

pesq_threshold = None
