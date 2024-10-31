from dataclasses import dataclass

ENDPOINT_ROOT:str="http://localhost:{port}/predict"      # Remember that all services have the same interface

@dataclass
class Services: 
    detect:str=ENDPOINT_ROOT.format(port=8080)
    blur:str=ENDPOINT_ROOT.format(port=7070)
    crop:str=ENDPOINT_ROOT.format(port=6060)