import collections

def main():
    N = int(input())
    S = [input() for i in range(N)]
    c = collections.Counter(S) 
    """
    count the number of same strings' emergence in the list "S",
    and collections.Counter returns the dict data like "{"name": "the number of emergence"}"
    """

    print(c.most_common()[0][0]) 
    
    """
    dict_object.most_common returns the list like "[(name,the number of emergence), ... ]"
    if you would like to get the biggest number of list, you can get it by pointing the index.
    """


if __name__ == "__main__":
    main()