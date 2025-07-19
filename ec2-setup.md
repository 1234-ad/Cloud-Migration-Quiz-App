# EC2 Setup Instructions

1. Launch Ubuntu EC2 instance.
2. SSH into EC2.
3. Install Python, pip, virtualenv, Git.
4. Clone project repo.
5. Run `pip install -r requirements.txt`.
6. Start app using Gunicorn:
   ```
   gunicorn run:app --bind 0.0.0.0:5000
   ```