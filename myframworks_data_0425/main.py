import numpy as np
import csv

RND_MEAN = 0
RND_STD = 0.003
LEANING_RATE = 0.0001

# csv -> numpy 배열로 변경

def load_dataset():
    global data, input_cnt, output_cnt
    # 파일은 어떻게 읽어오나요?
    with open('./data/abalone.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None) # f = readline...
        rows = []
        for row in csv_reader:
            rows.append(row)
    input_cnt, output_cnt = 10, 1
    data = np.zeros([len(rows), input_cnt + output_cnt])
    print(data)

    for n,row in enumerate(rows):
        if n==16:
            print(row)
        if row[0]=="I":
            data[n,0] =1
        if row[0]=="M":
            data[n,1] =1
        if row[0]=="F":
            data[n,2] =1
        data[n,3:] = row[1:] # 원핫인코딩

# 뭘 내보내야 할
# 기울기랑 절편 
# 기준값 필요
def init_model():
    global weight, bias, input_cnt, output_cnt
    weight = np.random.normal(RND_MEAN, RND_STD[input_cnt, output_cnt])
    bias = np.zeros([output_cnt])
    
def train_and_test(epoch_count=10, mb_size = 10 ):
    # 1. 데이터를 나누세요!
    step_count = arrange_data(mb_size)
    test_x, test_y = get_data_test()

    # 2. 학습(행렬곱)
    for epoch in range(epoch_count):
        losses = []
        accs =[]

        for n in range(step_count):
            train_x, train_y = get_train_data(mb_size, n)
            loss, acc = run_train(train_x, train_y)
            losses.append(loss)
            accs.append(acc)
            pass

    # 3. 테스트

def run_train(x,y):
    #순방향 => 정확도
    output, aux_nn = forward_neuralnet(x)
    loss, aux_pp = forward_postproc(output, y)
    accuracy = eval_accuracy(output, y)
    #역방향 => 오차
    G_loss = 1.0
    G_output = backprop_postproc(G_loss, aux_pp)
    backprop_neuralnet(G_output, aux_nn)
    #
    return loss,acc

def get_train_data(mb_size,nth):
    global data, shuffle_map, test_begin_idx
    if nth == 0:
        np.random.shuffle(shuffle_map[:test_begin_idx])
    train_and_data = data[shuffle_map[ mb_size * nth : mb_size * (nth+1) ]]
    return train_data[:,:-output_cnt],train_data[:,-output_cnt:]

def arrange_data(mb_size):
    global data, shuffle_map, test_begin_idx
    shuffle_map = np.arange(data.shape[0])
    np.random.shuffle(shuffle_map)
    step_count = int(data.shape[0]*0.8)//mb_size
    test_begin_idx = step_count * mb_size
    return step_count

def get_data_test():
    global data, shuffle_map, test_begin_idx, output_cnt
    test_data = data[shuffle_map[test_begin_idx:]]
    return test_data[:, :-output_cnt], test_data[:,-output_cnt:]
    pass

if __name__ == "__main__":
    load_dataset() #csv 파일 읽는 방법
    init_model() #기울기와 절편이 넘파이 배열로 웬만하면 [][]보다는 [,]사용해서 한번에 접근
    train_and_test() # epoch, batch