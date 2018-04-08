def adjacentElementsProduct(inputArray):
    prodArray = []
    for i in range(0, len(inputArray)-1):
        product = inputArray[i]*inputArray[i+1]
        prodArray.append(product)
    return max(prodArray)
