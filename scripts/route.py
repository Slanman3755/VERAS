import click
import veras


@click.command()
@click.argument("origin")
@click.argument("destination")
def route(origin, destination):
    """Print route between origin and destination airports.

    ORIGIN is the ICAO identifier of the origin airport
    DESTINATION is the ICAO identigier of the destination airport"""
    print(veras.router.find_route(origin, destination))


if __name__ == "__main__":
    route()
