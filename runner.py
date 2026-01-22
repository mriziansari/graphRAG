from google.genai import Client
from dotenv import load_dotenv
import os
import json
from rich import print_json
from entity_extractor import EntityExtractor
from validator import GraphValidator
from in_memory_graph_store import InMemoryGraphStore
from graph_retrieval import GraphRetrieval
from test_data import CLEANED_GRAPH_DATA

load_dotenv()

if __name__ == "__main__":

    gclient = Client(api_key=os.getenv("GOOGLE_API_KEY"))
    entity_extractor = EntityExtractor(gclient, "gemini-2.5-flash-lite")

    text = """
Inception is a science fiction movie released in 2010. It was directed by Christopher Nolan and stars Leonardo DiCaprio, Joseph Gordon-Levitt, and Elliot Page.
The movie belongs to the Science Fiction and Thriller genres.
Christopher Nolan also directed Interstellar, which starred Matthew McConaughey and Anne Hathaway.
Leonardo DiCaprio previously worked with Christopher Nolan in The Dark Knight Rises.
"""

    graph_data = entity_extractor.extract_entities(text)
    
    validator = GraphValidator()
    clean_data = validator.validate_and_canonicalize(graph_data)
    # clean_data = CLEANED_GRAPH_DATA
    graph_store = InMemoryGraphStore()
    graph_store.add_graph(clean_data["nodes"], clean_data["edges"])
    graph_retrieval = GraphRetrieval(graph_store)
    seeds = graph_retrieval.find_seed_nodes("Movies directed by Christopher Nolan")
    nodes, edges = graph_retrieval.traverse_graph(seeds)
    context = graph_retrieval.graph_to_text(nodes, edges)
    print("\n\n<<<<<<<<Context>>>>>>>>:\n")
    print(context)
    answer = entity_extractor.extract_answer(context, "Movies directed by Christopher Nolan")
    print("\n\n<<<<<<<<Answer>>>>>>>>:\n")
    print(answer)
    
    


    
