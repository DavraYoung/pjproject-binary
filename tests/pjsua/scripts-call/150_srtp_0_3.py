#
from inc_cfg import *

test_param = TestParam(
    "Callee=no SRTP, caller=optional (with duplicated offer) SRTP",
    [
        InstanceParam(
            "callee", "--null-audio --use-srtp=0 --srtp-secure=0 --max-calls=1"
        ),
        InstanceParam(
            "caller", "--null-audio --use-srtp=3 --srtp-secure=0 --max-calls=1"
        ),
    ],
)
