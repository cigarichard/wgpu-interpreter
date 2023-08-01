import subprocess
import time
import csv

def run_command(command):
    start_time = time.time()
    process = subprocess.run(command, shell=True)
    end_time = time.time()
    exec_time = end_time - start_time
    return exec_time

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Run', 'Execution Time'])
        for i, exec_time in enumerate(data):
            writer.writerow([i+1, exec_time])

if __name__ == "__main__":
    command = 'xdsl-run --wgpu examples/1.mlir'
    runs = 10
    exec_times = [run_command(command) for _ in range(runs)]
    write_to_csv(exec_times, 'evaluation_result/execution_times.csv')
