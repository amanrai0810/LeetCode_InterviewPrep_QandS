# 98. Validate Binary Search Tree

## Problem

Given the `root` of a binary tree, determine whether it is a valid **Binary Search Tree (BST)**.

A BST satisfies the following conditions:

* The left subtree of a node contains only nodes with values **less than** the node's value.
* The right subtree of a node contains only nodes with values **greater than** the node's value.
* Both the left and right subtrees must also be valid BSTs.

---

## Example 1

```
       8
      / \
     3   10
    / \    \
   1   6    14
```

Output:

```
true
```

### Recursive Calls

```
validate(8, -∞, +∞)
│
├── validate(3, -∞, 8)
│   ├── validate(1, -∞, 3)
│   └── validate(6, 3, 8)
│
└── validate(10, 8, +∞)
    └── validate(14, 10, +∞)
```

Every node lies within its allowed range, so the tree is a valid BST.

---

## Example 2

```
      10
     /  \
    5    15
        /
       6
```

Output

```
false
```

### Recursive Calls

```
validate(10, -∞, +∞)
│
├── validate(5, -∞, 10) ✓
│
└── validate(15, 10, +∞)
    │
    └── validate(6, 10, 15) ✗
```

Node `6` violates the BST property because it must be greater than `10`.

---

# Approach

A common mistake is to compare a node only with its immediate parent.

Instead, every node must satisfy the range inherited from all its ancestors.

For each node:

* It must be greater than the minimum allowed value.
* It must be smaller than the maximum allowed value.
* Recursively validate the left subtree with an updated maximum.
* Recursively validate the right subtree with an updated minimum.

---

## Algorithm

1. If the current node is `null`, return `true`.
2. Check whether the node value lies within `(min, max)`.
3. If it doesn't, return `false`.
4. Recursively validate:

   * Left subtree using `(min, node.val)`
   * Right subtree using `(node.val, max)`
5. Return `true` only if both subtrees are valid.

---

## Why use `long` instead of `int`?

The node values are of type `int`, but the initial range should be larger than every possible integer.

Using

```java
Long.MIN_VALUE
Long.MAX_VALUE
```

avoids incorrect comparisons when a node contains:

```java
Integer.MIN_VALUE
```

or

```java
Integer.MAX_VALUE
```

If `int` limits were used as the initial bounds, these edge cases could fail.

---

## Java Solution

```java
class Solution {

    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean validate(TreeNode node, long min, long max) {

        if (node == null)
            return true;

        if (node.val <= min || node.val >= max)
            return false;

        return validate(node.left, min, node.val)
                && validate(node.right, node.val, max);
    }
}
```

---

## Dry Run

For the tree

```
       8
      / \
     3   10
    / \    \
   1   6    14
```

Execution order:

```
8 (-∞, +∞)
│
├── 3 (-∞, 8)
│   ├── 1 (-∞, 3)
│   └── 6 (3, 8)
│
└── 10 (8, +∞)
    └── 14 (10, +∞)
```

Every node satisfies its allowed range, so the function returns:

```
true
```

---

## Complexity Analysis

**Time Complexity**

```
O(n)
```

Every node is visited exactly once.

**Space Complexity**

```
O(h)
```

where `h` is the height of the tree due to the recursive call stack.

* Balanced Tree: `O(log n)`
* Skewed Tree: `O(n)`

---

## Key Takeaways

* Compare each node against a valid range, not just its parent.
* Update the range during recursion.
* Use `long` bounds to safely handle integer edge cases.
* Visit every node exactly once, resulting in an efficient `O(n)` solution.
