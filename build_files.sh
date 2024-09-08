# echo "build loading.........."
python3 install -r requirements.txt

# echo "staticfiles build....."
python3 manage.py collectstatic --noinput

# #!/bin/bash

# echo "Building loading.........."
# pip3 install -r requirements.txt

# if [ $? -ne 0 ]; then
#     echo "Error: Failed to install dependencies."
#     exit 1
# fi

# echo "Static files build....."
# python3 manage.py collectstatic --noinput

# if [ $? -ne 0 ]; then
#     echo "Error: Failed to collect static files."
#     exit 1
# fi

# echo "Build completed successfully."


