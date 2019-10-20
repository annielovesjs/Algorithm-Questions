# return all the permutations with k distinct characters
# ex. input: inputStr = 'pqpqs'
# num = 2
# output: 7 bc [pq, pqp, pqpq, qp, qpq, pq, qs]
# approach - sliding window

def maxNumSubstr(inputStr, num):
    distinctCount = 0
    charCount = {}
    start = 0
    end = start
    result = []
    
    if num == 0:
        return 0
    elif num == 1:
        return len(inputStr)

    while(start <= end and end < len(inputStr)):
        if distinctCount == 0:
            charCount[inputStr[start]] = 1
            distinctCount = 1
        
        if distinctCount < num and end < len(inputStr):
            end+=1
            if end > len(inputStr)-1:
                continue
            if inputStr[end] not in charCount or charCount[inputStr[end]] == 0:
                distinctCount+=1
                charCount[inputStr[end]] = 1
            else:
                charCount[inputStr[end]]+=1
        else:
            if num == distinctCount:
                result.append(inputStr[start:end+1])
            if end == len(inputStr) - 1 or (not (end+1 >= len(inputStr)) and  inputStr[end+1] not in charCount):
                charCount[inputStr[start]]-=1
                if charCount[inputStr[start]] == 0:
                    distinctCount-=1
                start+=1
                while end > start + 1:
                    charCount[inputStr[end]]-=1
                    if charCount[inputStr[end]] == 0:
                        distinctCount -=1
                    end -=1
            else:
                end+=1
                if end >= len(inputStr):
                    continue
                if inputStr[end] not in charCount:
                    charCount[inputStr[end]] = 1
                else:
                    charCount[inputStr[end]] +=1
    print(result)
    print(charCount)
    return len(result)

print(maxNumSubstr('pqpqs6',4))

#words to exclude 
#return array with the most frequently used words -> if two have the same num and is max, 
#return both answers
#input:
# literatureText = "jack and jill went to the market to buy bread and cheese cheese is jack facroutie food"
# wordsToExclude = ["and", "he", "the", "to", "is"]
# output: ["jack", "cheese"]
# O(n + m) solution - store in dictionary the frequency, go through the string again, and look for the max frequency

def retrieveFrequentlyUsedWords(literatureText, wordsToExclude):
    literatureText = literatureText.split(' ')
    wordFrequency = {}
    bannedWords = {}
    maxfreq = 0
    results = []

    for word in wordsToExclude:
        bannedWords[word] = True
    print("banned")
    print(bannedWords)
    for word in literatureText:
        if word not in bannedWords:
            if word not in wordFrequency:
                wordFrequency[word] = 1
            else:
                wordFrequency[word] += 1
            if wordFrequency[word] > maxfreq:
                maxfreq = wordFrequency[word]
    print(wordFrequency)

    for word in literatureText:
        if word not in bannedWords:
            if wordFrequency[word] == maxfreq:
                results.append(word)
                bannedWords[word] = True

    return results

print(retrieveFrequentlyUsedWords("jack and jill went to the market to buy bread and cheese cheese is jack favorite food", ["and", "he", "the", "to", "is"]))


# most postive aggregate score
# given a list of product ID's and review scores, find the most positive aggreagate for each product
# positive aggregate is the average of the top 5 highest review scores
# input: 
# scoreCount - int representing the count of review scores for all the products
# reviewScoresOfProduct - list of nums where each element of the list consists of 
# an integer representing the productID and a real num representing the reviewScore
# of the product 

# non max heap implementation 
def positiveAggregate(scoreCount, reviewScoresOfProduct):
    productReviews = {}
    productID = None
    productReview = None
    result = []

    for review in reviewScoresOfProduct:
        productID = review[0].split(':')[1]
        productReview = int(review[1].split(':')[1])
        if productID not in productReviews:
            productReviews[productID] = [productReview]
        else:
            productReviews[productID].append(productReview)

    for key in productReviews:
        print(key)
        sum = 0
        productReviews[key].sort(reverse=True)
        for i in range(5):
            sum += productReviews[key][i]
        sum = sum / 5
        tempObj = ['productid:{}'.format(key), 'productReview:{}'.format(sum)]
        result.append(tempObj)
    print(productReviews)
    print(result)


sampleInput = [
    ['productid:1', 'reviewScore:4'],
    ['productid:1', 'reviewScore:9'],
    ['productid:1', 'reviewScore:1'],
    ['productid:1', 'reviewScore:5'],
    ['productid:1', 'reviewScore:1'],
    ['productid:1', 'reviewScore:3'],
    ['productid:1', 'reviewScore:2'],
    ['productid:1', 'reviewScore:7'],
    ['productid:2', 'reviewScore:1'],
    ['productid:2', 'reviewScore:4'],
    ['productid:2', 'reviewScore:1'],
    ['productid:2', 'reviewScore:3'],
    ['productid:2', 'reviewScore:2'],
    ['productid:2', 'reviewScore:5']
]
print(positiveAggregate(13, sampleInput))

