from argparse import ArgumentParser


def get_test_argument():
    parser = ArgumentParser()
    parser.add_argument('-f')
    parser.add_argument('--type', default ='test',type=str,  help='')
    parser.add_argument("--data_dir", default='/content/drive/MyDrive/Project_HK1_2022/NLP/Code/data_test',  type=str, help="Đường dẫn data đầu vào")
    parser.add_argument("--model_path", default='/content/drive/MyDrive/Project_HK1_2022/NLP/Code/output/best_model.pt', type=str, help="")
    parser.add_argument("--overwrite_data", action='store_true', default=True, help="")
    parser.add_argument("--batch_size", default=16, type=int, help="")
    parser.add_argument('--num_worker', type=int, default=2, help="")
    parser.add_argument("--no_cuda", action='store_true', help="")
    parser.add_argument("--model_arch", default='hier_roberta_ml', type=str, choices=['hier_roberta_sl', 'hier_roberta_ml', 'hier_bert_ml'], help="")
    return parser.parse_args()


def get_train_argument():
    parser = ArgumentParser()
    parser.add_argument('-f')
    parser.add_argument('--type',default ='train', type=str, help='')
    parser.add_argument("--task", default='UIT-ViSD4SA', type=str, choices=['UIT-ViSD4SA'], help="")
    parser.add_argument("--data_dir", default='/content/drive/MyDrive/Project_HK1_2022/NLP/Code/data_test', type=str,help="")
    parser.add_argument("--overwrite_data", action='store_true', default=True, help="")
    parser.add_argument("--load_weights", default=None, type=str,help='')
    parser.add_argument("--model_name_or_path", default='vinai/phobert-base', type=str, help="")
    parser.add_argument("--model_arch", default='hier_roberta_ml', type=str, help="")
    parser.add_argument("--output_dir", default='/content/drive/MyDrive/Project_HK1_2022/NLP/Code/output', type=str, help="")
    parser.add_argument("--max_seq_length", default=256, type=int, help="")
    parser.add_argument("--train_batch_size", default=40, type=int, help="")
    parser.add_argument("--eval_batch_size", default=32, type=int, help="")
    parser.add_argument("--learning_rate", default=1e-4, type=float, help="")
    parser.add_argument("--classifier_learning_rate", default=3e-3, type=float, help="")
    parser.add_argument("--epochs", default=4, type=int, help="")
    parser.add_argument("--warmup_proportion", default=0.1, type=float, help="")
    parser.add_argument("--weight_decay", default=0.01, type=float, help="")
    parser.add_argument("--adam_epsilon", default=1e-6, type=float, help="")
    parser.add_argument("--max_grad_norm", default=1.0, type=float, help="")
    parser.add_argument("--early_stop", default=10.0, type=float, help="")
    parser.add_argument("--run_test", action='store_true', default=True, help="")
    parser.add_argument("--no_cuda", action='store_true', default=False,help="")
    parser.add_argument('--seed', type=int, default=422, help="")
    parser.add_argument('--num_workers', type=int, default=0,help="")
    parser.add_argument('--save_step', type=int, default=10000, help="")
    parser.add_argument('--gradient_accumulation_steps', type=int, default=1, help="")
    return parser.parse_args()
