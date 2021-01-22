#! python

import click
import veras


@click.command()
@click.option("--protocol", "-c", default="bolt")
@click.option("--host", "-h", default="localhost")
@click.option("--port", "-p", default=7687)
@click.option("--username", "-u", default="neo4j")
@click.option("--password", "-i", default="neo4j")
def ping_database(protocol, host, port, username, password):
    route_db = veras.route_database.RouteDatabase(f"{protocol}://{host}:{port}", username, password)
    route_db.print_route("klax", "ksfo")
    route_db.close()


if __name__ == "__main__":
    ping_database()
