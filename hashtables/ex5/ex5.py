# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # ---  first attempt only passes half of the tests.  Problem with duplicate keys---
    # #create hashtable
    # hashtable = {}
    # # create result array
    # result = []
    # # loop through all of the files and add to the hashtable k = ext v = filePath
    # for i in files:
    #     subStringArray = i.split('/')
    #     ext = subStringArray[len(subStringArray) - 1]
    #     hashtable[ext] = i
    # # loop through the queries to find the matches in the hashtable
    # for i in queries:
    #     if i in hashtable:
    #         result.append(hashtable[i])
    # print(result)
    # return result

    # create a hashtable
    hashtable = {}
    # create a result array
    result = []
    # loop through and add ext as the key and an array of paths for the value
    for i in files:
        subStringArray = i.split("/")
        ext = subStringArray[len(subStringArray) - 1]
        if ext in hashtable:
            hashtable[ext].append(i)
        else:
            hashtable[ext] = [i]
    # loop through queries and add bating key values to the array(concat the arrays together)
    for i in queries:
        if i in hashtable:
            result = result + hashtable[i]
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
