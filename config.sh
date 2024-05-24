sudo apt update -y
sudo apt install -y pip
sudo apt install -y python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt