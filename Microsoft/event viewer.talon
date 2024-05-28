os: windows
and app.name: Microsoft Management Console
os: windows
and app.exe: /^mmc\.exe$/i
-
filter current log: user.ev_filter_current_log()
next bug check: user.ev_next_bug_check()