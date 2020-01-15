import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_bar_plot(f_label, y_name, focus_atts, fig_title, performance_flag=False):
    label_df = pd.DataFrame(f_label.keys(), columns=focus_atts)
    label_df = pd.concat([label_df, pd.DataFrame(f_label.values())], axis=1)
    fig = plt.figure(figsize=(8, 6), dpi=100)
    sns.set(style="whitegrid", font_scale=1.7)
    if len(focus_atts) == 1:
        sns.barplot(x=focus_atts[0], y=y_name, data=label_df)
    else:
        sns.barplot(x=focus_atts[0], y=y_name, hue=focus_atts[1], data=label_df)
    font_size = 20
    plt.title("after " + fig_title, fontsize=font_size)
    plt.ylabel(y_name, fontsize=font_size)
    plt.xlabel(focus_atts[0], fontsize=font_size)

    plt.yticks([x / 10 for x in range(0, 11) if x % 2 == 0], fontsize=font_size - 2)
    plt.ylim([0, 1])
    if len(focus_atts) > 1:
        if performance_flag:
            plt.legend(loc=1, fontsize=font_size - 5)
        else:
            plt.legend(loc=2, fontsize=font_size - 5)
    plt.tight_layout()