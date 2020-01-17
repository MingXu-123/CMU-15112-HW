from learnhmm import *
from math import log
import sys


def new_dict(infile_path):
    res = dict()
    index = 0
    with open(infile_path, 'r') as f:
        for item in f:
            char = item.strip()
            res[index] = char
            index += 1
    return res


def viterbi(prior, trans, emit, example, len_tag_dict):
    predict = []
    W = np.zeros((len(example), len_tag_dict))
    B = np.zeros((len(example), len_tag_dict))
    # print(example)
    # print(">>>>>")
    # print(trans)
    for t in range(len(example)):
        if t == 0:
            # print(np.array(prior).T)
            # print(emit[:, example[t]])
            W[t] = prior + emit[:, example[t]]
            for i in range(len_tag_dict):
                B[t][i] = i
        # print(W)
        # print(" ")
        # print(B)
        else:
            # print(W)
            # print(B)
            for k in range(len_tag_dict):
                # print((t, k))
                W_t_minus_1 = W[t - 1]
                # print(W_t_minus_1)
                # print("asdsad")
                tmp = []
                for j in range(len_tag_dict):
                    # print(W_t_minus_1[j])
                    tmp_val = W_t_minus_1[j] + trans[j][k] + emit[k][example[t]]
                    tmp.append(tmp_val)
                # print("tmp = [] is" ,tmp)
                # print("argmax is", np.argmax(tmp))
                index = np.argmax(tmp)
                B[t][k] = index
                W[t][k] = tmp[index]
    # print("final W is\n", W)
    # print("final B is\n", B)
    # print(W[len(example) - 1])
    y_hat_T = np.argmax(W[len(example) - 1])
    # print(y_hat_T)
    predict.append(y_hat_T)
    # print(">>>>>>>>>>>>>>>>>>>.")
    for t in range(len(example) - 1, 0, -1):
        # print(t)
        y_hat_T_minus_1 = B[t][int(y_hat_T)]
        # print("y_hat_T_minus_1 is", y_hat_T_minus_1)
        predict.insert(0, y_hat_T_minus_1)
        y_hat_T = y_hat_T_minus_1
    # print("predict is ", predict)
    res = []
    for i in range(len(predict)):
        res.append(int(predict[i]))
    # print("final res is", res)
    return res


def main():
    test_input = sys.argv[1]
    index_to_word = sys.argv[2]
    index_to_tag = sys.argv[3]
    hmmprior = sys.argv[4]
    hmmemit = sys.argv[5]
    hmmtrans = sys.argv[6]
    predicted_file = sys.argv[7]
    metrics_file = sys.argv[8]

    words, tags = parse_data(test_input)
    # print(words)
    # print(tags)
    tag_dict = load_index_dict(index_to_tag)
    word_dict = load_index_dict(index_to_word)
    # print(tag_dict)
    # print(word_dict)

    tag_dict_new = new_dict(index_to_tag)
    word_dict_new = new_dict(index_to_word)
    # print(tag_dict_new)
    # print(word_dict_new)

    words_idx_lst = convert_to_index(words, word_dict)
    tags_idx_lst = convert_to_index(tags, tag_dict)
    # print(words_idx_lst)
    # print(tags_idx_lst)
    prior = np.loadtxt(hmmprior)
    trans = np.loadtxt(hmmtrans)
    emit = np.loadtxt(hmmemit)

    prior = np.log(prior)
    trans = np.log(trans)
    emit = np.log(emit)
    # print(prior)
    # print(" ")
    # print(trans)
    # print(" ")
    # print(emit)
    # print(" ")

    # print(".................................")
    out_str = ""
    for example in words_idx_lst:
        predict = viterbi(prior, trans, emit, example, len(tag_dict))
        sub_str = ""
        for word, tag in zip(example, predict):
            # print(word, tag)
            word_str = word_dict_new[word]
            pred_str = tag_dict_new[tag]
            sub_str += (word_str + "_" + pred_str + " ")
        sub_str = sub_str[:-1]
        out_str += sub_str + "\n"
    out_str = out_str[:-1]
    print("out_str is", out_str)
    write(predicted_file, out_str)


if __name__ == '__main__':
    main()