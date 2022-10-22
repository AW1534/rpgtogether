from src.helper.rendering import Page


def heal(player, args, renderer):
    if player.health == player.max_health:
        Page(title="heal", text="You are already at maximum health.")
        return False
    else:
        healing = player.max_health - player.health
        Page(title="heal", text=[f"You have healed {healing} hp.",
                                 f"You currently have {player.health} hp."])
        player.health += healing
        return True
