class Config:
  def __init__(self):
#====data paths
    self.train_orig = "/content/projektR/notebooks/UNet/Train_images/train" #train dataset
    self.valid_orig = "/content/projektR/notebooks/UNet/Validation_images/validation" #validation dataset
    self.test_orig = "/content/projektR/notebooks/UNet/Test_images/test" #test dataset
    self.extension = "model0"
    self.expname = "Model 0 Only LAD Scaled size"
    self.checkpoints = "/content/projektR/notebooks/UNet/" + self.extension + "/checkpoints/"
    self.optimizer = "/content/projektR/notebooks/UNet/" + self.extension + "/optimizer/"
    self.test_results = "/content/projektR/notebooks/UNet/" + self.extension + "/test/"
#====data configure
    self.seed_value = 0
    self.imgsize = [848,848] #[1184,1184]
    self.masksize = [848,848] #[1184,1184]
    self.channels = 1
    self.threshold = 0.5
    self.train_batchsize = 4
    self.valid_batchsize = 4
    self.drop = 0.5
    self.LoadThread = 0
#====training configure
    self.epochsize = 100
    self.lr = 0.00001 #initial learning rate
    self.gamma = 0.1
    self.lr_epoch_step = 30
    self.save_model_epoch = 2
    self.num_work = 6
    
    self.cuda_dev = 1
    self.cuda_dev_list = "0,1"