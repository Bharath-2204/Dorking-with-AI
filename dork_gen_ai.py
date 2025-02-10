from gpt4all import GPT4All
import time

model = GPT4All("C:\\Users\\bhara\\gpt4all\\Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf")  # Load a local AI model

#Function to generate dorks using AI based on the keyword
def dorkgen_ai(keyword):

    prompt = f"""
    Generate exactly 10 unique Google Dorks to find information related to the name '{keyword}'. The dorks should focus on:

    1. Finding profiles, resumes, or personal information related to a person named {keyword}.
    2. Locating documents, PDFs, or articles where the name '{keyword}' appears.
    3. Searching for webpages with the name '{keyword}' in titles, URLs, or content.
    4. Identifying specific file types, such as PDFs or DOCs, that contain information about {keyword}.
    5. Avoid generating irrelevant or generic search results not related to this name.

    Each dork should be on a separate line, and all results should be clearly related to the name '{keyword}'.
    """

    response = model.generate(prompt, max_tokens=1000)
    dorks = response.strip().split("\n")
    filtered = [dork.split('-')[0] for dork in dorks if keyword in dork.lower()] 
    finaldork = [dork.split(' ',1)[1] for dork in filtered]

    #Saving the dorks to a text file
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"{keyword}_dorks_{timestamp}.txt"
    with open(output_file,"w") as f:
        for dork in finaldork:
            f.write(f"{dork}\n")

    return finaldork

