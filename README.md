
---

# README - Phase 1 : Conception et Développement

## Description du projet

Ce projet vise à créer une application web pour collecter et analyser les retours des étudiants sur différentes formations proposées. Cette phase de conception et développement s'articule autour de la mise en place d'une architecture robuste, d'une base de données performante et d'un backend fiable pour traiter les retours.

---

## 1. Base de données : db_digital

### 1.1. Configuration
La base de données utilisée pour ce projet est gérée via **phpMyAdmin** avec les spécifications suivantes :
- **Nom de la base de données** : `db_digital`
- **Système de gestion** : MySQL
- **Serveur local** : WampServer
- **Utilisateur MySQL** : `root`
- **Mot de passe** : *(aucun mot de passe configuré)*

### 1.2. Structure des tables principales

#### **Table : feedbacks**
Contient les données relatives aux retours des étudiants :
| Champ              | Type         | Description                                      |
|--------------------|--------------|--------------------------------------------------|
| `id`              | INT (PK, AI) | Identifiant unique du retour                     |
| `formation`       | VARCHAR(255) | Nom de la formation                              |
| `prioriteRetour`  | ENUM          | Niveau de priorité (`faible`, `moyenne`, `haute`)|
| `typeRetour`      | VARCHAR(255) | Type de retour (contenu, formateur, etc.)        |
| `date`            | DATE         | Date du retour                                  |
| `rating`          | INT          | Évaluation sur une échelle de 1 à 5             |
| `comments`        | TEXT         | Commentaires de l'utilisateur                   |
| `attachedfiles`   | TEXT         | Chemin vers les fichiers joints                 |
| `consentement`    | BOOLEAN      | Consentement pour l'utilisation des données     |

#### **Table : users**
Pour gérer les utilisateurs de l'application (administrateurs et étudiants) :
| Champ          | Type         | Description                         |
|----------------|--------------|-------------------------------------|
| `id`          | INT (PK, AI) | Identifiant unique de l'utilisateur |
| `username`    | VARCHAR(255) | Nom d'utilisateur                   |
| `email`       | VARCHAR(255) | Adresse e-mail                      |
| `password`    | VARCHAR(255) | Mot de passe haché                  |
| `role`        | ENUM          | Rôle (`admin`, `student`)           |

---

## 2. Backend : Conception et Développement

### 2.1. Architecture
Le backend est conçu avec **Django**, intégrant un ORM (Object-Relational Mapping) pour interagir avec la base de données MySQL.

- **Modèle MVC** : Séparation claire entre la logique métier (Models), les interactions utilisateur (Views), et la présentation (Templates).
- **API REST** : À intégrer dans les prochaines phases pour exposer les données des retours via une API.

### 2.2. Modèles Django

Les modèles ci-dessous reflètent la structure des tables mentionnées précédemment :

#### **Modèle : Feedback**
```python
from django.db import models

class Feedback(models.Model):
    FORMATIONS = [
        ('data_engineering', 'Data Engineering'),
        ('data_science', 'Data Science'),
        ('web_development', 'Développement Web'),
        ('cyber_security', 'Cybersécurité'),
        ('artificial_intelligence', 'Intelligence Artificielle'),
        ('cloud_computing', 'Cloud Computing'),
    ]

    formation = models.CharField(max_length=255, choices=FORMATIONS)
    prioriteRetour = models.CharField(max_length=20, choices=[('faible', 'Faible'), ('moyenne', 'Moyenne'), ('haute', 'Haute')])
    typeRetour = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    comments = models.TextField()
    attachedfiles = models.FileField(upload_to='uploads/', blank=True, null=True)
    consentement = models.BooleanField()

    def __str__(self):
        return f"{self.formation} - {self.typeRetour}"
```

#### **Modèle : User**
```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = [
        ('admin', 'Administrateur'),
        ('student', 'Étudiant'),
    ]
    role = models.CharField(max_length=10, choices=ROLES)
```

---

## 3. Frontend : Intégration avec Django

- **Templates** : Les fichiers HTML sont organisés dans le dossier `templates/feedback` pour une meilleure gestion.
- **CSS et JS** : Les fichiers statiques sont gérés via le dossier `static/feedback` et incluent le fichier CSS principal (`style.css`) et les scripts JavaScript associés.

---

## 4. Instructions pour le déploiement local

1. **Cloner le dépôt :**
   ```bash
   git clone <url-du-repo>
   cd <nom-du-repo>
   ```

2. **Configurer la base de données :**
   - Créez la base `db_digital` dans phpMyAdmin.
   - Importez le fichier SQL de migration (fichier `db_digital.sql` si fourni).

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Effectuer les migrations :**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Lancer le serveur de développement :**
   ```bash
   python manage.py runserver
   ```

6. **Accéder à l'application :**
   - Rendez-vous sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 5. Étapes suivantes

- Implémenter un système de génération de rapports automatiques.
- Ajouter une fonctionnalité d'analyse de sentiment.

---

## Auteur
Fouejio Francky Joël  
Mastère 2 en Intelligence Artificielle  et Science des Données  

--- 

Ce fichier README se concentre sur les étapes essentielles de la **Phase 1** tout en restant extensible pour documenter les phases suivantes.
