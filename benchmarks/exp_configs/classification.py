from haven import haven_utils as hu

# Define exp groups for parameter search
EXP_GROUPS = {'font':
                hu.cartesian_exp_group({
                    'lr':[0.1],
                    'batch_size':[256],
                    'model': "classification",
                    'backbone': "resnet18",
                    'max_epoch': 100,
                    'imagenet_pretraining': False,
                    'episodic': False,
                    'dataset': {'path':'/mnt/datasets/public/research/synbols/latin_res=32x32_n=100000.npz',
                                'name': 'synbols',
                                'task': 'font'}}),
                'font_pretrained': hu.cartesian_exp_group({
                    'lr':[0.01],
                    'batch_size':[256],
                    'model': "classification",
                    'backbone': "resnet18",
                    'max_epoch': 100,
                    'episodic': False,
                    'imagenet_pretraining': [True],
                    'dataset': {'path':'/mnt/datasets/public/research/synbols/latin_res=32x32_n=100000.npz',
                                'name': 'synbols',
                                'task': 'font'}}),
                'font_plain':
                    hu.cartesian_exp_group({
                        'lr':[0.1],
                        'batch_size':[512],
                        'model': "classification",
                        'backbone': "resnet18",
                        'max_epoch': 100,
                        'imagenet_pretraining': False,
                        'episodic': False,
                        'num_classes': 982,
                        'dataset': {'path':'/mnt/datasets/public/research/synbols/plain_n=1000000.npz',
                                    'name': 'synbols',
                                    'task': 'font'}}),
                    'font_pretrained': hu.cartesian_exp_group({
                        'lr':[0.01],
                        'batch_size':[256],
                        'model': "classification",
                        'backbone': "resnet18",
                        'max_epoch': 100,
                        'episodic': False,
                        'imagenet_pretraining': [True],
                        'dataset': {'path':'/mnt/datasets/public/research/synbols/latin_res=32x32_n=100000.npz',
                                    'name': 'synbols',
                                    'task': 'font'}}),                
                }