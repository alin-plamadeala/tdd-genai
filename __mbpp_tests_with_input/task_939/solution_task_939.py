def sorted_models(models):
    return sorted(models, key=lambda x: (-x['model'], x['make'].lower()))
