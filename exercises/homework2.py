# задачка 1
address = "1.1.1.1"
print(address.replace('.','[.]'))

# # задачка 2
# class Solution:
#     sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
#     def mostWordsFound(self, sentences):
#         print(max(len(sentences[i]. split())
#                 for i in range(len(sentences))))


# задачка 3

operations = ["--X","X++","X++"]
count = 0
for i in operations:
    if '+' in i:
        count += 1
    else:
        count -= 1
    print(count)


#2
    #
    # res = [len(i.split(' ')) for i in sentences]
    # return max(res)

    # max = 0
    # for i in sentences:
    #     n = len(i.split(' '))
    #     if n > max:
    #         max = n
    # return max