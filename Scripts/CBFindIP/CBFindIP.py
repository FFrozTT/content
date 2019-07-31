import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *
from typing import List
res = []  # type: List[str]
t = []  # type: List[str]
found = []
ips = argToList(demisto.args()['ip'])
for ip in ips:
    for e in demisto.executeCommand('cb-get-processes', {'query': 'ipaddr:' + ip}):
        if isError(e):
            res += e
        else:
            found.append(ip)
            t += e['HumanReadable']
if t:
    appendContext("found_ips", ','.join(found), dedup=True)
    demisto.results({'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': e['HumanReadable'],
                     'EntryContext': e['EntryContext']})
else:
    demisto.results({'ContentsFormat': formats['text'], 'Type': entryTypes['note'], 'Contents': 'No results.'})
demisto.results(res)
