import matplotlib.pyplot as plt


def plot_markers(ax, well, depth, data_Y, df_markers):
        ax.plot(data_Y, depth, color='blue')
        ax.invert_yaxis()
        ax.set_title(well)

        gr_medio = data_Y.mean() #TODO melhorar isso, pegar o gama do ponto de fato 
        for mark, dept in (df_markers.loc[well]).items():
            try:
                if not dept:
                    continue
            except:
                 print("Marcadores duplicados???")

            ax.plot(gr_medio, dept, color='red')
            ax.annotate(mark, (gr_medio, dept)) #, textcoords="offset points") #, xytext=(10,10), ha='center')

def show_markers(dict_data, df_markers, depth="DEPTH", channel="GR", **kwargs):
    
    n_plots = len(dict_data)
    fig, ax = plt.subplots(ncols=n_plots, **kwargs)

    for ii, (well, data) in enumerate(dict_data.items()):
        well_name = well.split("_")[0]
        plot_markers(ax[ii], well_name, data[depth], data[channel], df_markers)

    return fig, ax