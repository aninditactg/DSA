class T:
    def __init__(self,data):
        self.data =data
        self.left_child= None
        self.right_child = None
    
def insert_BST(root,val):
    if root is None:
        return T(val)
    elif val < root.data:
        root.right_child= insert_BST (root.left_child,val)
    elif val > root.data:
        root.right_child= insert_BST(root.right_child,val)
    return root
    
def search_BST(root,item):
    #if item== root.data:
    if root is None or item == root.data:
        return root
        #print ("value found!")
    elif item < root.data:
        return search_BST(root.left_child,item)
    else:
        return search_BST(root.right_child,item)
       
def inorder_tree(root):
    if root:
        inorder_tree(root.left_child)
        print(root.data)
        inorder_tree(root.right_child)
           
def preorder_tree(root):
    if root:
        print (root.data)
        preorder_tree (root.left_child)
        preorder_tree(root.right_child)
                   
def postorder_tree(root):
    if root:
        postorder_tree(root.left_child)
        postorder_tree(root.right_child)
        print(root.data)
        
root = T(5)
#insert_BST(root,5)
insert_BST(root,10)
insert_BST(root,15)
insert_BST(root,1)
insert_BST(root,25)
#inorder_tree(root)
#search_BST(root,10)
# preorder_tree(root)
postorder_tree(root)
if search_BST(root,150) is None:
     print ("value not found")
else:
     print("value found")

                   
