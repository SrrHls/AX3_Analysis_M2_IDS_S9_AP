import matplotlib.pyplot as plt

# ...existing code...

def plot_intervals(intervals):
    fig, axs = plt.subplots(6, 1, figsize=(10, 15))
    
    for i, interval in enumerate(intervals):
        axs[i].plot(interval)
        axs[i].set_title(f'Interval {i+1}')
        axs[i].set_xlabel('Time')
        axs[i].set_ylabel('Amplitude')
    
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Replace these with your actual interval data
    interval1 = [1, 2, 3, 4, 5]
    interval2 = [2, 3, 4, 5, 6]
    interval3 = [3, 4, 5, 6, 7]
    interval4 = [4, 5, 6, 7, 8]
    interval5 = [5, 6, 7, 8, 9]
    interval6 = [6, 7, 8, 9, 10]
    
    intervals = [interval1, interval2, interval3, interval4, interval5, interval6]
    plot_intervals(intervals)
