from chain import Chain

chain = Chain(10)

for i in range(5):
    chain.add_to_pool(str(i))
    chain.mine()
