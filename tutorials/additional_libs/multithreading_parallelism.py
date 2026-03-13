# Concurrency and Parallelism
# ---------------------------
# Python handles concurrent code in three main ways:
# 1. threading: Best for I/O-bound tasks (network requests, file reading). Subject to the GIL.
# 2. multiprocessing: Best for CPU-bound tasks (heavy math). Bypasses the GIL.
# 3. asyncio: Best for highly concurrent I/O-bound tasks using a single-threaded event loop.

import threading
import multiprocessing
import asyncio
import time

# --- Helper Functions ---

# I/O Bound Task (Simulated with time.sleep)
def io_bound_task(name, duration):
    print(f"[Thread {name}] Starting I/O operation...")
    time.sleep(duration) # Simulates waiting for a database or API response
    print(f"[Thread {name}] Finished I/O operation.")

# CPU Bound Task (Heavy computation)
def cpu_bound_task(name, iterations):
    print(f"[Process {name}] Starting heavy computation...")
    # Calculating the sum of squares up to 'iterations'
    total = sum(i * i for i in range(iterations))
    print(f"[Process {name}] Finished computation. Result length: {len(str(total))}")

# Async I/O Bound Task (Simulated with asyncio.sleep)
async def async_io_task(name, duration):
    print(f"[Async Task {name}] Starting async I/O...")
    await asyncio.sleep(duration) # Non-blocking wait
    print(f"[Async Task {name}] Finished async I/O.")

async def main_async():
    # asyncio.gather runs multiple async functions concurrently
    await asyncio.gather(
        async_io_task("A", 2),
        async_io_task("B", 2),
        async_io_task("C", 2)
    )

# --- Execution ---
# The 'if __name__ == "__main__":' block is MANDATORY when using multiprocessing on Windows,
# otherwise it causes an infinite recursive loop of process spawning.

if __name__ == "__main__":
    
    # 1. THREADING
    # ------------
    # Threads run in the same memory space. The Global Interpreter Lock (GIL) prevents 
    # multiple threads from executing Python bytecodes at once, but they release the GIL 
    # during I/O operations (like sleep, web requests).
    
    print("=== 1. THREADING (I/O Bound) ===")
    start_time = time.time()
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=io_bound_task, args=(f"T{i}", 2))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join() # Wait for all threads to finish
        
    print(f"Threading time: {time.time() - start_time:.2f} seconds (Should be ~2s, not 6s)\n")

    
    # 2. MULTIPROCESSING
    # ------------------
    # Spawns entirely separate OS processes, each with its own memory space and its own GIL.
    # True parallelism. Ideal for number crunching.
    
    print("=== 2. MULTIPROCESSING (CPU Bound) ===")
    start_time = time.time()
    
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=cpu_bound_task, args=(f"P{i}", 15_000_000))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join() # Wait for all processes to finish
        
    print(f"Multiprocessing time: {time.time() - start_time:.2f} seconds\n")


    # 3. ASYNCIO
    # ----------
    # Uses an Event Loop in a single thread. It uses the 'async' and 'await' keywords
    # to pause a function when it hits an I/O bottleneck and switch to another task instantly.
    # Highly efficient for things like web scraping thousands of URLs or handling WebSockets.
    
    print("=== 3. ASYNCIO (High Concurrency I/O Bound) ===")
    start_time = time.time()
    
    # Run the main asynchronous function
    asyncio.run(main_async())
    
    print(f"Asyncio time: {time.time() - start_time:.2f} seconds (Should be ~2s)")