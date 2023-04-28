
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
            
        nodeMaping = dict()
        
        def dfs(inputNode):
            if inputNode in nodeMaping:
                return nodeMaping[inputNode]

            newNode = Node(inputNode.val)
            nodeMaping[inputNode] = newNode

            for nei in inputNode.neighbors:
                newNode.neighbors.append(dfs(inputNode))

        return dfs(node) 
