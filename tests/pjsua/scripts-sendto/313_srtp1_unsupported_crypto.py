import inc_sip as sip
import inc_sdp as sdp

sdp = """
v=0
o=- 0 0 IN IP4 127.0.0.1
s=tester
c=IN IP4 127.0.0.1
t=0 0
m=audio 4000 RTP/AVP 0 101
a=rtpmap:0 PCMU/8000
a=sendrecv
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=crypto:1 CRYPTO_X inline:WnD7c1ksDGs+dIefCEo8omPg4uO8DYIinNGL5yxQ
"""

args = "--null-audio --auto-answer 200 --max-calls 1 --use-srtp 1 --srtp-secure 0"
include = []
exclude = ["a=crypto"]

sendto_cfg = sip.SendtoCfg(
    "caller has used unsupported crypto, callee (SRTP optional) accept the call without crypto",
    pjsua_args=args,
    sdp=sdp,
    resp_code=200,
    resp_inc=include,
    resp_exc=exclude,
)
