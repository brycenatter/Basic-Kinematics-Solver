# Basic-Kinematics-Solver
Kinamatic equation solver built spacifically for a NumWorks calculator but can also be used in the command line or any Python-compatible calculator. This script was built using only the "math" module, which is only used for taking a square root. The script is layed out with each of the four kinematic equations defined as a seperate function.



### Installation:
- On a NumWorks calculator:
  - First option: 
    1. Download the Python File [kin.py](https://raw.githubusercontent.com/natterbr21/Kinamatics-for-NumWorks/38202025e8a0321457aa8dcbafb4ebab5dff519e/kin.py)
    2. Copy and paste into NumWorks script editor
    3. Install using [NumWorks Workshop](https://workshop.numworks.com/)
  - Second option:
    1. Use the [direct link](https://workshop.numworks.com/python/natterbr21/kin) to install the script

- In the command line:
   1. Download the Python File [kin.py](https://raw.githubusercontent.com/natterbr21/Kinamatics-for-NumWorks/38202025e8a0321457aa8dcbafb4ebab5dff519e/kin.py)
   2. Run using Python 3


### Usage:
When used in the command line or on a Python-compatible calculator, the usage is the same.

- For information that is not given in the problem use a **"n"**
- Place a **"s"** in for the varible you want to solve for
- Only one variable can be a **"n"** and only one variable can be a **"s"**
  - Exception: If position data is not given, you must put a **"n"** in both "Position (Final)" and "Position (Inital)".
- This script can only solve for problems with uniform acceleartion
- When solving for "Time", there will sometimes be two answers due to the quadratic nature of the equation. Just remember that negative time doesn't really exist.


### Example:

![Example Image](https://raw.githubusercontent.com/natterbr21/Kinamatics-for-NumWorks/main/images/NumWorksexample.gif)
