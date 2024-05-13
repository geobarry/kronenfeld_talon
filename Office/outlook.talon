os: windows
and app.name: Microsoft Outlook
os: windows
and app.exe: /^outlook\.exe$/i
-
refresh: user.outlook_refresh()
new email: user.outlook_new_email()
attach file: user.outlook_attach_file()
select attachment: user.outlook_select_attachment()
download attachment: user.outlook_download_attachment()
(show|back to) message: user.show_message()
reply$: user.outlook_invoke_by_automation_id("Reply")
reply all$: user.outlook_invoke_by_automation_id("ReplyAll")
forward$: user.outlook_invoke_by_automation_id("Forward")
send message: user.outlook_send_message()
search: key(f3)
close notifications: user.outlook_close_notifications()
