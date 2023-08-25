        if root.value == target:
            print(level)
        getLevel(root.lchild, target, level+1)
        getLevel(root.rchild, target, level+1)
