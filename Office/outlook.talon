os: windows
and app.name: Microsoft Outlook
os: windows
and app.exe: /^outlook\.exe$/i
-
menu {user.outlook_menu_heading}: user.invoke_by_value(outlook_menu_heading,"automation_id")
toggle ribbon: key(ctrl-f1)
refresh: user.outlook_refresh()
new email: user.outlook_new_email()
attach file: user.outlook_attach_file()
select attachment: user.outlook_select_attachment()
download attachment: user.outlook_download_attachment()
back to message: user.outlook_show_message()
go to message: user.outlook_go_to_message()
go to {user.outlook_main_panel}: user.outlook_go_to_main_panel(outlook_main_panel)

{user.outlook_shared_button}: user.outlook_click_button(outlook_shared_button)
send message: user.outlook_send_message()
search: key(f3)
close notifications: user.outlook_close_notifications()

# accounts and folders
open account {user.email_account}: user.outlook_open_account(email_account)
{user.email_account} {user.email_folder}: user.outlook_open_account(email_account,email_folder)