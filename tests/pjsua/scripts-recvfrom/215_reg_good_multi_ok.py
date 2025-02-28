import inc_sip as sip
import inc_sdp as sdp

pjsua = (
    "--null-audio --id=sip:CLIENT --registrar sip:127.0.0.1:$PORT "
    + "--username theuser1 --realm python1 --password passwd --next-cred "
    + "--username theuser2 --realm python2 --password passwd "
    + "--auto-update-nat=0"
)

req1 = sip.RecvfromTransaction(
    "Initial registration",
    401,
    include=["REGISTER sip"],
    resp_hdr=[
        'WWW-Authenticate: Digest realm="python1", nonce="1234"',
        'WWW-Authenticate: Digest realm="python2", nonce="6789"',
    ],
    expect="SIP/2.0 401",
)

req2 = sip.RecvfromTransaction(
    "Registration retry with auth (not allowed multiple auth)",
    200,
    include=[
        "REGISTER sip",
        "Authorization:",  # [\\s\\S]+Authorization:"
        'realm="python1"',  # "realm=\"python2\"",
        'username="theuser1"',  # "username=\"theuser2\"",
        'nonce="1234"',  # "nonce=\"6789\"",
        "response=",
    ],
    expect="registration success",
    pj_config="PJSIP_AUTH_ALLOW_MULTIPLE_AUTH_HEADER.*: 0",
)

req3 = sip.RecvfromTransaction(
    "Registration retry with auth (allowed multiple auth)",
    200,
    include=[
        "REGISTER sip",
        "Authorization:[\\s\\S]+Authorization:",  # Must have 2 Auth hdrs
        'realm="python1"',
        'realm="python2"',
        'username="theuser1"',
        'username="theuser2"',
        'nonce="1234"',
        'nonce="6789"',
        "response=",
    ],
    expect="registration success",
    pj_config="PJSIP_AUTH_ALLOW_MULTIPLE_AUTH_HEADER.*: 1",
)

recvfrom_cfg = sip.RecvfromCfg(
    "Multiple authentication challenges",
    pjsua,
    [req1, req2, req3],
    pj_config="PJSIP_AUTH_ALLOW_MULTIPLE_AUTH_HEADER",
)
