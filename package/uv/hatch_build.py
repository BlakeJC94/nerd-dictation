from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import os
import shutil


class CustomBuildHook(BuildHookInterface):
    PLUGIN_NAME = "sync_source"

    def initialize(self, version, build_data):
        src = os.path.normpath(os.path.join(self.root, "..", "..", "nerd-dictation"))
        dst_dir = os.path.join(self.root, "src", "nerd_dictation")
        dst = os.path.join(dst_dir, "__init__.py")

        if not os.path.exists(src):
            # AIDEV-NOTE: when building from sdist, the file is already in place
            # because sdist force-include maps it to the project root
            alt = os.path.join(self.root, "nerd-dictation")
            if os.path.exists(alt):
                src = alt

        if os.path.exists(src):
            os.makedirs(dst_dir, exist_ok=True)
            shutil.copy2(src, dst)