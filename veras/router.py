import veras.route_database

routes = {
    "KLAX": {
        "KSFO": "SUMMR2 STOKD SERFR SERFR4",
    },
}

def find_route(origin, destination):
    return routes[origin.upper()][destination.upper()]
