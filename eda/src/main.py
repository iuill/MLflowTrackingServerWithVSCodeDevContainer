import pandas as pd

df_train = pd.read_csv('/workspace/dat_app/input/train.csv')
df_test = pd.read_csv('/workspace/dat_app/input/test.csv')

target = "target"

#
# sweetviz
#
import sweetviz as sv
sv_report = sv.compare([df_train, "Train"], [df_test, "Test"], target_feat=target)
sv_report.show_html("sweetviz_result.html")


#
# ydata_profiling
#
import ydata_profiling as y_pr
y_pr_train = y_pr.ProfileReport(df_train, title="train data profiling Report", minimal=False)
y_pr_train.to_file("ydata_train_result.html")

y_pr_test = y_pr.ProfileReport(df_test, title="test data profiling Report", minimal=False)
y_pr_test.to_file("ydata_test_result.html")

y_pr_compare = y_pr_train.compare(y_pr_test)
y_pr_compare.to_file("ydata_compare_result.html")

#
# autoviz
#
from autoviz.AutoViz_Class import AutoViz_Class
autoviz_train = AutoViz_Class().AutoViz(
    filename='', dfte=df_train, depVar=target, verbose=1, chart_format="html",save_plot_dir="./autoviz_train/"
    )
autoviz_test = AutoViz_Class().AutoViz(
    filename='', dfte=df_test, depVar="", verbose=1, chart_format="html",save_plot_dir="./autoviz_test/"
    )
