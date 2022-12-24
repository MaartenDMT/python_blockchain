from chain import Chain

chain = Chain(10)

i=0

while (True):
    data = input("add something to te chain: ")
    chain.add_to_pool(data)
    chain.mine()
    if i % 5 == 0:
        print(chain.blocks[i])
        
    i +=1
        