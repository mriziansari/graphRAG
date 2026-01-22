from markdown_it.common.entities import entities
import uuid 
from typing import Dict, List
from rich import print_json 
import json

class GraphValidator:
    def __init__(self):
        self.graph =  {
  "entities": [
    {
      "id": "e1",
      "name": "Inception",
      "type": "Movies"
    },
    {
      "id": "e2",
      "name": "science fiction",
      "type": "Genre"
    },
    {
      "id": "e3",
      "name": "2010",
      "type": "Release Year"
    },
    {
      "id": "e4",
      "name": "Christopher Nolan",
      "type": "Person"
    },
    {
      "id": "e5",
      "name": "Leonardo DiCaprio",
      "type": "Person"
    },
    {
      "id": "e6",
      "name": "Joseph Gordon-Levitt",
      "type": "Person"
    },
    {
      "id": "e7",
      "name": "Elliot Page",
      "type": "Person"
    },
    {
      "id": "e8",
      "name": "Thriller",
      "type": "Genre"
    },
    {
      "id": "e9",
      "name": "Interstellar",
      "type": "Movies"
    },
    {
      "id": "e10",
      "name": "Matthew McConaughey",
      "type": "Person"
    },
    {
      "id": "e11",
      "name": "Anne Hathaway",
      "type": "Person"
    },
    {
      "id": "e12",
      "name": "The Dark Knight Rises",
      "type": "Movies"
    }
  ],
  "relationships": [
    {
      "source": "e1",
      "relation": "has genre",
      "target": "e2"
    },
    {
      "source": "e1",
      "relation": "has release year",
      "target": "e3"
    },
    {
      "source": "e4",
      "relation": "directed",
      "target": "e1"
    },
    {
      "source": "e1",
      "relation": "stars",
      "target": "e5"
    },
    {
      "source": "e1",
      "relation": "stars",
      "target": "e6"
    },
    {
      "source": "e1",
      "relation": "stars",
      "target": "e7"
    },
    {
      "source": "e1",
      "relation": "has genre",
      "target": "e8"
    },
    {
      "source": "e4",
      "relation": "directed",
      "target": "e9"
    },
    {
      "source": "e9",
      "relation": "stars",
      "target": "e10"
    },
    {
      "source": "e9",
      "relation": "stars",
      "target": "e11"
    },
    {
      "source": "e5",
      "relation": "worked with",
      "target": "e4"
    },
    {
      "source": "e12",
      "relation": "starred in",
      "target": "e5"
    },
    {
      "source": "e12",
      "relation": "directed by",
      "target": "e4"
    }
  ]
}

    def _canonical_key(self, name: str) -> str:
        """Normalize entity names deterministically"""
        return name.strip().lower()

    def validate_and_canonicalize(self) -> Dict:
        entities = self.graph.get("entities", [])
        relationships = self.graph.get("relationships", [])

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
                "relation": rel.strip().lower(),
                "target": tgt_canonical
            })
        print_json(data = nodes)
        print("\n\n<<<<<<<<Edges>>>>>>>>:\n")
        print_json(data = edges)
        return {
            "nodes": nodes,
            "edges": edges
        }

        



if __name__ == "__main__":
    validation = GraphValidator()
    validation.validate_and_canonicalize()