import os
from dotenv import load_dotenv
import datetime
import json
from semanticscholar import SemanticScholar


def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__


def download_dataset(ss_api_key):
    sch = SemanticScholar(api_key=ss_api_key)

    ds_papers = sch.search_paper('data science', limit=100)
    se_papers = sch.search_paper('software engineering', limit=100)
    bi_papers = sch.search_paper('bioinformatics', limit=100)
    graph_papers = sch.search_paper('graph theory', limit=100)
    db_papers = sch.search_paper('database', limit=100)

    dataset = [ds_papers, se_papers, bi_papers, graph_papers, db_papers]

    result = []
    for data in dataset:
        length = 1
        for res in data:
            if length > 500:
                break
            length += 1
            result.append(res)

    with open('data1/dataset.json', 'w+') as f:
        json.dump(result, f, default=json_default)


if __name__ == '__main__':
    load_dotenv()
    SS_API_KEY = os.getenv('SS_API_KEY')

    download_dataset(SS_API_KEY)
