import re

STATUS_FAIL = "FAIL"
STATUS_ERROR = "ERROR"
STATUS_ABORTED = "ABORTED"
STATUS_REGRESSION = "REGRESSION"
STATUS_SUCCESS = "SUCCESS"

STATUS_FIXED = "FIXED"
STATUS_PASSED = "PASSED"

RESULTSTATUS_FAILURE = "FAILURE"
RESULTSTATUS_FAILED = "FAILED"
RESULTSTATUS_SKIPPED = "SKIPPED"

STR_RE_SPLIT_VIEW = "(.*)/view/([^/]*)/?"
RE_SPLIT_VIEW_URL = re.compile(STR_RE_SPLIT_VIEW)
