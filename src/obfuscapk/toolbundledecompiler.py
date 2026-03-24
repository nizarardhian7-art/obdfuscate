import logging
import os
import platform
import shutil

class BundleDecompiler(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        if platform.system() == "Windows":
            return
        path = os.environ.get("BUNDLE_DECOMPILER_PATH", "BundleDecompiler.jar")
        full_path = shutil.which(path)
        if full_path is None:
            self.logger.warning("BundleDecompiler not found, skipping")
            return

class AABSigner(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
