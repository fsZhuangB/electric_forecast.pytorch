# @Author : bamtercelboo
# @Datetime : 2018/07/19 22:35
# @File : model_LSTM.py
# @Last Modify Time : 2018/07/19 22:35
# @Contact : bamtercelboo@{gmail.com, 163.com}

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np
import random
import torch.nn.init as init

"""
Neural Networks model : LSTM
"""


class LSTM(nn.Module):
    
    def __init__(self, seq_length, hidden_size, dropout=0.75, num_layer=2):
        super(LSTM, self).__init__()

        # lstm
        self.lstm = nn.LSTM(seq_length, hidden_size, dropout=dropout, num_layers=num_layer)

        # linear
        self.hidden2label = nn.Conv1d(48, 48, 7, stride=1)
        # dropout
        self.module_name = "LSTM"

    def forward(self, x):
        # lstm
        lstm_out, _ = self.lstm(x)
        lstm_out = torch.transpose(lstm_out, 0, 1)
        lstm_out = torch.transpose(lstm_out, 1, 2)

        logit = self.hidden2label(lstm_out)
        logit = logit.squeeze()
        return logit


def get_LSTM(seq_length, hidden_size, num_layer=3):
    return LSTM(seq_length, hidden_size, num_layer=num_layer)


if __name__ == '__main__':
    x = torch.randn(7, 32, 48)
    net = LSTM(48, 48)
    out = net(x)
    print(out.shape)