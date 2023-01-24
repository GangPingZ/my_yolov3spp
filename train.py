#一 import
import argparse
import yaml
from torch.utils.tensorboard import SummaryWriter





#二 def train(hyp)
def train(hyp):
    pass





#三 if __name__=="__main__":






if __name__ == '__main__':
    ##1.参数占位三步走。opt：Namespace()
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=30)
    opt = parser.parse_args()

    ##2.超参数以及一些设置准备
        #1.加载设置的超参数hyp.yaml，后面训练需要。
    with open(opt.hyp) as f:
        hyp = yaml.load(f, Loader=yaml.FullLoader)
        #2.确定输出文件保存的目录。
    tb_writer = SummaryWriter(comment=opt.name)

    ##3.开始训练
    train(hyp)




