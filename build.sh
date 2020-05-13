echo "Making migrations"
python manage.py makemigrations
echo "Running migrations"
python manage.py migrate
echo "Copying template"
mkdir templates
cp ./dist/index.html ./templates/index.html
