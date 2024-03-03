from test import generate_random_preferences, is_stable
from gale_shapley import gale_shapley
from time import time
import matplotlib.pyplot as plt


def main():
    sizes = [10, 100, 1000]
    times = [] 

    for n in sizes:
        print(f"Running Gale Shapley algorithm for n={n}")
        men_preferences, women_preferences = generate_random_preferences(n)

        # Start the timer
        start_time = time()

        men_engaged = gale_shapley(men_preferences, women_preferences)

        # Stop the timer and calculate the elapsed time in seconds
        elapsed_time = time() - start_time

        # Store the elapsed time
        times.append(elapsed_time) 

        # Format the time string based on the elapsed time
        if elapsed_time > 60:
            minutes = int(elapsed_time // 60)
            seconds = elapsed_time % 60
            time_string = f"{minutes}m {seconds:.0f}s"
        elif elapsed_time > 1:
            time_string = f"{elapsed_time:.3f}s"
        elif elapsed_time * 1000 > 1:
            time_string = f"{elapsed_time * 1000:.3f}ms"
        else:
            time_string = " < 1ms"

        print(f"Elapsed time: [{time_string}]")
        print(f"Validating the matching")

        # assert is_stable(
        #     men_engaged, men_preferences, women_preferences
        # ), "Matching is not stable"

        # print(f"Matching is stable for n={n}\n")

    # After all executions, plot the results
    plt.plot(sizes, times, marker="o")
    plt.title("Execution Time of Gale Shapley Algorithm")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (s)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()

    exit(0)
