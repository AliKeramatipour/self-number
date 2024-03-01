or key, value in temporary_dict.items():
            if key not in bricks or bricks[key] > value:
                bricks[key] = value