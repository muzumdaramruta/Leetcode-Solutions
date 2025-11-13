/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}
*/

class Solution {
    public Node construct(int[][] grid) {
        int n = grid.length;
        return buildQuadTree(grid, 0, 0, n-1, n-1);
    }
    
    private Node buildQuadTree(int[][] grid, int left, int top, int right, int bottom) {
        // Check if the sub-grid has the same value
        boolean isLeaf = true;
        int val = grid[top][left];
        for (int i = top; i <= bottom; i++) {
            for (int j = left; j <= right; j++) {
                if (grid[i][j] != val) {
                    isLeaf = false;
                    break;
                }
            }
            if (!isLeaf) {
                break;
            }
        }
        // If the sub-grid has the same value, create a leaf node
        if (isLeaf) {
            return new Node(val == 1, true, null, null, null, null);
        }
        // If the sub-grid has different values, divide it into four sub-grids
        int midRow = (top + bottom) / 2;
        int midCol = (left + right) / 2;
        Node topLeft = buildQuadTree(grid, left, top, midCol, midRow);
        Node topRight = buildQuadTree(grid, midCol+1, top, right, midRow);
        Node bottomLeft = buildQuadTree(grid, left, midRow+1, midCol, bottom);
        Node bottomRight = buildQuadTree(grid, midCol+1, midRow+1, right, bottom);
        // Create a non-leaf node with the four children
        return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
    }
}