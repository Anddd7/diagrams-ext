from diagrams import Cluster
from diagrams.aws.general import _General
from diagrams.aws.network import _Network, VPC, PrivateSubnet, PublicSubnet

# Node


class SecureSubnet(_Network):
    _icon = "secure-subnet.png"


class IntraSubnet(_Network):
    _icon = "intra-subnet.png"


class Cloud(_General):
    _icon = "aws-cloud.png"


class Account(_General):
    _icon = "aws-account.png"


class Region(_General):
    _icon = "region.png"


# Cluster


class ClusterVPC(Cluster):
    _icon_node = VPC
    _graph_attr = {
        "bgcolor": "white",
        "pencolor": "#8C4FFF",
    }

    def __init__(
        self,
        label: str = "vpc",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterPublicSubnet(Cluster):
    _icon_node = PublicSubnet
    _graph_attr = {
        "bgcolor": "#F2F6E8",
        "pencolor": "#7AA116",
    }

    def __init__(
        self,
        label: str = "public",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterPrivateSubnet(Cluster):
    _icon_node = PrivateSubnet
    _graph_attr = {
        "bgcolor": "#E6F6F7",
        "pencolor": "#00A4A6",
    }

    def __init__(
        self,
        label: str = "private",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterSecureSubnet(Cluster):
    _icon_node = SecureSubnet
    _graph_attr = {
        "bgcolor": "#F8CECC",
        "pencolor": "#B85450",
    }

    def __init__(
        self,
        label: str = "secure",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterIntraSubnet(Cluster):
    _icon_node = IntraSubnet
    _graph_attr = {
        "bgcolor": "#FFE6CC",
        "pencolor": "#D79B00",
    }

    def __init__(
        self,
        label: str = "intra",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterCloud(Cluster):
    _icon_node = Cloud
    _graph_attr = {
        "bgcolor": "white",
        "pencolor": "#F78E04",
    }

    def __init__(
        self,
        label: str = "cloud",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterAccount(Cluster):
    _icon_node = Account
    _graph_attr = {
        "bgcolor": "white",
        "pencolor": "#CD2264",
    }

    def __init__(
        self,
        label: str = "account",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)


class ClusterRegion(Cluster):
    _icon_node = Region
    _graph_attr = {"bgcolor": "white", "pencolor": "#147EBA", "style": "rounded,dashed"}

    def __init__(
        self,
        label: str = "region",
        direction: str = "LR",
    ):
        super().__init__(label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr)
