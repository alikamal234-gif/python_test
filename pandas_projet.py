"""
Projet d'apprentissage Pandas - Défis Pratiques

Ce fichier contient une série de défis pour vous aider à pratiquer et maîtriser 
la bibliothèque Pandas en Python. 

Les données à utiliser se trouvent dans le fichier 'ventes.csv'.
"""

import pandas as pd

# ==========================================
# DÉFI 1 : Chargement et exploration des données
# ==========================================

def charger_donnees(chemin_fichier):
    """
    Charge les données depuis un fichier CSV dans un DataFrame Pandas.
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier CSV.
        
    Returns:
        pd.DataFrame: Le DataFrame contenant les données.
    """
    return pd.read_csv(chemin_fichier)

def afficher_infos_de_base(df):
    """
    Affiche les informations de base sur le DataFrame (types de données, 
    valeurs non nulles, utilisation de la mémoire).
    
    Args:
        df (pd.DataFrame): Le DataFrame à analyser.
        
    Returns:
        None (Affiche simplement les informations dans la console)
    """
    return df.info() 

# ==========================================
# DÉFI 2 : Nettoyage et transformation
# ==========================================

def ajouter_colonne_chiffre_affaires(df):
    """
    Ajoute une nouvelle colonne 'chiffre_affaires' au DataFrame.
    Le chiffre d'affaires est calculé en multipliant le 'prix_unitaire' 
    par la 'quantite'.
    
    Args:
        df (pd.DataFrame): Le DataFrame d'origine.
        
    Returns:
        pd.DataFrame: Le DataFrame modifié avec la nouvelle colonne.
    """
    

def filtrer_ventes_par_ville(df, ville):
    """
    Filtre le DataFrame pour ne garder que les ventes réalisées dans 
    une ville spécifique.
    
    Args:
        df (pd.DataFrame): Le DataFrame avec toutes les ventes.
        ville (str): Le nom de la ville à filtrer (ex: 'Paris').
        
    Returns:
        pd.DataFrame: Un nouveau DataFrame contenant uniquement les ventes 
                      de la ville spécifiée.
    """
    pass

# ==========================================
# DÉFI 3 : Agrégation et GroupBy
# ==========================================

def calculer_ventes_totales_par_categorie(df):
    """
    Calcule le chiffre d'affaires total pour chaque catégorie de produits.
    (Nécessite que la colonne 'chiffre_affaires' ait été ajoutée au préalable).
    
    Args:
        df (pd.DataFrame): Le DataFrame contenant les données de ventes.
        
    Returns:
        pd.Series ou pd.DataFrame: Les ventes totales indexées par 'categorie'.
    """
    pass

def trouver_produit_le_plus_vendu(df):
    """
    Trouve le produit (nom) qui a été le plus vendu en termes de quantité totale.
    
    Args:
        df (pd.DataFrame): Le DataFrame contenant les données de ventes.
        
    Returns:
        str: Le nom du produit le plus vendu.
    """
    pass

# ==========================================
# DÉFI 4 : Tri et Sélection
# ==========================================

def obtenir_top_5_ventes(df):
    """
    Trie le DataFrame pour trouver les 5 ventes générant le plus grand 
    chiffre d'affaires.
    
    Args:
        df (pd.DataFrame): Le DataFrame contenant les données.
        
    Returns:
        pd.DataFrame: Un DataFrame contenant les 5 meilleures ventes, triées 
                      par chiffre d'affaires décroissant.
    """
    pass


# ==========================================
# ZONE DE TEST (Pour tester vos fonctions)
# ==========================================
if __name__ == "__main__":
    # Vous pouvez écrire votre code de test ici !
    print("Début des défis Pandas...")
    
    # Dé-commentez les lignes suivantes pour tester votre code
    fichier = "ventes.csv"
    df = charger_donnees(fichier)
    # print(df.head())
    print(afficher_infos_de_base(df))
