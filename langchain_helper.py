from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()



def generate_restaurant_name_and_titles(cuisine):
    llm = GoogleGenerativeAI(model="gemini-1.5-pro")

    # First chain: Suggest a restaurant name
    template1 = """I want to open a restaurant for {cusine} food. Suggest 1 fancy name for it."""
    prompt1 = PromptTemplate.from_template(template1)
    name_chain = LLMChain(prompt=prompt1, llm=llm, output_key="restaurant_name")

    # Second chain: Suggest menu items for the restaurant
    template2 = """Suggest some menu items for {restaurant_name}. Return it as a comma-separated list."""
    prompt2 = PromptTemplate.from_template(template2)
    items_chain = LLMChain(prompt=prompt2, llm=llm, output_key="menu_items")

    # Combine the chains into a SequentialChain
    chains = SequentialChain(
        chains=[name_chain, items_chain],
        input_variables=["cusine"],
        output_variables=["restaurant_name", "menu_items"],
    )

    # Invoke the chain
    response = chains.invoke({"cusine": cuisine})

    return response

if __name__=="__main__":
    print(f'respoonse is : {generate_restaurant_name_and_titles('Indian')}')
