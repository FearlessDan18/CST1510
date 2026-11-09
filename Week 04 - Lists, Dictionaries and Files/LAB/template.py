"""
RECORD CHECK  -  AI / Data Science lane  (Excellent version)
============================================================

Name  :
Lane  :  AI / Data Science
Date  :

Run it:   python template.py

Loads every dataset record from datasets.txt (label,value,limit - one record
per line), checks each one against its limit, prints a bordered report, then
writes label,status lines to check_results.txt and prints how many records
were over limit.

Excellent pieces:
  - records loaded from your own data file (Typical)
  - results written out to a new file
  - running count of OVER LIMIT, printed once after the loop
  - the load is wrapped in try/except - a missing file starts empty, no crash
"""

# =================================================================== FUNCTIONS
# 1. check_record and print_report come back from Week 3 - one job each.


def check_record(value, limit):
    """Return the difference, percentage and status for one record."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered report - nothing is worked out in here."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records


def write_results(path, results):
    """Write one label,status line per result to a file."""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")


# ====================================================================== STORE
# 2. Records come from a file, one label,value,limit line per record.
#    A missing file is caught here - clear message, empty list, no crash.

DATA_FILE = "datasets.txt"
RESULTS_FILE = "check_results.txt"

try:
    records = load_records(DATA_FILE)
except FileNotFoundError:
    print(f"{DATA_FILE} not found - starting with an empty list.")
    records = []


# =============================================================== PROCESS + OUTPUT
# 3. Check and report on every record, keep a running OVER LIMIT count,
#    then write the results out and print the summary once.

over_limit_count = 0
results = []

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)

    results.append((record["label"], status))
    if status == "OVER LIMIT":
        over_limit_count += 1

write_results(RESULTS_FILE, results)

print(f"Checked {len(records)} records. {over_limit_count} were over limit.")
print(f"Results written to {RESULTS_FILE}.")


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers are correct by hand
#    [x] Ran it with a missing file - the try/except caught it and started
#        with an empty list instead of crashing (FileNotFoundError)
#    [x] Every function does one job - status logic lives only in
#        check_record, loading only in load_records, printing only in
#        print_report, file writing only in write_results