import veras.route_database

routes = {
    "KLAX": {
        "KSFO": "SUMMR2 STOKD SERFR SERFR4",
    },
}

def find_route(origin, destination):
    return routes[origin.upper()][destination.upper()]

def run():
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "password")
    greeter.print_greeting("hello, world")
    greeter.close()


if __name__ == "__main__":
    main()