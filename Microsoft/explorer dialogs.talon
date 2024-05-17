os: windows
and app.name: Microsoft Outlook
and win.title: Insert File
-
go <user.system_path>: user.explorer_navigate_to_folder(system_path)
panel files: user.file_explorer_tab_to_files()