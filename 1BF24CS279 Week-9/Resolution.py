# Week 9: FOL Resolution
# Prove that John likes Peanuts

# Resolution function
def resolve(c1, c2):

    for literal in c1:
        if literal.startswith("~"):
            opposite = literal[1:]
        else:
            opposite = "~" + literal

        if opposite in c2:
            # Remove complementary literals
            resolvent = (c1 - {literal}) | (c2 - {opposite})

            # Remove tautological clauses
            if any(
                (lit.startswith("~") and lit[1:] in resolvent)
                or ("~" + lit) in resolvent
                for lit in resolvent
            ):
                continue

            return resolvent

    return None


# Main program
print("FOL Resolution")
print("Goal: John likes Peanuts\n")

# Ground clauses obtained from the FOL knowledge base
C1 = {"~Food(Peanuts)", "Likes(John,Peanuts)"}
C2 = {"~Eats(Anil,Peanuts)",
      "Killed(Anil)", "Food(Peanuts)"}

C3 = {"Eats(Anil,Peanuts)"}
C4 = {"Alive(Anil)"}
C5 = {"~Alive(Anil)", "~Killed(Anil)"}

# Negation of the goal
C6 = {"~Likes(John,Peanuts)"}

# Step 1: Resolve C4 and C5
print("Step 1:")
r1 = resolve(C4, C5)
print("Alive(Anil) and Alive -> Not Killed")
print("Result:", r1)

# Step 2: Resolve C2 and C3
print("\nStep 2:")
r2 = resolve(C2, C3)
print("Eats(Anil,Peanuts) and Food Rule")
print("Result:", r2)

# Step 3: Resolve r1 and r2
print("\nStep 3:")
r3 = resolve(r1, r2)
print("Not Killed(Anil) and Food Rule")
print("Result:", r3)

# Step 4: Resolve with C1
print("\nStep 4:")
r4 = resolve(r3, C1)
print("Food(Peanuts) and John likes all food")
print("Result:", r4)

# Step 5: Resolve with negated goal
print("\nStep 5:")
r5 = resolve(r4, C6)
print("Likes(John,Peanuts) and Negated Goal")
print("Result:", r5)

# Final result
print("\nFinal Result:")

if r5 == set():
    print("Empty Clause Obtained.")
    print("Goal Proved: John likes Peanuts.")
else:
    print("Goal Not Proved.")