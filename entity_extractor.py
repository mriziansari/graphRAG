import json
from google.genai.types import GenerateContentConfig

class EntityExtractor:
    """Extracts entities from the provided text."""

    def __init__(self, llm_client, model_name):
        self.client = llm_client
        self.model = model_name
    
    def extract_entities(self, text) -> dict:
        """Extract entities from the provided text."""

        SYSTEM_PROMPT = """You are an information extraction engine.

TASK:
Extract entities and relationships from the provided text.

ENTITY TYPES: only these types are allowed
Movie, Person, Genre, Release_Year

RULES:
- Only extract what is explicitly stated
- Do NOT infer or hallucinate
- Reuse the same entity id consistently
- Use concise relation names

OUTPUT FORMAT (STRICT JSON):
{
  "entities": [
    { "id": "e1", "name": "...", "type": "..." }
  ],
  "relationships": [
    { "source": "e1", "relation": "...", "target": "e2" }
  ]
}"""

        USER_PROMPT = f"""
Text:
{text}
"""
        config = GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            temperature=0.0,
        )
        try:
            response = self.client.models.generate_content(
                model=self.model,
                config=config,
                contents=USER_PROMPT,
            )
            # Parse the JSON response
            try:
                parsed_response = json.loads(response.text)
                return parsed_response

            except json.JSONDecodeError:

                print("Failed to parse JSON response. Raw text:", response.text)
                return {"entities": [], "relationships": []}

        except Exception as e:
            print("Exception:", e)
            return {"entities": [], "relationships": []}    

    def extract_answer(self, cotent, query):
        prompt = f"""
        Answer the following query using only the provided content. Give a proper answer in a good sentences. 
        Cotent: {cotent}
        Query: {query}
        """
        config = GenerateContentConfig(
            response_mime_type="text/plain",
            temperature=0.0,
        )
        try:
            response = self.client.models.generate_content(
                model=self.model,
                config=config,
                contents=prompt,
            )
           
            try:
               return response.text

            except Exception as e:
                print("Exception:", e)
                return ""

        except Exception as e:
            print("Exception:", e)
            return ""    