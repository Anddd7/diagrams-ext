# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _Generic


class _Virtualization(_Generic):
    _type = "virtualization"
    _icon_dir = "resources/generic/virtualization"


class Qemu(_Virtualization):
    _icon = "qemu.png"


class Virtualbox(_Virtualization):
    _icon = "virtualbox.png"


class Vmware(_Virtualization):
    _icon = "vmware.png"


class XEN(_Virtualization):
    _icon = "xen.png"


# Aliases