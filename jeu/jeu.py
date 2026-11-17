import pygame

class Jeu:

    def __init__(self):
        pygame.init()

        # dimensions de la fenètre de jeu
        self.largeur = 1000
        self.hauteur = 700

        # lancement de la fenètre
        self.fenetre = pygame.display.set_mode(
            (self.largeur, self.hauteur)
        )

        pygame.display.set_caption("Traffic Manager")

        self.horloge = pygame.time.Clock()
        self.en_cours = True

    def lancer(self):

        while self.en_cours:

            # gestion des événements
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    self.en_cours = False

            # couleur de fond
            self.fenetre.fill((40, 40, 40))

            # actualisation de l'affichage
            pygame.display.flip()

            self.horloge.tick(60)

        pygame.quit

#test