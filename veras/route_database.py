from neo4j import GraphDatabase

class RouteDatabase:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_route(self, origin, destination):
        with self.driver.session() as session:
            movie = session.write_transaction(self._return_route, origin, destination)
            print(movie)

    @staticmethod
    def _return_route(transaction, origin, destination):
        result = transaction.run("match (origin:airport)-[r:route]->(destination:airport) "
                                 "where origin.id = toupper($origin) and destination.id = toupper($destination) "
                                 "return r.route", origin=origin, destination=destination)
        return result.single()[0]
