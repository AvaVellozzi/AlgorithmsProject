import time
import random

def generate_input(filename, n):
    # generates input file with random prefs for hospitals and residents
    with open(filename, "w") as f:
        f.write(f"{n}\n")
        
        # Generate hospital prefs
        for _ in range(n):
            prefs = list(range(n))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")

        # Generate resident prefs
        for _ in range(n):
            prefs = list(range(n))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")

def read_input(file):
    # Reads input file & extract num of participants and their prefs
    with open(file, 'r') as f:
        # Number of hospitals/residents
        n = int(f.readline().strip())
        hospitals_prefs = [list(map(int, f.readline().strip().split())) for _ in range(n)]
        residents_prefs = [list(map(int, f.readline().strip().split())) for _ in range(n)]
    return n, hospitals_prefs, residents_prefs

def write_output(file, matches):
    # Writes stable matches to an output file
    with open(file, 'w') as f:
        for hospital, resident in matches:
            f.write(str(hospital) + " " + str(resident) + "\n")

class PriorityQueue:
    # priority queue implementation for managing free hospitals
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        # Removes and returns the smallest element (aka highest priority)
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            min_val = self.heap[0]
            self.heap.pop()
            return min_val
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, i):
        # Chapter 2.5 of txtbk - restore heap property after insertion
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _heapify_down(self, i):
        # Chapter 2.5 of txtbk - restore heap property after extraction
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def is_empty(self):
        return len(self.heap) == 0

def stable_matching(hospitals_prefs, residents_prefs):
    # Implements the Gale Shapley algo for stable matching
    n = len(hospitals_prefs)
    result = []
    free_hospitals = PriorityQueue()
    
    for hospital in range(n):
        free_hospitals.insert(hospital)
    
    # -1 means the resident is free
    resident_pairing = [-1] * n
    # track next resident each hospital proposes to
    hospital_next_proposal = [0] * n
    resident_rank = [{resident: rank for rank, resident in enumerate(prefs)} for prefs in residents_prefs]
    
    # Continue matching process while there's still free hospitals
    while not free_hospitals.is_empty():
        # Extract next free hospital w/ the highest priority
        hospital = free_hospitals.extract_min()
        
        # Find the resident that this hospital is proposing to next
        resident = hospitals_prefs[hospital][hospital_next_proposal[hospital]]
        
        # Move to next pref for the hospital in case this proposal is rejected
        hospital_next_proposal[hospital] += 1
        
        # If resident not paired -> accept hospital's proposal
        if resident_pairing[resident] == -1:
            resident_pairing[resident] = hospital
        else:
            # If resident already paired -> check if they prefer new hospital
            current_hospital = resident_pairing[resident]
            
            # Compare rankings of new & current hospitals for this resident
            if resident_rank[resident][hospital] < resident_rank[resident][current_hospital]:
                # Resident prefers new hospital so switch
                resident_pairing[resident] = hospital
                
                # Prev matched hospital becomes free again and reenters queue
                free_hospitals.insert(current_hospital)
            else:
                # Resident prefers their current hospital so new hospital remains free
                free_hospitals.insert(hospital)

    # Construct final list of stable matches
    for resident in range(len(resident_pairing)):
        hospital = resident_pairing[resident]
        pair = (hospital, resident)
        result.append(pair)
    return result

if __name__ == "__main__":
    # Different sizes to test scalability
    test_sizes = [10, 50, 100, 500, 1000]
    results = []

    for size in test_sizes:
        input_file = f"input_{size}.txt"
        output_file = f"output_{size}.txt"
        
        generate_input(input_file, size)
        n, hospitals_prefs, residents_prefs = read_input(input_file)
        
        start_time = time.time()
        matches = stable_matching(hospitals_prefs, residents_prefs)
        end_time = time.time()
        
        write_output(output_file, matches)
        
        execution_time = round(end_time - start_time, 5)
        results.append((size, execution_time))
        print(f"Processed size: {size}, Time taken: {execution_time} seconds")

    print("\nSummary of Execution Times:")
    for size, exec_time in results:
        print(f"n = {size}: {exec_time} sec")
