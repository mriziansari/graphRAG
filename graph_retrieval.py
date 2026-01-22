from rich import print_json
class GraphRetrieval:
    def __init__(self, graph_store):
        self.graph_store = graph_store
    
    def find_seed_nodes(self, query: str):
        query_lower = query.lower()
        seeds = []

        for node in self.graph_store.final_nodes.values():
            if node["name"].lower() in query_lower:
                seeds.append(node["id"])

        return seeds

    def traverse_graph(self,seed_ids, max_depth=2):
        frontier = [(seed_id, 0) for seed_id in seed_ids]
        visited = set(seed_ids)
        subgraph_nodes = {}
        subgraph_edges = []

        while frontier:
            current_node_id, current_depth = frontier.pop(0)
            
            if current_depth > max_depth:
                continue
            
            node = self.graph_store.get_node(current_node_id)
            if node and node["id"] not in subgraph_nodes:
                subgraph_nodes[node["id"]] = node

            neighbors = self.graph_store.get_neighbors(current_node_id)
            for rel, neighbor_id in neighbors:
                edge = (current_node_id, rel, neighbor_id)
                if edge not in subgraph_edges:
                    subgraph_edges.append(edge)
                
                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    frontier.append((neighbor_id, current_depth + 1))
        
        return list(subgraph_nodes.values()), subgraph_edges

    def graph_to_text(self, nodes, edges):
        text = []
        nodes_map = {node["id"]: node for node in nodes}
        for src, rel, trg in edges:
            src_name = nodes_map[src]["name"]
            trg_name = nodes_map[trg]["name"]
            if src_name and trg_name:
                sentence = f"{src_name} {rel.lower().replace('_', ' ')} {trg_name}"
                text.append(sentence)
        return "\n".join(text)
            
        