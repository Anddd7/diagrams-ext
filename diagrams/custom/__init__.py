"""
Custom provides the possibility of load an image to be presented as a node.
"""

from diagrams import Node, loadicon


class Custom(Node):
    _provider = "custom"
    _type = "custom"
    _icon_dir = None

    fontcolor = "#ffffff"

    def _load_icon(self):
        return loadicon(self._icon)

    def __init__(self, label, icon_path, *args, **kwargs):
        self._icon = icon_path
        super().__init__(label, *args, **kwargs)
