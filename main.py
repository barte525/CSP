from Binary import Binary
from Futoshiki import Futoshiki
import time

if __name__ == '__main__':
    print('binary 10x10')
    Binary(10, file='data/binary_10x10', assignment={}).print_solution(is_backtracking=True,
                                                                       constraint_heuristic=True,
                                                                       domain_heuristic=False)
    print('binary 8x8')
    Binary(8, file='data/binary_8x8', assignment={}).print_solution(is_backtracking=True,
                                                                    constraint_heuristic=True,
                                                                    domain_heuristic=False)
    print('binary 6x6')
    Binary(6, file='data/binary_6x6', assignment={}).print_solution(is_backtracking=True,
                                                                    constraint_heuristic=True,
                                                                    domain_heuristic=False)
    print('futoshiki 4x4')

    Futoshiki(4, file='data/futoshiki_4x4', assignment={}).print_solution(is_backtracking=True,
                                                                          constraint_heuristic=True,
                                                                          domain_heuristic=False)
    print('futoshiki 5x5')
    Futoshiki(5, file='data/futoshiki_5x5', assignment={}).print_solution(is_backtracking=True,
                                                                          constraint_heuristic=True,
                                                                          domain_heuristic=False)
    start = time.time()
    Futoshiki(6, file='data/futoshiki_6x6', assignment={}).futoshiki(is_backtracking=True,
                                                                     constraint_heuristic=False,
                                                                     domain_heuristic=False)
    end = time.time()
    print("Futoshiki 6x6, Backtracking, no heuristic:", end - start)
    start = time.time()
    Futoshiki(6, file='data/futoshiki_6x6', assignment={}).futoshiki(is_backtracking=True,
                                                                     constraint_heuristic=True,
                                                                     domain_heuristic=False)
    end = time.time()
    print("Futoshiki 6x6, Backtracking, variable heuristic:", end - start)
    start = time.time()
    Futoshiki(6, file='data/futoshiki_6x6', assignment={}).futoshiki(is_backtracking=True,
                                                                     constraint_heuristic=False,
                                                                     domain_heuristic=True)
    end = time.time()
    print("Futoshiki 6x6, Backtracking, domain heuristic:", end - start)
    start = time.time()
    Futoshiki(6, file='data/futoshiki_6x6', assignment={}).futoshiki(is_backtracking=False,
                                                                     constraint_heuristic=False,
                                                                     domain_heuristic=False)
    end = time.time()
    print("Futoshiki 6x6, Forward checking, no heuristic:", end - start)
    start = time.time()
    Futoshiki(6, file='data/futoshiki_6x6', assignment={}).futoshiki(is_backtracking=False,
                                                                     constraint_heuristic=True,
                                                                     domain_heuristic=False)
    end = time.time()
    print("Futoshiki 6x6, Forward checking, variable heuristic:", end - start)
    start = time.time()
    Futoshiki(6, file='data/futoshiki_6x6', assignment={}).futoshiki(is_backtracking=False,
                                                                     constraint_heuristic=False,
                                                                     domain_heuristic=True)
    end = time.time()
    print("Futoshiki 6x6, Forward checking, domain heuristic:", end - start)

    start = time.time()
    Binary(10, file='data/binary_10x10', assignment={}).binary(is_backtracking=True,
                                                               constraint_heuristic=False,
                                                               domain_heuristic=False)
    end = time.time()
    print("Binary 10x10, Backtracking, no heuristic:", end - start)
    start = time.time()
    Binary(10, file='data/binary_10x10', assignment={}).binary(is_backtracking=True,
                                                               constraint_heuristic=True,
                                                               domain_heuristic=False)
    end = time.time()
    print("Binary 10x10, Backtracking, variable heuristic:", end - start)
    start = time.time()
    Binary(10, file='data/binary_10x10', assignment={}).binary(is_backtracking=True,
                                                               constraint_heuristic=False,
                                                               domain_heuristic=True)
    end = time.time()
    print("Binary 10x10, Backtracking, domain heuristic:", end - start)
    start = time.time()
    Binary(10, file='data/binary_10x10', assignment={}).binary(is_backtracking=False,
                                                               constraint_heuristic=False,
                                                               domain_heuristic=False)
    end = time.time()
    print("Binary 10x10, Forward checking, no heuristic:", end - start)
    start = time.time()
    Binary(10, file='data/binary_10x10', assignment={}).binary(is_backtracking=False,
                                                               constraint_heuristic=True,
                                                               domain_heuristic=False)
    end = time.time()
    print("Binary 10x10, Forward checking, variable heuristic:", end - start)
    start = time.time()
    Binary(10, file='data/binary_10x10', assignment={}).binary(is_backtracking=False,
                                                               constraint_heuristic=False,
                                                               domain_heuristic=True)
    end = time.time()
    print("Binary 10x10, Forward checking, domain heuristic:", end - start)

    start = time.time()
    Binary(12, assignment={}).binary(is_backtracking=True,
                                     constraint_heuristic=False,
                                     domain_heuristic=True)
    end = time.time()
    print("Binary 12x12, Backtracking, domain heuristic:", end - start)
    # start = time.time()
    # Binary(12, assignment={}).binary(is_backtracking=True,
    #                                  constraint_heuristic=False,
    #                                  domain_heuristic=False)
    # end = time.time()
    # print("Binary 12x12, Backtracking, no heuristic:", end - start)

