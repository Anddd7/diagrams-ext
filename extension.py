from diagrams import Cluster, Diagram, Node

from diagrams.aws.network import (
    NATGateway,
    InternetGateway,
    ElasticLoadBalancing,
)
from diagrams.aws.extension import (
    ClusterSecureSubnet,
    ClusterVPC,
    ClusterPrivateSubnet,
    ClusterPublicSubnet,
    ClusterIntraSubnet,
    ClusterRegion,
    ClusterCloud,
    ClusterAccount,
)
from diagrams.aws.database import RDSInstance
from diagrams.aws.compute import EKS

graph_attr = {"layout": "neato", "compound": "true", "splines": "spline"}
with Diagram("dist/demo", show=False, graph_attr=graph_attr) as diag:
    # input
    subnet_area = 3
    az_count = 3
    az_names = ["1a", "1b", "1c", "1d", "1e", "1f"]
    layer_count = 3
    layer_types = [ClusterPublicSubnet, ClusterPrivateSubnet, ClusterIntraSubnet]
    layer_names = ["public", "private", "intra"]

    # param
    spacer = 2.5  # 直径 1.9
    vpc_padding = 1
    az_padding = 0.4
    subnet_padding = 0.2
    vpc_width = subnet_area * az_count + spacer * (az_count - 1)
    vpc_height = subnet_area * layer_count + spacer * (layer_count - 1)

    # cluster cache, add nodes later
    subnets = [[{}] * layer_count for _ in range(az_count)]

    with ClusterVPC("vpc") as vpc:
        p_tl = Node("", shape="none", pin="true", pos=f"{-vpc_padding},{vpc_height+vpc_padding}")
        p_br = Node("", shape="none", pin="true", pos=f"{vpc_width+vpc_padding},{-vpc_padding}")

    for ia in range(az_count):
        x = (subnet_area + spacer) * ia
        y = 0
        for il, type in enumerate(layer_types):
            y = (subnet_area + spacer) * il
            name = f"sn-{layer_names[il]}-{az_names[ia]}"
            with type(name) as instance:
                p_tl = Node("", shape="none", pin="true", pos=f"{x},{y+subnet_area}")
                p_br = Node("", shape="none", pin="true", pos=f"{x+subnet_area},{y}")

                subnets[ia][il] = {"subnet": instance, "x": x + subnet_padding, "y": y + subnet_padding}

        with Cluster(
            f"az-{az_names[ia]}",
            graph_attr={
                "bgcolor": "transparent",
                "penwidth": "2.0",
                "style": "rounded,dashed",
            },
        ):
            p_tl = Node("", shape="none", pin="true", pos=f"{x-az_padding},{y+subnet_area+az_padding}")
            p_br = Node("", shape="none", pin="true", pos=f"{x+subnet_area+az_padding},{-az_padding}")

    with vpc:
        igw = InternetGateway(pin="true", pos=f"{vpc_width/2},{-3}")
    with subnets[1][0]["subnet"]:
        x, y = subnets[1][0]["x"], subnets[1][0]["y"]
        nat = NATGateway(pin="true", pos=f"{x},{y}")
        elb = ElasticLoadBalancing(pin="true", pos=f"{x+spacer},{y}")
    with subnets[1][1]["subnet"]:
        x, y = subnets[1][1]["x"], subnets[1][1]["y"]
        eks = EKS(pin="true", pos=f"{x},{y}")
    with subnets[1][2]["subnet"]:
        x, y = subnets[1][2]["x"], subnets[1][2]["y"]
        rds = RDSInstance(pin="true", pos=f"{x},{y}")

    igw >> elb >> eks >> rds
    eks >> nat >> igw
