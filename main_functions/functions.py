def scrolling_list(current_tab, modes,options, selected_list_index,up_down):
        if current_tab =='modes':
                selected_list_index = (selected_list_index + up_down) % len(modes)
        elif current_tab == 'options':
                selected_list_index = (selected_list_index + up_down) % len(options)
        return selected_list_index
                
        