import sys
import os


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [number]")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print(f"Usage: {sys.argv[0]} [number] (number must be an integer)")
        sys.exit(1)
    number = sys.argv[1]
    if not os.path.exists(number):
        os.mkdir(number)

    sol_path = os.path.join(number, "sol.py")
    if not os.path.exists(sol_path):
        with open(sol_path, "w") as f:
            f.write("class Solution(object):\n")

    md_path = os.path.join(number, "report.md")
    if not os.path.exists(md_path):
        report_data = f"## Problem {number}\n"
        report_data += (
            "- Time Complexity: \n" "- Space Complexity: \n" "- Relative Algorithms: \n"
        )
        with open(md_path, "w") as f:
            f.write(report_data)
