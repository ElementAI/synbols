from haven import haven_utils as hu

# Define exp groups for parameter search
EXP_GROUPS = {'active_font':
    hu.cartesian_exp_group({
        'lr': [0.001],
        'batch_size': [32],
        'model': "active_learning",
        'backbone': "vgg16",
        'num_classes': 1002,
        'query_size': [100],
        'learning_epoch': 10,
        'heuristic': ['bald', 'random', 'entropy'],
        'iterations': [1, 20],
        'max_epoch': 100,
        'imagenet_pretraining': [True],
        'dataset': {'path': '/mnt/datasets/public/research/synbols/latin_res=32x32_n=100000.npz',
                    'name': 'active_learning',
                    'task': 'font',
                    'p': 0.0,
                    'initial_pool': 2000,
                    'seed': 1337,
                    'uncertainty_config': {'is_bold': {}}}}),
    'active_font_noise':
        hu.cartesian_exp_group({
            'lr': [0.001],
            'batch_size': [32],
            'model': "active_learning",
            'backbone': "vgg16",
            'num_classes': 1002,
            'query_size': [100],
            'learning_epoch': 10,
            'heuristic': ['bald', 'random', 'entropy'],
            'iterations': [1, 20],
            'max_epoch': 100,
            'imagenet_pretraining': [True],
            'dataset': {
                'path': '/mnt/datasets/public/research/synbols/latin_res=32x32_n=100000.npz',
                'name': 'active_learning',
                'task': 'font',
                'p': 0.1,
                'initial_pool': 2000,
                'seed': 1337,
                'uncertainty_config': {'is_bold': {}}}}),
}
