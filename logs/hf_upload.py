# %%
import pandas as pd
import pickle
import datasets
# ファイルパスを指定
file_path = 'elo_results.pkl'

# 'rb'は「バイナリ読み込みモード」を意味します
with open(file_path, 'rb') as file:
    # pickleを使用してファイルの内容を読み込む
    data = pickle.load(file)

# 読み込んだデータを表示
print(data)

# %%

data["full"]["elo_rating_final"]

# %%

df2 = data["full"]["leaderboard_table_df"]
df2 = df2.sort_values("rating", ascending=False)
ds2 = datasets.Dataset.from_pandas(df2)
ds2.push_to_hub("kanhatakeyama/chatbot-arena-ja-elo-rating")


# %%
