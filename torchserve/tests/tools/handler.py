import torch
from ts.torch_handler.base_handler import BaseHandler


class ModelHandler(BaseHandler):
    def preprocess(self, data):
        return torch.as_tensor([data[0]["body"]["input"]], device=self.device)
