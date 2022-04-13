import charts

if __name__ == '__main__':
    x, bt_time, fc_time, bt_nodes, fc_nodes = charts.generate_data_for_plots(from_files=True, n=6, is_binary=True,
                                                                             constraint_heuristic=False,
                                                                             domain_heuristic=True)
    print(x, bt_time, fc_time, bt_nodes, fc_nodes)
    charts.draw_plots(x, bt_time, fc_time, bt_nodes, fc_nodes)

