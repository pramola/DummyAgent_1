from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


#story time
storyPrompt = PromptTemplate(
    template="Tell me a story about {mainCharacter} where villan was a {villianArc} within 10 lines no more than that. /no_think",
    input_variables=['mainCharacter', 'villianArc'])

# start the chat model
#very deterministic
chatModel = ChatOllama(
    model="qwen3.5:4b",
    temperature=0, 
    reasoning=False
)
#thinking mode is turned false as a lot of time is taken for now simple result is sufficient 


#dwarf story with Giants as villain
storyTime = storyPrompt.format(mainCharacter="dwarf", villianArc="giants")

#model ran but a lot of time to respond
# resp = chatModel.invoke(storyTime)
# print(resp.content)

for chunk in chatModel.stream(storyTime):
    print(chunk.content, end="", flush=True)
print()  # newline after stream ends   