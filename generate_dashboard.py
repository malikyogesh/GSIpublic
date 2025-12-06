from google import genai
from google.genai import types

# 1. Initialize the client
# The client will automatically pick up your API key from the 
# GOOGLE_API_KEY environment variable.
client = genai.Client()

# 2. Define the Google Search tool configuration
# The simple presence of the Tool with GoogleSearch() enables grounding.
grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

# 3. Define the content generation configuration
config = types.GenerateContentConfig(
    # Pass the configured tool in a list to the 'tools' parameter
    tools=[grounding_tool]
)

# 4. Make the generate_content call
# The model will decide if a search is necessary for the prompt.
prompt = "Latest news about Equinix?" 
# This is a real-time question that requires grounding.

response = client.models.generate_content(
    model="gemini-2.5-flash",  # Or your preferred model
    contents=prompt,
    config=config,
)

# 5. Print the response and check for grounding metadata
print(f"Model Response: {response.text}\n")

if response.candidates and response.candidates[0].grounding_metadata:
    print("--- Grounding Metadata ---")
    print(f"Search Queries Used: {response.candidates[0].grounding_metadata.web_search_queries}")
    # You can also parse 'grounding_chunks' to display citations
else:
    print("No grounding metadata found (model did not use search).")
