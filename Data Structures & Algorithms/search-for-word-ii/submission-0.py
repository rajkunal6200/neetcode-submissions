class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):

        root = TrieNode()

        # Build Trie
        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):

            char = board[r][c]

            if char not in parent.children:
                return

            node = parent.children[char]

            # Word found
            if node.word:
                result.append(node.word)
                node.word = None

            # Mark visited
            board[r][c] = "#"

            # Explore 4 directions
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "#"):

                    dfs(nr, nc, node)

            # Backtracking
            board[r][c] = char

            # PRUNING: Remove exhausted Trie branch
            if not node.children and node.word is None:
                del parent.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result