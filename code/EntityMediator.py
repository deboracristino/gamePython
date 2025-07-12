from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        player = None
        enemies = []

        for ent in entity_list:
            if isinstance(ent, Enemy):
                enemies.append(ent)
            elif ent.__class__.__name__ == "Player":
                player = ent

        if not player:
            return

        for enemy in enemies:
            # Colisão com jogador
            if player.rect.colliderect(enemy.rect):
                enemy.health = 0
            # Passou do jogador (ponto por desvio)
            elif enemy.rect.right < player.rect.left and not hasattr(enemy, 'counted'):
                player.score += 1
                enemy.counted = True
                enemy.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                entity_list.remove(ent)
