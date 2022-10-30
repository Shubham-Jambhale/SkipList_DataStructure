# SkipList

# Question

Yagna and Alex are discussing about the implementation of a lookup dictionary of words with
O(logn) complexity. Yagna came up with an idea of usage of skip lists. Lets help Yagna to
implement a lookup dictionary using skip list.

Following are the instructions for SkipList:

• Create a class with LookUpSkipList. It should have a constructor which takes the list of
  words and probability “P” with which the element is chosen to the next level.

• Class should have the methods lookup_search, delete, insert, print.

• Insert method inserts the word into skiplists.

• Delete method deletes the word from skiplists.

• Lookup_search method checks the presence of the word and if word presents returns the
  True else insert the word to the skiplist.

• Print method prints the words from bottom level to top level. Bottom level contains all the
  words.
  
 • All the methods except print should be implemented in O(logn) time complexity.
  
Note: The sorting of words can be like lexicographical order / dictionary order. All the words
are in Lower case. For comparing the strings you can use inbuilt python functions.

# Example:

lexicographical order : aa->aaa->ab->az->cd->df-> ja-> jb-> . . . -> z->za..
Evaluation Usage will be like this:
lu_sk_lists = LookUpSkipList([“iub”,”usa”,”there”,”sort”,”god”],0.6)
lu_sk_lists.print()
lu_sk_lists.insert(“word”)
lu_sk_lists.delete(“there”)
lu_sk_lists.lookup_search(“iub”)
lu_sk_lists.lookup_search(“present”)
  
  
