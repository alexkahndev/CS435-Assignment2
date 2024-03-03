# CS435-Assignment2

## Description

This project implements the Gale-Shapley algorithm in Python for stable matching. The program generates random preferences for men and women and confirms that the Gale-Shapley algorithm always returns a stable matching.

## Installation

### Project Installation

Instructions on how to install the project.

```sh
git clone https://github.com/alexkahndev/CS435-Assignment2.git
```

### Python Installation

Here are the commands to install Python on various devices:

#### Windows
```sh
Start-Process msiexec.exe -Wait -ArgumentList '/I https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe /passive InstallAllUsers=1 PrependPath=1'
```

#### macOS
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install python
```

#### Linux (Ubuntu)
```sh
sudo apt-get update && sudo apt-get install python3.9
```

Please replace \`3.9.5\` and \`python3.9\` with the version you want to install. These commands will download and install Python directly from the official website or through package managers like Homebrew or APT. Always refer to the official documentation for the most accurate and up-to-date information. After installing Python, you can verify the installation by typing \`python --version\` in the command line. This should display the installed version of Python.

## Dependencies

Used matplotlib to graph time data

## Usage

To run the program run 

```sh
python main.py
```

## Bugs

Testing with n = 100000 caused a memory error on my device and was ommited in my final answer

### Best Friend and Worst Friend

In the Gale-Shapley algorithm, a participant's "best friend" would be their most preferred choice that also finds the match acceptable. The "worst friend" would be the least preferred choice that is still a valid match (i.e., they have not rejected the participant).

## Findings

In the analysis, the Gale-Shapley algorithm was tested with different sizes: 10, 100, 1000, 10000, 100000. The execution time is expected to increase quadratically with the size of the input due to the algorithm’s time complexity of O(n^2). This complexity arises because each man may propose to each woman once in the worst-case scenario, contributing an ‘n’ factor for each man and woman, resulting in O(n*n) or O(n^2). Therefore, when plotting the execution time against the input size, an upward-opening parabolic curve is expected, indicating that the execution time increases as the square of the input size. The testing and plotting with matplotlib confirm this expectation, showing that the time to complete the algorithm increases quadratically, providing empirical evidence supporting the theoretical time complexity.
