## Code that physically changes the icons

import os
import shutil
import subprocess
import sys


def replace_icon(app_name, icon_path):
    # Define path to Applications
    applications_path = "/Applications"

    # Define path to app's Resources folder
    app_resources_path = f"{applications_path}/{app_name}.app/Contents/Resources"

    # Find the icns file in the Resources folder
    icon_file = None
    for file in os.listdir(app_resources_path):
        if file.endswith(".icns"):
            icon_file = file
            break

    if icon_file is None:
        print("Icon File not found")
        return
    # Backup the original icon
    original_icon_path = os.path.join(app_resources_path, icon_file)
    backup_icon_path = os.path.join(app_resources_path, f"backup_{icon_file}")
    shutil.copy2(original_icon_path, backup_icon_path)
    print(f"Backup of the original icon is saved as {backup_icon_path}")

    # Replace the icon
    shutil.copy2(icon_path, original_icon_path)
    print(f"Icon for {app_name} has been changed.")

    # Refresh Finder and Dock
    subprocess.run(["sudo", "killall", "Dock"])
    subprocess.run(["sudo", "killall", "Finder"])
    print("Finder and Dock have been refreshed to apply the new icon.")
