import collect
import analyze
import visualize
import pandas as pd
import matplotlib.pyplot as plt
from config import CONFIG


if __name__== '__main__':
    resultfiles = dict()

    #collect
    resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(    # 서울특별시 데이터 생성후 파일만들기
        district=CONFIG['district'],
        **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collect.crawling_foreign_visitor(country, **CONFIG['common'])  # 외국방문 데이터 생성후 파일만들기
        resultfiles['foreign_visitor'].append(rf)

    print("resultfile ==== ",resultfiles)
    # 1. analysis and visualize
    result_analysis = analyze.analysis_correlation(resultfiles)
    print("resu===",result_analysis)
    # visualize.graph_scatter(result_analysis)

    # 2. analysis and visualize
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    print("result_analysis main::===" ,result_analysis)
    # graph_table = pd.DataFrame(result_analysis, colums=['tourspot', 'r_중국', 'r_일본', 'r_미국'])
    # graph_table = graph_table.set_index('tourspot')
    #
    # graph_table.plot(kind='bar')
    # plt.show()
