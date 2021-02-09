
from diagrams import Diagram, Cluster
from diagrams.gcp.network import DNS
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import SQL
from diagrams.gcp.database import Memorystore

with Diagram("Simple Website Diagram") as diag:
    dns = DNS("dns")
    load_balancer = LoadBalancing("Load Balances")
    database = SQL("User Database")
    cache = Memorystore("Cache")
    with Cluster("Webservers"):
      svc_group = [ComputeEngine("Webserver 1"),
                  ComputeEngine("Webserver 2"),
                  ComputeEngine("Webserver 3")]
    dns >> load_balancer >> svc_group
    svc_group >> cache
    svc_group >> database
diag