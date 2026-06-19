from math import gcd
import cmath
from typing import List, Tuple, Set

# =============================================
# PAIR CLASS - Core of your notation
# =============================================
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

# =============================================
# CORE CONSTANTS
# =============================================
ONE = 1
ZERO = 0
I = complex(0, 1)
MINUS_I = -I
MINUS_ONE = -1

print("THE ABSOLUTE SQUARE ROOT OF 1")
print("=" * 88)

# =============================================
# 1. ABSOLUTE SQUARE ROOT
# =============================================
print("1 ∈ √1 = 1 ⊆ (1,√1) , (√1,1) , (1,1)")
pairs_sqrt = {Pair(1,1), Pair(1,ONE), Pair(ONE,1)}
for p in pairs_sqrt:
    print("   ", p)

print("\n1 - 1 = 0")
pairs_zero = {Pair(1,-1), Pair(0,1), Pair(0,-1), Pair(0,0)}
for p in pairs_zero:
    print("   ", p)

# =============================================
# 2. IMAGINARY UNIT EXTRACTION
# =============================================
print("\n" + "="*88)
print("IMAGINARY UNIT EXTRACTION")
print("="*88)

print("√-1 = i ⊆ (i,1) , (1,i) , (0,i)")
pairs_i = {Pair(I,1), Pair(1,I), Pair(0,I)}
for p in pairs_i:
    print("   ", p)

print("\nΓ1/i = -i")
pairs_minus_i = {Pair(I, MINUS_I), Pair(MINUS_I, I), Pair(1, MINUS_I), Pair(MINUS_I, 1)}
for p in pairs_minus_i:
    print("   ", p)

print("\nΓ-i/i = -1")
pairs_minus1 = {Pair(I,-1), Pair(-1,I), Pair(MINUS_I,-1), Pair(-1, MINUS_I), Pair(-1,0)}
for p in pairs_minus1:
    print("   ", p)

# =============================================
# 3. BRANCHING PRIMACY
# =============================================
print("\n" + "="*88)
print("BRANCHING PRIMACY — SIMULTANEOUS EXECUTION")
print("="*88)

print("BRANCH 1 (Imaginary Rotor)")
print("Γi+i = 2i ⊆ (i,i) , (i,2i) , (2i,0)")
two_i = 2 * I
print("   2i =", two_i)

print("i² = -1 ⊆ (i,i) , (i,-1) , (-1,0)")
print("i² =", I*I)

print("Γ2i-i = i")
print("2i - i =", two_i - I)

print("\nBRANCH 2 (Real + Rational)")
def successor(n): return n + 1

print("Γ1+1 =", successor(1))
print("Γ9+1 =", successor(9))
print("Γ99+1 =", successor(99))

# =============================================
# 4. RATIONAL EXTENSIONS
# =============================================
print("\n" + "="*88)
print("RATIONAL EXTENSIONS (1/k) & RECIPROCALS")
print("="*88)

rationals = [
    (2, 0.5),
    (3, 1/3),
    (4, 0.25),
    (5, 0.2),
    (6, 1/6),
    (7, 1/7),
    (8, 0.125),
    (9, 1/9),
    (10, 0.1)
]

for k, val in rationals:
    print(f"Γ1/{k} = {val} ⊆ (1,{k}) , ({k},{val}) , ({val},0)")

print("\nRECIPROCALS:")
print("Γ1/.5 = 2 ⊆ (1,.5) , (.5,2) , (2,0)")
print("Γ1/.999999999 ≈ 1.000000001")

print("\nNEGATIVE DIRECTION:")
print("Γ1-2 = -1 ⊆ (1,-2) , (2,-1) , (-1,0)")

# =============================================
# 5. id_X and Γ OPERATOR
# =============================================
def id_X(x):
    return x

def Gamma(a, b=0):
    """Γ(a·1 + b·i) = z"""
    return complex(a, b)

print("\nΓ(a·1 + b·i) = z  with  gcd(p,q)=1")
print("Example: Γ(1 + 2i) =", Gamma(1,2))

# =============================================
# 6. ASCII COMPLEX PLANE
# =============================================
print("\n" + "="*88)
print("ASCII COMPLEX PLANE (Expanded View)")
print("="*88)
print("""          Im
 -3i  -2i   -i    0    +i   +2i   +3i
  │     │     │     │     │     │     │
-3 ┼─────┼─────┼─────┼─────┼─────┼─────┼───── Re
  │     │     │     │     │     │     │
-2 ┼─────┼─────┼─────┼─────┼─────┼─────┼─────
  │     │(-1,i)│     │ (1,i)│     │     │
-1 ┼─────┼─────┼─────┼─────┼─────┼─────┼─────
  │     │     │     │     │     │     │
 0 ┼─────┼─────┼─────┼─────●─────┼─────┼───── ← (0,0)
  │     │     │ (0,0)│     │     │     │
+1 ┼─────┼─────┼─────┼─────┼─────┼─────┼─────
  │     │(-1,-i)│   │ (1,-i)│    │     │
+2 ┼─────┼─────┼─────┼─────┼─────┼─────┼─────
  │     │     │     │     │     │     │
+3 ┼─────┼─────┼─────┼─────┼─────┼─────┼─────
 -3   -2    -1    0    +1    +2    +3""")

print("\nKey Marked Points:")
print("• (1,1)     → Absolute Anchor")
print("• (0,1)     → i")
print("• (0,-1)    → -i")
print("• (-1,0)    → -1 ← Branch Interchange Pivot")
print("• (2,0)     → n+1 Example")
print("• (.5,0)    → 1/2 Example")

# =============================================
# 7. PARAMETER SPACE CLOSURE
# =============================================
print("\n" + "="*88)
print("PARAMETER SPACE CLOSURE (Interchangeable Branches)")
print("="*88)
print("REAL / RATIONAL GENERATOR  ⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄⇄  IMAGINARY i-Rotor")
print("n+1 ↔ 1-n ↔ 1/k ↔ k")
print("Dense Closed Field ℂ via Γ(a + bi) + gcd(p,q)=1")
print("Logical Biconditional: 1 ⇔ -1 (Always Held)")

print("\n" + "="*88)
