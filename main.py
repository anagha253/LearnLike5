from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def prompt_ans(concept):
    return (
        f"""You are a friendly educational agent named ExplainBot who helps children understand hard ideas.
            Your job is to think step-by-step like this:
            Step 1: 
            Thought: What sub-topics or knowledge do I need to explain this?
            Action: Simulate a search or recall for each part.
            Observation: Summarize what you found.
            ---
            Step 2:
            Thought: How do I simplify this for a 5-year-old?
            Action: Rephrase using simple language, analogies, and fun examples.
            ---
            Step 3:
            Final Answer: Give a full kid-friendly explanation.

            -----
            topic: {concept}
            """
            )

def simplify_for_kids(concept,prev_observation):
    return(
        f"""
        You are a playful explainer AI.
        Your job is to explain complex ideas like you're talking to a 5-year-old.
        Use fun, simple language, relatable analogies (like toys, food, or animals), and give one real-world example.
        Concept: {concept}
        Observations: {prev_observation}
        Now, give your final answer.
        """
    )

def generate_response(prompt):
    response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=prompt, 
    config = types.GenerateContentConfig(
        temperature=0.1
    )
    )
    return response.text



# if __name__ == '__main__':
#     load_dotenv()
#     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#     client =  genai.Client(api_key=GEMINI_API_KEY)
#     concept = input("Enter the concept you want to learn!")

    

#     prompt1 = prompt_ans(concept)

#     response1 = generate_response(client,prompt1)
#     print(f"okay i am thinking now to give you better ans...\n here are my thoughts: {response1} \n\n trying to simplify the data for you!\n")
#     print("******")
#     prompt2 = simplify_for_kids(concept,response1)
#     response = generate_response(client,prompt2)
#     print(response)
