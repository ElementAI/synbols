from haven import haven_utils as hu

# Define exp groups for parameter search
EXP_GROUPS = {'fewshot_char':
                hu.cartesian_exp_group({
                    'lr':[0.1],
                    'batch_size':[1],
                    'model': "fewshot",
                    'backbone': "resnet18",
                    'max_epoch': 100,
                    'imagenet_pretraining': False,
                    'dataset': {'path':'/mnt/datasets/public/research/synbols/latin_res=32x32_n=100000.npz',
                                'name': 'fewshot_synbols',
                                'task': 'char',
                                # start 5-way 5-shot 15-query
                                'nclasses_train': 5, 
                                'nclasses_val': 5,
                                'nclasses_test': 5,
                                'support_size_train': 5,
                                'support_size_val': 5,
                                'support_size_test': 5,
                                'query_size_train': 15,
                                'query_size_val': 15,
                                'query_size_test': 15,
                                # end 5-way 5-shot 15-query
                                'train_iters': 600,
                                'val_iters': 600,
                                'test_iters': 600}})}