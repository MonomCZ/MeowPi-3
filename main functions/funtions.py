def scrolling_list(current_tab, modes_or_options, selected_list_index):
        selected_mode_index = (selected_mode_index + 1) % len(modes_or_options)
        selected_mode = modes_or_options[selected_mode_index]