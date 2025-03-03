

# Connexion au service container d'Heroku
heroku container:login

# Création de l'application
heroku create api-ynov

# Construction de l'image Docker sous Windows
docker build . -t api-ynov

# Tag Image Docker au registery d'Heroku
docker tag api-ynov registry.heroku.com/api-ynov/web

# Publication de l'image Docker dans le registery d'Heroku
docker push registry.heroku.com/api-ynov/web

# Configuration du cotainer
heroku stack:set container -a api-ynov

# Activation du container
heroku container:release web -a api-ynov

# Ouverture de l'application
heroku open -a api-ynov


#Consignes FASTAPI/Docker
# 1. Mettre l'application Streamlit dans un Container Docker
# 2. Créer une page de documentation de l'API sur le front (iFrame de /docs de l'api sur le front)  
# 3. Créer une Page et un formulaire qui fait appel à l'API