from flask import Flask
import os
import psutil
from datetime import datetime
import pytz

app = Flask(__name__)

# Function to get the top command output (simplified for demo)
def get_top_output():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        process_list.append(f"{proc.info['pid']} {proc.info['name']} {proc.info['cpu_percent']} {proc.info['memory_info'].rss}")
    return "\n".join(process_list)

@app.route('/htop')
def htop():
    # Full name (you can change this to your actual name)
    name = "Your Full Name"

    # Username
    username = os.getlogin()

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Top output (simulated)
    top_output = get_top_output()

    # HTML response
    response = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>User:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <p><strong>Top Output:</strong></p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)