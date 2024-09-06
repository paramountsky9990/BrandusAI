echo "build loading.........."
pip3 install -r requirements.txt

echo "staticfiles build....."
python3 manage.py collectstatic --noinput

