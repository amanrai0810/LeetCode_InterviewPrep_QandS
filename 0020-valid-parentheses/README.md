# 20. Valid Parentheses

**Easy**

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

A string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

---

## Example 1

**Input:**

```text
s = "()"
```

**Output:**

```text
true
```

---

## Example 2

**Input:**

```text
s = "()[]{}"
```

**Output:**

```text
true
```

---

## Example 3

**Input:**

```text
s = "(]"
```

**Output:**

```text
false
```

---

## Example 4

**Input:**

```text
s = "([])"
```

**Output:**

```text
true
```

---

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

---

## Approach

Use a **Stack** to keep track of opening brackets.

- Push every opening bracket onto the stack.
- When a closing bracket is encountered:
  - If the stack is empty, return `false`.
  - Otherwise, pop the top element and check whether it matches the current closing bracket.
- After processing the entire string:
  - If the stack is empty, the string is valid.
  - Otherwise, return `false`.

---

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Java Solution

See [`0020-valid-parentheses.java`](0020-valid-parentheses.java).