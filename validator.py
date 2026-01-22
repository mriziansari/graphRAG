import uuid 
from typing import Dict, List
from rich import print_json 
import json


class GraphValidator:
    def __init__(self):
        pass

    def _canonical_key(self, name: str) -> str:
        """Normalize entity names deterministically"""
        return name.strip().lower()
    
    def validate_and_canonicalize(self, graph: Dict) -> Dict:
        entities = graph.get("entities", [])
        relationships = graph.get("relationships", [])

        # ----------------------------
        # STEP 1: Validate entities
        # ----------------------------

        raw_entity_map = {}
        for entity in entities:
            if not entity.get("name") or not entity.get("id"):
                continue
            raw_entity_map[entity["id"]] = entity

        if not raw_entity_map:
            return {"nodes": [], "edges": []}
        
        # ----------------------------
        # STEP 2: Canonicalize entities
        # ----------------------------

        canonical_map = {}
        raw_to_canonical = {}

        for raw_id, entity in raw_entity_map.items():
            key = f"{entity.get('type','unknown')}::{self._canonical_key(entity['name'])}"
            if key not in canonical_map:
                canonical_id = f"node_{uuid.uuid4().hex[:8]}"
                canonical_map[key] = {
                    "id": canonical_id,
                    "name": entity["name"],
                    "type": entity.get("type", "unknown")
                }
            raw_to_canonical[raw_id] = canonical_map[key]["id"]
            
        nodes = list(canonical_map.values())
        
        
        # ----------------------------
        # STEP 3: Validate + rewrite relationships
        # ----------------------------
        edges = []

        for r in relationships:
            src = r.get("source")
            tgt = r.get("target")
            rel = r.get("relation")

            if not src or not tgt or not rel:
                continue

            if src not in raw_to_canonical:
                continue
            if tgt not in raw_to_canonical:
                continue

            src_canonical = raw_to_canonical[src]
            tgt_canonical = raw_to_canonical[tgt]

            edges.append({
                "source": src_canonical,
                "relation": rel.strip().upper().replace(" ", "_"),
                "target": tgt_canonical
            })
        # print_json(data = nodes)
        # print("\n\n<<<<<<<<Edges>>>>>>>>:\n")
        # print_json(data = edges)
        return {
            "nodes": nodes,
            "edges": edges
        }