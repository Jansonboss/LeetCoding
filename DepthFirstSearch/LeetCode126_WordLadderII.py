# https://leetcode.com/problems/word-ladder-ii/
# This is implicit graph using 
# BFS from end point to get distance + DFS  from start poit to get path

#                            end point
#                            ^
#                           /
#                          |
#		  word1	------- word5
#       /     \       /     \
##     /       \    /        \
#    word2 -- word3---------word6
#      \         /
#       \      /
#        word4 



#                        A: start point
#                    / 	 	  \
#                  B           C: end point
#                /  \          |
#              E     F         |
#            /   \ /  \       /  
#          G     H     I    /
#           \   /  \ /    /
#             J     K   /
#              \   /   / 
#               \ /  /
#				  I