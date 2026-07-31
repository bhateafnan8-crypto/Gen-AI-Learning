"""
🔹 Step 1: Create a virtual environment: python -m venv myenv
(myenv is just a folder name—you can name it anything.)

🔹 Step 2: Activate the environment
✅ On Windows: myenv\Scripts\activate
✅ On Mac/Linux: source myenv/bin/activate
After activation, you’ll see the environment name in your terminal prompt like:
(myenv) user@machine:~$

🔹 Step 3: Install libraries (isolated from global): pip install requests

🔹 Step 4: Deactivate when done: deactivate


📦 Example: Project Folder Structure
my_project/
│
├── myenv/              ← virtual environment
├── main.py             ← your code
├── requirements.txt    ← all installed packages


Generate requirements.txt: pip freeze > requirements.txt

Install from it: pip install -r requirements.txt
"""