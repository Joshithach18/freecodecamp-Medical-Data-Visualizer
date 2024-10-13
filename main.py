# main.py

from medical_data_visualizer import draw_cat_plot, draw_heat_map

def main():
    # Generate and display the categorical plot
    cat_fig = draw_cat_plot()
    cat_fig.savefig('catplot.png')

    # Generate and display the heat map
    heat_fig = draw_heat_map()
    heat_fig.savefig('heatmap.png')

# Import and run tests from test_module.py
if __name__ == "__main__":
    main()
    import test_module
    test_module.run_tests()
