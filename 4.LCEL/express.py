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
    RunnableLambda(lambda x: x*2 )
    | branch
)

print(chain.invoke(5))
# 10 is a positive number

print(chain.invoke(-3))
# -6 is zero or negative