echo "Making migrations"
python manage.py makemigrations
echo "Running migrations"
python manage.py migrate
echo "Copying template"
mkdir templates
cp ./client/dist/client/index.html ./templates/index.html
