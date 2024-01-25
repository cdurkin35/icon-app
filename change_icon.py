## Code that physically changes the icons

import os
import shutil
import subprocess
import sys


def replace_icon(app_name, icon_path):
    # Define path to Applications
    applications_path = "/Applications"

    # Define path to app's .app folder
    app_path = os.path.join(applications_path, f"{app_name}.app")

    # Verify app path exists
    if not os.path.exists(app_path):
        print(f"{app_name} does not exist in your Applications folder!")
        return
