# AI-Powered LMS

<img src="https://raw.githubusercontent.com/ravikumawat7716/StudyQuest-GenAI-powered-LMS/refs/heads/main/frontend/public/SE%20Team%2023%20.jpg" alt="SE Team 23">

## Local Project Setup

### **Prerequisites**

Ensure you have the following tools installed:

- **Git**: Download and install it from [Git's official site](https://git-scm.com/).
- **Python 3.x**: Download and install it from [Python's official site](https://www.python.org/downloads/).
- **Node.js**: Download and install it from [Node.js official site](https://nodejs.org/).

---

### **Steps**

#### **1. Clone the Repository**

Open your terminal and run the following command to clone the repository to your local machine:
```bash
git clone https://github.com/ravikumawat7716/StudyQuest-GenAI-powered-LMS.git
```

#### **2. Backend Setup**

If you prefer to use your system's global Python environment, you can skip steps 2 and 3. However, using a virtual environment is recommended.

**Step 2.1: Create a Virtual Environment**

- Navigate to the `backend` folder and create a virtual environment:
  ```bash
  python3 -m venv venv
  ```

**Step 2.2: Activate the Virtual Environment**

- Activate the virtual environment based on your operating system:
  - On Linux/Mac:
    ```bash
    source ./venv/bin/activate
    ```
  - On Windows:
    ```bash
    .\venv\Scripts\activate
    ```

**Step 2.3: Install Backend Dependencies**

- Install the required Python packages using pip:
  ```bash
  pip install -r requirements.txt
  ```

**Step 2.4: Configure MongoDB**

- Update the MongoDB URI in the `backend/model/connection.py` file with your MongoDB connection string.

**Step 2.5: Start the Backend Server**

- Run the backend server using:
  ```bash
  python main.py
  ```

---

#### **3. Ollama Installation and Running Qwen-2-0.5B**

**Step 3.1: Download and Install Ollama**

1. Visit the [Ollama download page for Windows](https://www.ollama.com/download/windows).
2. Download the installer and follow the on-screen instructions to complete the installation.

**Step 3.2: Run the Qwen-2 Model**

- Open your terminal and execute:
  ```bash
  ollama run qwen2:0.5b
  ```

This will download the Qwen-2 model and run it.

---

#### **4. Frontend Setup**

**Step 4.1: Firebase Configuration**

- Create a new Firebase project in the [Firebase Console](https://console.firebase.google.com/).
- Update the Firebase configuration in the following files:
  - `frontend/src/config.js`
  - `frontend/src/firebase.js`

**Step 4.2: Install Frontend Dependencies**

- Navigate to the `frontend` directory:
  ```bash
  cd frontend
  ```
- Install the required Node.js packages:
  ```bash
  npm install
  ```

**Step 4.3: Run the Frontend Application**

- Start the frontend application:
  ```bash
  npm run dev
  ```
- Access the application in your web browser at [http://localhost:5173/](http://localhost:5173/).

---

### **Development Process**

You are now ready to start the development process for the AI-Powered LMS application. Use the following URLs:

- **Frontend**: [http://localhost:5173/](http://localhost:5173/)
- **Backend**: [http://localhost:5000/](http://localhost:5000/)
