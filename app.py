import os
import sys
from time import sleep
from langchain_openai import ChatOpenAI
from langchain import PromptTemplate, LLMChain
import gradio as gr


os.environ["OPENAI_API_KEY"] = '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' # Replace YOUR_API_KEY with your actual API key

llm = ChatOpenAI(model_name="gpt-4")


template = """Translate the following English text to French:
{english_text}"""
prompt = PromptTemplate(
    input_variables=["english_text"],
    template=template,
)

chain = LLMChain(llm=llm, prompt=prompt)



"""
english_text = "Now, when you run this code, it will display the French translation one character at a time, creating a rolling print effect. You can customize the rolling speed by changing the delay in sleep()."
french_text = chain.run(english_text)




# 6. Rolling print the translated text
def rolling_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)  # Adjust delay for desired speed
    print()  # Add a newline at the end
    sleep(0.25)
rolling_print(french_text)  """


def translate_text(english_text):
    french_text = chain.run(english_text)
    return french_text


iface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(lines=2, placeholder="Enter English text here..."),
    outputs="text",
    title="English to French Translator",
    description="Translate English text to French using LangChain and GPT-4.",
)



iface.launch()



