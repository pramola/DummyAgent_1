LCEL : Lang Chain Expression Language

It is a way to compose LangChain Runnables into pipelines.
It uses the | operator to connect components.
Example: prompt | model | parser.
The output of prompt becomes the input to model.
The output of model becomes the input to parser.
LCEL automatically creates a RunnableSequence for this pipeline.
You can also use RunnableParallel, RunnableBranch, RunnablePassthrough, etc.
The resulting chain supports standard methods like invoke(), batch(), and stream().
So LCEL is essentially a declarative way to build Runnable-based workflows.
Think: LCEL = syntax/framework for connecting Runnables together.

This pipe operator (traditionally called as OR operator) is used to take input provided from left side runnable and then pass it through to the right side operator
It is like a shorcut to RunnableSequence


An example of how it can be combined with the Branch
```
from langchain_core.runnables import RunnableBranch, RunnableLambda

# Two different processing chains
positive_chain = RunnableLambda(
    lambda x: f"{x} is a positive number"
)

negative_chain = RunnableLambda(
    lambda x: f"{x} is zero or negative"
)

# RunnableBranch
branch = RunnableBranch(
    (lambda x: x > 0, positive_chain),
    negative_chain  # default branch
)

# LCEL: connect another Runnable to the branch
chain = (
    RunnableLambda(lambda x: x * 2)
    | branch
)

print(chain.invoke(5))
# 10 is a positive number

print(chain.invoke(-3))
# -6 is zero or negative
How it works
Input: 5
  ↓
Lambda: x * 2
  ↓
10
  ↓
RunnableBranch
  ↓
10 > 0 ?
  ↓
positive_chain
  ↓
"10 is a positive number"
```
