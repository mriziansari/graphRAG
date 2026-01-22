class InMemoryGraphStore:
    def __init__(self):
        self.final_nodes = {}   # node_id -> node
        self.final_edges = set()  # (src, relation, tgt)

    def add_graph(self, nodes: list, edges: list):
        # Add nodes
        for node in nodes:
            node_id = node["id"]
            if node_id not in self.final_nodes:
                self.final_nodes[node_id] = node

        # Add edges
        for edge in edges:
            key = (
                edge["source"],
                edge["relation"],
                edge["target"]
            )
            self.final_edges.add(key)


    def get_node(self, node_id: str):
        return self.final_nodes.get(node_id)

    def get_neighbors(self, node_id: str):
        neighbors = []
        for src, rel, tgt in self.final_edges:
            if src == node_id:
                neighbors.append((rel, tgt))
        return neighbors

    def find_seed_nodes(graph_store, query: str):
        query_lower = query.lower()
        seeds = []

        for node in graph_store.nodes.values():
            if node["name"].lower() in query_lower:
                seeds.append(node["id"])

        return seeds
