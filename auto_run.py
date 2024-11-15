import os
import yaml
import torch

para_dict = {
    'dataset':'d',
    'fedtype':'f',
    'global_rounds':'c',
    'gpu':'g',
    'iid_beta':'iid_b',
    'learning_rate':'lr',
    'local_step':'i',
    'logdir':'l',
    'n_trainer':'n',
    'num_hops':'nhop',
    'num_layers':'nl',
    'repeat_time':'r',
    'pruning':'p'
}

if __name__ == '__main__':
    with open('.\config\config_cli.yaml','r') as file:
        config = yaml.safe_load(file)

    command = config.get("command",'')
    parameters = config.get("parameters",{})

    for i in range(5,6):
        cmd_list = [command]

        for key, value in parameters.items():
            if isinstance(value,bool):
                if value:
                    cmd_list.append(f"-{para_dict[key]}")
            elif key == 'n_trainer':
                cmd_list.append(f"-{para_dict[key]}=\"{i}\"")
            else:
                cmd_list.append(f"-{para_dict[key]}=\"{value}\"")

        cmd = " ".join(cmd_list)
        print(cmd)

        torch.cuda.empty_cache()
        os.system(cmd)


