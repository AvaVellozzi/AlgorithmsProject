import time
import random

def read_input(file):
    with open(file, 'r') as f:
        n = int(f.readline().strip())
        men_prefs = [list(map(int, f.readline().strip().split())) for _ in range(n)]
        women_prefs = [list(map(int, f.readline().strip().split())) for _ in range(n)]
    return n, men_prefs, women_prefs

def write_output(file, result):
    with open(file, 'w') as f:
        for pair in result:
            f.write(f"{pair[0]} {pair[1]}\n")

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val

    def heapify_up(self, i):
        if i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                self.heapify_up(parent)

    def heapify_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0


def stable_matching(hospitals_prefs, residents_prefs):
    n = len(hospitals_prefs)
    free_hospitals = PriorityQueue()
    for hospital in range(n):
        free_hospitals.insert(hospital)
    
    resident_pairing = [-1] * n  # Index of the man each woman is engaged to
    hospital_next_proposal = [0] * n  # Next woman each man will propose to
    resident_rank = [{resident: rank for rank, resident in enumerate(prefs)} for prefs in residents_prefs]
    
    while not free_hospitals.is_empty():
        hospital = free_hospitals.extract_min()
        resident = hospitals_prefs[hospital][hospital_next_proposal[hospital]]
        hospital_next_proposal[hospital] += 1
        
        if resident_pairing[resident] == -1:
            resident_pairing[resident] = hospital
        else:
            current_hospital = resident_pairing[resident]
            if resident_rank[resident][hospital] < resident_rank[resident][current_hospital]:
                resident_pairing[resident] = hospital
                free_hospitals.insert(current_hospital)
            else:
                free_hospitals.insert(hospital)
    
    return [(hospital, resident) for resident, hospital in enumerate(resident_pairing)]

# Read input
n, men_prefs, women_prefs = read_input("input.txt")
start_time = time.time()
result = stable_matching(men_prefs, women_prefs)
end_time = time.time()
write_output("output.txt", result)
print(f"Processed size: {n}, Time taken: {end_time - start_time:.5f} seconds")
