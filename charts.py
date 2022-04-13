import matplotlib.pyplot as plt
from Binary import Binary
from Futoshiki import Futoshiki
import time


def generate_data_for_plots(from_files, n, is_binary, constraint_heuristic, domain_heuristic):
    bt_time, fc_time, bt_nodes, fc_nodes = [], [], [], []
    if from_files:
        if is_binary:
            x = ['binary6x6', 'binary8x8', 'binary10x10']
            add_binary(6, 'data/binary_6x6', bt_nodes, bt_time, True, constraint_heuristic,
                       domain_heuristic)
            add_binary(8, 'data/binary_8x8', bt_nodes, bt_time, True, constraint_heuristic,
                       domain_heuristic)
            add_binary(10, 'data/binary_10x10', bt_nodes, bt_time, True, constraint_heuristic,
                       domain_heuristic)
            add_binary(6, 'data/binary_6x6', fc_nodes, fc_time, False, constraint_heuristic,
                          domain_heuristic)
            add_binary(8, 'data/binary_8x8', fc_nodes, fc_time, False, constraint_heuristic,
                          domain_heuristic)
            add_binary(10, 'data/binary_10x10', fc_nodes, fc_time, False, constraint_heuristic,
                          domain_heuristic)
        else:
            x = ['futoshiki4x4', 'futoshiki5x5', 'futoshiki6x6']
            add_futoshiki(4, 'data/futoshiki_4x4', bt_nodes, bt_time, True, constraint_heuristic,
                       domain_heuristic)
            add_futoshiki(5, 'data/futoshiki_5x5', bt_nodes, bt_time, True, constraint_heuristic,
                       domain_heuristic)
            add_futoshiki(6, 'data/futoshiki_6x6', bt_nodes, bt_time, True, constraint_heuristic,
                       domain_heuristic)
            add_futoshiki(4, 'data/futoshiki_4x4', fc_nodes, fc_time, False, constraint_heuristic,
                       domain_heuristic)
            add_futoshiki(5, 'data/futoshiki_5x5', fc_nodes, fc_time, False, constraint_heuristic,
                       domain_heuristic)
            add_futoshiki(6, 'data/futoshiki_6x6', fc_nodes, fc_time, False, constraint_heuristic,
                       domain_heuristic)
    else:
        x = []
        for el in range(1, n+1):
            if is_binary:
                if el % 2 == 0:
                    x.append(str(el))
                    add_binary(el, '', bt_nodes, bt_time, True, constraint_heuristic, domain_heuristic)
                    add_binary(el, '', fc_nodes, fc_time, False, constraint_heuristic, domain_heuristic)
            else:
                x.append(str(el))
                add_futoshiki(el, '', bt_nodes, bt_time, True, constraint_heuristic, domain_heuristic)
                add_futoshiki(el, '', fc_nodes, fc_time, False, constraint_heuristic, domain_heuristic)

    return x, bt_time, fc_time, bt_nodes, fc_nodes


def add_binary(n, file, binary_nodes, binary_time,is_backtracking, constraint_heuristic, domain_heuristic):
    start = time.time()
    print('binary', is_backtracking, constraint_heuristic, domain_heuristic)
    binary_nodes.append(Binary(n, file=file, assignment={}).binary(is_backtracking,
                                                                constraint_heuristic,
                                                                domain_heuristic))
    end = time.time()
    binary_time.append(end-start)


def add_futoshiki(n, file, futoshiki_nodes, futoshiki_time, is_backtracking, constraint_heuristic, domain_heuristic):
    start = time.time()
    print('futoshiki', is_backtracking, constraint_heuristic, domain_heuristic)
    futoshiki_nodes.append(Futoshiki(n, file=file, assignment={}).futoshiki(is_backtracking,
                                                                constraint_heuristic,
                                                                domain_heuristic))
    end = time.time()
    futoshiki_time.append(end-start)


def draw_plots(x, bt_time, fc_time, bt_nodes, fc_nodes):
    plt.plot(x, bt_time, label="BT")
    plt.plot(x, fc_time, label="FC")
    plt.title("Time duration")
    plt.legend()
    plt.show()
    plt.plot(x, bt_nodes, label="BT")
    plt.plot(x, fc_nodes, label="FC")
    plt.title("Nodes visits")
    plt.legend()
    plt.show()

    # fig, ax = plt.subplots(2)
    # ax[0].plot(x, bt_time, label="BT")
    # ax[0].plot(x, fc_time, label="FC")
    # ax[0].set_title("Time duration", y=0.8)
    # ax[0].legend()
    # ax[1].plot(x, bt_nodes, label="BT")
    # ax[1].plot(x, fc_nodes, label="FC")
    # ax[1].set_title("Nodes visits", y=0.8)
    # ax[1].legend()
    # plt.show()

    #fig, ax = plt.subplots(2)
