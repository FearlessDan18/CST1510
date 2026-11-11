"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """Parse a raw, messy server log line into a clean dictionary of values."""
    cleaned_line = raw_line.strip().lower()
    hostname_part, rest = cleaned_line.split(",", 1)
    hostname = hostname_part.strip()
    
    data = {"hostname": hostname}
    for piece in rest.split(","):
        key, value = piece.split("=")
        data[key.strip()] = float(value.strip())
    return data

def status_of(record):
    """Determine the server status based on disk usage percentage."""
    used = record["used"]
    total = record["total"]
    percentage = (used / total) * 100
    
    if percentage > 90:
        return "OVER LIMIT"
    elif percentage > 75:
        return "WARNING"
    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [
    "   Srv-01 , used=87 , total=100   ",
    "SRV-02,USED=45,TOTAL=100",
    "  srv-03  ,  used=95  ,  total=100  ",
    "srv-04,used=60,total=200",
    "   SRV-05 , used=92 , total=100 "
]


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for raw_record in raw_records:
   total_records = len(raw_records)
   flagged_count = 0

for raw_record in raw_records:
    parsed = parse_line(raw_record)
    status = status_of(parsed)
    
    if status in ("OVER LIMIT", "WARNING"):
        flagged_count += 1
        
    print(f"Record: {parsed} | Status: {status}")

print(f"\nSummary: {total_records} records processed, {flagged_count} flagged.")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
