# EA EXAM SOLVING — Strict Beginner Instructions

## WHY SIMPLE CODE
Write code like a first-year student who just learned Python. Exams expect basic solutions — if you use advanced Python features, graders may think you copied or don't understand the basics. Simple code is also easier to debug and explain if asked.

## ABSOLUTE RULES (Never break)
- Only `import numpy as np` — nothing else
- NO classes, NO OOP, NO lambda, NO map, NO filter, NO list comprehensions beyond basic ones
- Only use: basic functions (def), for loops, while loops, if/else, numpy arrays/vectors, lists, simple variables
- NO special calls: no `itertools`, no `collections`, no `functools`, no `operator`, no `zip` with unpacking tricks
- Population is a simple list of lists: `[[gene1, gene2, ..., fitness], ...]`
- Fitness is ALWAYS the last element of each individual (access with `p[-1]` or `p[len(p)-1]`)
- Use `[:]` to copy lists — never assign `a = b` (that's a reference, not a copy)
- Rejection sampling: `if not feasible: continue` — simplest way to handle constraints
- Fitness is ALWAYS maximization. If problem says minimize → `fitness = 100 / cost`
- Minimal comments — just `# I:` and `# E:` per function

## FINDING THE BEST INDIVIDUAL — DO IT WITH A FOR LOOP
```python
# DO THIS (simple for loop):
best_idx = 0
best_fit = population[0][-1]
for i in range(1, len(population)):
    if population[i][-1] > best_fit:
        best_fit = population[i][-1]
        best_idx = i
best = population[best_idx]

# DO NOT USE: max(population, key=lambda p: p[-1])
# Lambdas are not beginner-level. Use the for loop above.
```

## HOW TO IDENTIFY REPRESENTATION
| What problem asks for | Type | How to generate |
|---|---|---|
| "chosen/not", "0 or 1" | Binary | `x = list(np.random.randint(0, 2, n))` |
| "amount", "value in [a,b]" | Real | `x = [round(np.random.uniform(a, b), 2) for _ in range(n)]` |
| "order", "sequence", "arrangement" | Permutation | `x = list(np.random.permutation(n))` |
| "count", "number of" | Integer | `x = list(np.random.randint(a, b, n))` |

## FITNESS FUNCTION
```python
def fitness(x):
    # I: x - list of genes
    # E: fitness value (float, higher = better)
    result = ...  # compute based on problem formula
    return round(result, 2)
```
Rules:
- If problem says "minimize cost" → `return round(100.0 / cost, 2)`
- If fitness can be negative → use tournament selection (not roulette)
- Knapsack: return 0 if over budget
- Portfolio: `return round(x[0]*return1 + x[1]*return2 + ..., 2)`

## CONSTRAINT CHECKER
```python
def check(x):
    # I: x - list of genes
    # E: True if feasible, False if violates any constraint
    if riskFactor(x) >= 2.5:
        return False
    if x[0] + x[1] + x[2] > 100000:
        return False
    return True
```
**Important**: Generate values that naturally satisfy easy constraints. For budget=100000: generate T2 first, then T1, then T3 = 100000 - T1 - T2 (guarantees sum = budget). Only reject on hard constraints like risk limits.

## GENERATE POPULATION — Your exact pattern
```python
def generate_pop(dim):
    # I: dim - number of individuals to generate
    # E: pop - list of [genes..., fitness]
    pop = []
    i = 0
    while i < dim:
        # Generate candidate (adjust based on representation type)
        T2 = round(np.random.uniform(0, 30000), 2)
        T1 = round(np.random.uniform(0, 100000 - T2), 2)
        T3 = round(100000 - T1 - T2, 2)
        x = [T1, T2, T3]

        # Skip if infeasible (rejection sampling)
        if riskFactor(x) >= 2.5:
            continue

        # Append genes + fitness
        f = fitness(x)
        x.append(f)
        pop.append(x)
        i = i + 1
    return pop
```

## MUTATION — Simple per-gene loop
```python
def mutate(x, pm):
    # I: x - individual (list), pm - mutation probability
    # E: mutated copy of x
    result = x[:]  # make a copy
    n = len(result)
    for j in range(n):
        r = np.random.uniform(0, 1)
        if r <= pm:
            # Binary: flip bit
            if result[j] == 0:
                result[j] = 1
            elif result[j] == 1:
                result[j] = 0
            # Real: add Gaussian noise (uncomment for real problems)
            # result[j] = result[j] + np.random.normal(0, 0.1)
            # result[j] = round(result[j], 2)
            # Permutation: swap two positions (uncomment for perm problems)
            # k = np.random.randint(0, n)
            # temp = result[j]
            # result[j] = result[k]
            # result[k] = temp
            # break  # only one swap for permutations
    return result
```

## CROSSOVER — Single-point
```python
def crossover(p1, p2, pc):
    # I: p1, p2 - parents (lists), pc - crossover probability
    # E: two children (lists)
    r = np.random.uniform(0, 1)
    if r > pc:
        return p1[:], p2[:]  # no crossover, return copies
    # Single-point crossover
    k = np.random.randint(1, len(p1))
    c1 = p1[:k] + p2[k:]
    c2 = p2[:k] + p1[k:]
    return c1, c2
```

## SELECTION — Roulette (simple for loop version)
```python
def roulette_select(pop, dim):
    # I: pop - population list, dim - number to select
    # E: selected - list of selected individuals
    selected = []

    # Get fitness values
    fits = []
    for i in range(len(pop)):
        fits.append(pop[i][-1])

    # Sum fitness
    total = 0.0
    for f in fits:
        total = total + f

    if total == 0:
        return pop[:]

    # Cumulative probabilities
    cum = []
    s = 0.0
    for f in fits:
        s = s + f / total
        cum.append(s)

    # Select individuals
    for _ in range(dim):
        r = np.random.uniform(0, 1)
        for i in range(len(cum)):
            if r <= cum[i]:
                selected.append(pop[i][:])
                break
    return selected
```

## TOURNAMENT (if fitness can be negative)
```python
def tournament_select(pop, dim, k):
    # I: pop - population, dim - number to select, k - tournament size
    # E: selected - list of selected individuals
    selected = []
    n = len(pop)
    for _ in range(dim):
        # Pick k random indices
        best_idx = -1
        best_fit = -999999999
        for _ in range(k):
            idx = np.random.randint(0, n)
            if pop[idx][-1] > best_fit:
                best_fit = pop[idx][-1]
                best_idx = idx
        selected.append(pop[best_idx][:])
    return selected
```

## ELITISM — Always include
```python
# Find best parent
best_p_idx = 0
best_p_fit = population[0][-1]
for i in range(1, len(population)):
    if population[i][-1] > best_p_fit:
        best_p_fit = population[i][-1]
        best_p_idx = i

# Find best offspring
best_o_idx = 0
best_o_fit = offspring[0][-1]
for i in range(1, len(offspring)):
    if offspring[i][-1] > best_o_fit:
        best_o_fit = offspring[i][-1]
        best_o_idx = i

# Inject best parent if better
if best_p_fit > best_o_fit:
    idx = np.random.randint(len(offspring))
    offspring[idx] = population[best_p_idx][:]
```

## COMPLETE MAIN LOOP (Your exact structure)
```python
# Generate initial population
population = generate_pop(50)

# Evolution loop
NMAX = 200
for gen in range(NMAX):
    # 1. Parent selection
    parents = roulette_select(population, len(population))

    # 2. Crossover (pair parents)
    offspring = []
    for i in range(0, len(parents) - 1, 2):
        c1, c2 = crossover(parents[i], parents[i+1], 0.8)
        offspring.append(c1)
        offspring.append(c2)

    # 3. Mutation
    mutated = []
    for i in range(len(offspring)):
        m = mutate(offspring[i], 0.1)
        mutated.append(m)
    offspring = mutated

    # 4. Elitism (paste the elitism code block above here)

    # 5. Replace population
    population = offspring

    # 6. Termination — check diversity
    max_fit = population[0][-1]
    min_fit = population[0][-1]
    for i in range(1, len(population)):
        if population[i][-1] > max_fit:
            max_fit = population[i][-1]
        if population[i][-1] < min_fit:
            min_fit = population[i][-1]
    if max_fit == min_fit:
        break

# Find and print best solution
best_idx = 0
best_fit = population[0][-1]
for i in range(1, len(population)):
    if population[i][-1] > best_fit:
        best_fit = population[i][-1]
        best_idx = i
best = population[best_idx]
print(f"Best: {best[:-1]} with fitness {best[-1]}")
```

## DEFAULT PARAMETERS
| Parameter | Value |
|---|---|
| Population size | 50 |
| Crossover probability | 0.8 |
| Mutation probability | 0.1 |
| Max generations | 200 |
| Tournament size | 2 |

## OUTPUT FORMAT
```python
print("T1 | T2 | T3 | Fitness | Risk")
for i in range(len(population)):
    p = population[i]
    print(str(p[0]) + " | " + str(p[1]) + " | " + str(p[2]) + " | " + str(p[-1]) + " | " + str(riskFactor(p)))
```

## MCQ FORMAT (test.txt) — Just list the correct answer
```
1. Question text here?
**Answer: The correct answer text here**

2. Next question?
**Answer: The correct answer text here**
```
Do NOT list all options A-D. Just write the question and the correct answer directly.

## WHAT NOT TO USE (Ever)
- NO `lambda` — use for loops to find max/min
- NO `max(list, key=...)` — use for loop with index tracking
- NO classes — everything is flat functions + variables
- NO `map()`, `filter()` — use for loops
- NO `itertools`, `collections` — only numpy
- NO f-strings with complex expressions — build strings with `+`
- NO list comprehensions beyond simple `[x for x in range(n)]`
- NO `zip()`, `enumerate()` beyond basic usage
- NO `*args`, `**kwargs` — use explicit parameter names

## FINE THE SHORTEST AND SIMPLEST SOLUTION POSSIBLE AND FOR COMMENTS USE ULTRA SIMPLE BASIC ONES OR NONE AT ALL
 - FOR MCQs SHOW ME QUESTION and below correct answer letter + text + reasoning
 - For code and comments ultra short bsic no specialcharcaters or emojis or formatting allowed only simple ultra short basic text + previous recommendations (DO NOT USE ANY ---------- OR ______ or ======= OR ANYTHING ELSE OUTSIDE a-zA-Z :)

## HERE IS THE SUBJECT:


