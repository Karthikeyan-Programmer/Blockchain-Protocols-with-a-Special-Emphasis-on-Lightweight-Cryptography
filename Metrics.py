import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
def PerformanceMetrics():
    def update(frame, time_data, tps_data, line):
        time_data.append(frame)
        tps_data.append(np.random.randint(0, 5001))
        line.set_data(time_data, tps_data)
        return line,
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 5000)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Transactions Per Second')
    def init():
        line.set_data([], [])
        return line,
    num_frames = 200
    ani = animation.FuncAnimation(
        fig, update, frames=num_frames, init_func=init, fargs=([], [], line),
        interval=50, blit=True
    )
    plt.show()
    def calculate_storage_overhead(block_size):
        return block_size / 20.0
    block_sizes = list(range(400, 2801, 100))
    storage_overheads = [calculate_storage_overhead(size) for size in block_sizes]
    plt.plot(block_sizes, storage_overheads, marker='o', linestyle='-', color='b')
    plt.xlabel('Block Size (transactions/block)')
    plt.ylabel('Total Storage Overhead (MB)')
    plt.title('Block Size vs Total Storage Overhead')
    plt.grid(True)
    plt.show()
    def update(frame, num_nodes, recovery_latency, bars):
        num_nodes.append(frame)
        recovery_latency[frame] = np.random.randint(80, 161)
        for bar, height in zip(bars, recovery_latency):
            bar.set_height(height)
        return bars
    fig, ax = plt.subplots()
    num_nodes = []
    recovery_latency = np.zeros(100)
    bars = ax.bar(np.arange(len(recovery_latency)), recovery_latency)
    ax.set_xlim(0, 100)
    ax.set_ylim(80, 160)
    ax.set_xlabel('Number of Nodes')
    ax.set_ylabel('Recovery Latency (ms)')
    ax.set_title('Number of Nodes vs Recovery Latency')
    ani = animation.FuncAnimation(
        fig, update, frames=100, fargs=(num_nodes, recovery_latency, bars),
        interval=500, blit=False
    )
    plt.show()
    def update(frame, data_sizes, encryption_times, sc):
        data_sizes.append(frame)
        encryption_time = np.random.randint(1000, 6001) 
        encryption_times.append(encryption_time)
        sc.set_offsets(np.c_[data_sizes, encryption_times])
        return sc,
    fig, ax = plt.subplots()
    data_sizes = []
    encryption_times = []
    sc = ax.scatter([], [], c='blue', marker='o', label='Encryption Time')
    ax.set_xlim(128, 64000)
    ax.set_ylim(1000, 6000)  
    ax.set_xlabel('Data Size (KB)')
    ax.set_ylabel('Encryption Time (ms)')
    ax.set_title('Data Size vs Encryption Time')
    ax.legend()
    ani = animation.FuncAnimation(
        fig, update, frames=np.arange(128, 64001, 1000), fargs=(data_sizes, encryption_times, sc),
        interval=500, blit=False
    )
    plt.show()
    def update(frame, data_sizes, decryption_times, bars):
        data_sizes.append(frame)
        decryption_time = np.random.randint(0, 4501)
        decryption_times[frame] = decryption_time
        for bar, height in zip(bars, decryption_times):
            bar.set_height(height)
        return bars
    fig, ax = plt.subplots()
    data_sizes = []
    decryption_times = np.zeros(64000)  
    bars = ax.bar(np.arange(len(decryption_times)), decryption_times, color='red')
    ax.set_xlim(0, 64000)  
    ax.set_ylim(0, 4500)
    ax.set_xlabel('Data Size (KB)')
    ax.set_ylabel('Decryption Time (ms)')
    ax.set_title('Data Size vs Decryption Time')
    ani = animation.FuncAnimation(
        fig, update, frames=np.arange(128, 64001, 1000),
        fargs=(data_sizes, decryption_times, bars),
        interval=10, blit=False  
    )
    plt.show()










