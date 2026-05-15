---
created: 2026-01-23
title: "Fix bug: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))"
area: bug
tier: 3
status: DONE
priority: P2
bd_legacy_id: ttydal-wkn
---

# Fix bug: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Description

Application throws ConnectionError with 'Connection reset by peer' error code 104. Need to investigate the cause and implement proper error handling or connection retry logic.
