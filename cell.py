# life_1d.py
import random, time
import matplotlib.pyplot as plt

# --- Parameter (anpassbar) ---
N = 41            # Anzahl Zellen
STEPS = 10000       # Anzahl Zeitschritte
RULE = 110        # 0..255 (110 wirkt "lebendig")
SEED = "center"   # "center" oder "random"
DELAY = 0.0001      # Sekunden zwischen Frames
PRINT_ROWS = True # ASCII-Ausgabe pro Schritt

def rule_to_bits(r):
    # Map 3er-Nachbarschaft (111..000) -> neuer Zustand
    return [(r >> i) & 1 for i in range(8)]

def step(state, bits):
    N = len(state)
    out = [0]*N
    for i in range(N):
        left  = state[(i-1) % N]
        mid   = state[i]
        right = state[(i+1) % N]
        neighborhood = (left<<2) | (mid<<1) | right
        out[i] = bits[neighborhood]
    return out

def show(state):
    print("".join("#" if x else "." for x in state))

def count_alive(state):
    return sum(state)

def main():
    # Startzustand
    if SEED == "center":
        state = [0]*N
        state[N//2] = 1
    else:
        state = [random.randint(0,1) for _ in range(N)]

    bits = rule_to_bits(RULE)

    # Metriken sammeln
    steps = []
    alive_counts = []

    # Simulation
    for t in range(STEPS):
        if PRINT_ROWS:
            show(state)
        steps.append(t)
        alive_counts.append(count_alive(state))

        state = step(state, bits)
        time.sleep(DELAY)

    # Plot am Ende
    plt.figure()
    plt.plot(steps, alive_counts)
    plt.xlabel("Step")
    plt.ylabel("Alive cells")
    plt.title(f"1D Cellular Automaton – RULE {RULE}, N={N}, seed={SEED}")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
